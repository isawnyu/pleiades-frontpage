/* set up the main map */
L.mapbox.accessToken = 'pk.eyJ1IjoiaXNhd255dSIsImEiOiJBWEh1dUZZIn0.SiiexWxHHESIegSmW8wedQ';
var coordsCenter = [38.0, 62.0];
var coordsInit = coordsCenter;
var zoomInit = 3;
var zoomMax = 6;
var mapOptionsInit = {
    attributionControl: {compact: true},
    boxZoom: false,
    center: coordsCenter,
    closePopupOnClick: false,
    doubleClickZoom: false,
    dragging: false,
    keyboard: false,
    maxZoom: zoomMax,
    scrollWheelZoom: false,
    tap: false,
    touchZoom: false,
    zoom: zoomInit,
    zoomControl: false
          };
var map = L.mapbox.map('map', 'isawnyu.map-knmctlkh', mapOptionsInit);
map.attributionControl.addAttribution("Ancient topography by AWMC, 2014 (cc-by-nc).");

/* animate the map with random Pleiades places */
var placesURL = 'https://raw.githubusercontent.com/ryanfb/pleiades-geojson/gh-pages/name_index.json'
var placesData = null
var placeIcon = new L.Icon({
    iconUrl: "https://pleiades.stoa.org/map_icons/justice-blue.png",
    iconSize:     [32, 37],
    iconAnchor:   [16, 37]
});
var markerCurrent = null
var popupCurrent = null
var timer = null

function displayPlace() {
    if (markerCurrent != null) {
        markerCurrent.addTo(map);
        markerCurrent.openPopup()
    }    
}
map.on('zoomend', function() {
    displayPlace()
});
map.on('moveend', function() {
    displayPlace()
});
var placesReq = $.getJSON(placesURL, function(data) {
})
    .done(function(data) {
        placesData = data;
        timer = setTimeout(animateMap, 6000);
    })
    .fail(function() {
        console.log("failed to retrieve places data from placesURL" + placesURL)
    });

function animateMap() {

    var pleiadesID = placesData[Math.floor((Math.random() * placesData.length) + 1)][1];
    mapPlace(pleiadesID);
}

function mapPlace(pleiadesID) {
    var jsonURL = "https://raw.githubusercontent.com/ryanfb/pleiades-geojson/gh-pages/geojson/" + pleiadesID + ".geojson"
    var placeReq = $.getJSON(jsonURL, function(data) {
    })
        .done(function(data) {
            if (markerCurrent === undefined || markerCurrent === null) {
            } else {
                markerCurrent.closePopup();
                map.removeLayer(markerCurrent);    
                markerCurrent = null;
            }
            var bounds = data["bbox"];
            if (bounds != null) {
                var reprPoint = data["reprPoint"];
                var placeTitle = data["title"];
                var placeDescription = data["description"];
                if (placeDescription.search("cited: ") == -1 && placeDescription.search("TAVO Index") == -1 && placeDescription.search("→") == -1) {
                    latLng = new L.LatLng(reprPoint[1], reprPoint[0]);
                    markerCurrent = new L.Marker(latLng, {
                        icon: placeIcon
                    });                    
                    var popHtml = '<div class="title"><a href="http://pleiades.stoa.org/places/' + pleiadesID + '">' + placeTitle + '</a></div><div class="description">' + placeDescription + '</div>';
                    markerCurrent.bindPopup(popHtml, {offset: new L.Point(0, -27), closeButton: false});
                    map.setView(latLng, zoomMax, {
                        pan: {
                            animate: true,
                            duration: 3
                        },
                        zoom: {
                            animate: true
                        }
                    });
                    timer = setTimeout(animateMap, 10000); 
                } else {
                    animateMap()
                }
            } else {
                animateMap()
            }
        })
        .fail(function() {
            console.log("failed to retrieve pleiades geojson from " + jsonURL)
        });
}

