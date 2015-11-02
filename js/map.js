    var latlng0 = new L.LatLng(38.0, 42.0);
    
    var tiles = L.tileLayer(
    //    'http://static.ahlfeldt.se/srtm/imperium/{z}/{x}/{y}.png', {
    //    'http://api.tiles.mapbox.com/v3/isawnyu.map-p75u7mnj/{z}/{x}/{y}.png', {
        'http://api.tiles.mapbox.com/v3/isawnyu.map-knmctlkh/{z}/{x}/{y}.png', {

            maxZoom: 7,
            reuseTiles: true,
            updateWhenIdle: false,
            noWrap: true
            });

    var ppoints = L.tileLayer(
        'http://api.tiles.mapbox.com/v3/isawnyu.75cul3di/{z}/{x}/{y}.png', {
            maxZoom: 7,
            reuseTiles: true,
            updateWhenIdle: false,
            opacity: 0.5,
            noWrap: true
            });
            
    var placeIcon = new L.Icon({
        iconUrl: "http://atlantides.org/images/justice-blue.png",
        iconSize:     [32, 37],
        iconAnchor:   [16, 37]
      });
    var marker = new L.Marker([-90, 45], {icon: placeIcon});

    var msg = null;
    var infoWindow = new L.Popup({
        offset: new L.Point(0, -30),
        closeButton: false,
        maxWidth: 500 });

    var current = null;
    var next = [];
    var prev = [];

    var timer = null;
    var count = 0;
    var limit = 100;
    var interval = 8000;
    
    /* Begin in recent-seeking state */
    var state = "recent-seeking";
    var url = "http://pleiades.stoa.org/api/ssdRecentPlaceJson";

    var map = null;

    function preset() {
      var d = { 
        "bbox": null
      }
      map = L.map('map', {
          center: latlng0,
          zoom: 6,
          closePopupOnClick: false,
          dragging: false,
          touchZoom: false,
          scrollWheelZoom: false,
          doubleClickZoom: false,
          boxZoom: false,
          keyboard: false,
          zoomControl: false,
          attributionControl: false });
      tiles.addTo(map);
      ppoints.addTo(map);
      map.setZoom(4, {"animate":true});
      placecount();
      timer = setTimeout(postset, 5000);
    }
    
    function postset() {
      time = setTimeout(play, 0);
    }

    function play() {
      
      if (count > limit) {
        if (state == "recent-seeking") { // switch state
          state = "any-seeking";
          count = 0;
          url = "http://pleiades.stoa.org/api/ssdAnyPlaceJson";
        }
        else { // quit
          current = null;
          return null;
        }
      }
      if (current != null) {
        prev.push(current);
      }
      if (next.length == 0) {
        $.getJSON(url, function(data) {
          limit = data['limit'];
          current = data['results'][0]['id'];
          if ($.inArray(current, prev) < 0 && 
              $.inArray(current, next) < 0) {
            show(data['results'][0]);
          }
          else {
            current = data['results'][1]['id'];
            show(data['results'][1]);
          }
        });
      }
      else {
        current = next.shift();
        var nextUrl = "http://pleiades.stoa.org/places/" + current + "/json";
        $.getJSON(nextUrl, function(data) {
          current = data["id"];
          show(data);
        });
      }
      count = count + 1;
      timer = setTimeout(play, interval);
    }

    function forward() {
      if (current != null) { prev.push(current); }
      if (next.length == 0) {
        $.ajax({
          url: url,
          dataType: 'json',
          headers: {'If-None-Match': '*'},
          success: function(data) {
            limit = data['limit'];
            current = data['results'][0]['id'];
            if ($.inArray(current, prev) < 0 && 
                $.inArray(current, next) < 0) {
              show(data['results'][0]);
            }
            else {
              current = data['results'][1]['id'];
              show(data['results'][1]);
            }
          }
        });
      }
      else {
        current = next.shift();
        var nextUrl = "http://pleiades.stoa.org/places/" + current + "/json";
        $.getJSON(nextUrl, function(data) {
          current = data["id"];
          show(data);
        });
      }
    }

    function back() {
      if (current != null) { next.unshift(current); }
      if (prev.length > 0) {
        current = prev.pop();
        var backUrl = "http://pleiades.stoa.org/places/" + current + "/json";
      }
      else {
        return null;
      }
      $.getJSON(backUrl, function(data) {
        current = data["id"];
        show(data);
      });
    }

    function show(data) {

      var bounds = data["bbox"];
      if (bounds == null) {
        latlng = latlng0;
      }
      else {
        latlng = new L.LatLng(
          (bounds[1]+bounds[3])/2.0, (bounds[0]+bounds[2])/2.0);
      }
      

      map.closePopup();
      var msg = $("#infoWindowContent").clone(true, true);
      var link = "http://pleiades.stoa.org/places/" + data["id"];
      $("#iwcTitle #detailsLink", msg).attr("href", link);
      $("#iwcTitle #detailsLink", msg).text(data["title"]);
      $("#iwcDescription", msg).text(data["description"]);

      if (data["recent_changes"] != null) {
        var items = $.map(data["recent_changes"], function(value){
          var q = value["modified"];
          var modified = new Date(
            Date.UTC(
              parseInt(q.substring(0,4)),
              parseInt(q.substring(5,7))-1,
              parseInt(q.substring(8,10)),
              parseInt(q.substring(11,13)),
              parseInt(q.substring(14,16))))
          return modified.toDateString() + " by " + value["principal"];
          });
        $("#iwcByline", msg).text("Last modified: " + items.join(", "));
      }
      else {
        $("#iwcByline", msg).hide();
      }

      $(msg).show();
      $("iwcNav", msg).hide();
      
      infoWindow.setLatLng(latlng);
      infoWindow.setContent($(msg).html());
      
      marker.setLatLng(latlng);
      map.openPopup(infoWindow);

      if (count == 1) {
        po = {"animate":true, "duration":3.0}
      }
      else {
        po = {"animate":true, "duration":1.0}
      }
      zo = {"animate":true}
      if (bounds == null) {
        map.removeLayer(marker)
        map.panTo(latlng, po);
        map.setZoom(4, zo);
      }
      else {
        marker.addTo(map)
        map.panTo([latlng.lat+1.2, latlng.lng], po);
        map.setZoom(6, zo);
      }
    }

    $(document).keyup(function(e) {
      if (e.keyCode == 27) { count = limit + 1; } // esc ends the slideshow
      /* Toggle pause/play with p key */
      else if (e.keyCode == 80) {
        if (timer == null) {
          timer=setTimeout(play, 500);
        }
        else {
          clearTimeout(timer);
          timer = null;
        }
      }
      else if (e.keyCode == 74) { back(); } // j goes back
      else if (e.keyCode == 75) { forward(); } // j goes forward
    });


