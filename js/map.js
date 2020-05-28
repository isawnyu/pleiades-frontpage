/* set up the main map */
mapboxgl.accessToken = 'pk.eyJ1IjoiaXNhd255dSIsImEiOiJja2FlaWk4MG0yaHY0MnNvemRneWF0d2RnIn0.FgwFQtymPTHYPYYha5mfHw';
var coordsCenter = [62.0, 38.0];
var coordsInit = coordsCenter;
var zoomInit = 2;
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
    zoomControl: false,
    attributionControl: false,
    style: 'mapbox://styles/isawnyu/cjzy7tgy71wvr1cmj256f4dqf',
    container: 'map'
};

var map = new mapboxgl.Map(mapOptionsInit);
map = map.addControl(new mapboxgl.AttributionControl({
        customAttribution: "Ancient topography by AWMC, 2014 (cc-by-nc)."
    }));

/* animate the map with random Pleiades places */
var placesURL = 'https://raw.githubusercontent.com/ryanfb/pleiades-geojson/gh-pages/name_index.json'
var placesData = null
var markerCurrent = null
var popupCurrent = null
var timer = null

function displayPlace() {
    if (markerCurrent != null) {
        markerCurrent.addTo(map);
        popupCurrent.addTo(map);
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
    var el = document.createElement('div');
    el.className = 'marker';
    el.style.backgroundImage = 'url(https://pleiades.stoa.org/map_icons/justice-blue.png)';
    el.style.width = '32px';
    el.style.height = '37px';
    var placeReq = $.getJSON(jsonURL, function(data) {
    })
        .done(function(data) {
            var bounds = data["bbox"];
            if (bounds != null) {

                var rFeature = data['features'].filter(function (obj) { return obj.properties.description == 'representative point'})[0];
                if (rFeature.geometry.type == 'Point') {
                    var placeTitle = data["title"];
                    var placeDescription = data["description"];
                    if (placeDescription.search("cited: ") == -1 && placeDescription.search("TAVO Index") == -1 && placeDescription.search("→") == -1) {
                        var lat = rFeature.geometry.coordinates[1]
                        var lon = rFeature.geometry.coordinates[0]
                        if (markerCurrent === undefined || markerCurrent === null) {
                        } else {
                            markerCurrent.remove();
                            popupCurrent.remove();
                            markerCurrent = null;
                            popupCurrent = null;
                        }

                        
                        latLng = new mapboxgl.LngLat(lon, lat);
                        markerCurrent = new mapboxgl.Marker(el).setLngLat(latLng);
                        var popHtml = '<div class="title"><a href="/places/' + pleiadesID + '">' + placeTitle + '</a></div><div class="description">' + placeDescription + '</div>';
                        popupCurrent = new mapboxgl.Popup({
                            anchor: "bottom",
                            closeButton: false,
                            maxWidth: "280px",
                            offset: {"bottom": [0,-17]}
                        }).setHTML(popHtml).setLngLat(latLng);
                        
                        markerCurrent.setPopup(popupCurrent);
                        markerCurrent.addTo(map);
                        map.flyTo({
                            center:  latLng,
                            zoom: zoomMax,
                            speed: 0.5
                        });
                        timer = setTimeout(animateMap, 10000); 
                    } else { animateMap() }
                } else { animateMap() }
            } else { animateMap() }
        })
        .fail(function() {
            console.log("failed to retrieve pleiades geojson from " + jsonURL)
        });
}

