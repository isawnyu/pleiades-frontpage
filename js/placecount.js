      function placecount() {
      /* Get count of places from API status */
      $.getJSON(
        "http://pleiades.stoa.org/api/status", 
        function(data) {
          $("#placesSearchLegend", document).text(
            "search the " +
            data['num_places'].toString().replace(
              /\B(?=(?:\d{3})+(?!\d))/g, ",") +
            " places" );
          $("#placesSearchLegend", document).css("visibility", "visible");
        });
    }
