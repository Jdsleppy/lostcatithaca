var mapCommon = (function () {
  var contents = "contents";

  var changeHTML = function () {
    var element = document.getElementById("attribute-to-change");
    element.innerHTML = contents;
  };

  return {
    makeMap: function () {
      var x = 42.439737520156676;
      var y = -76.50087118148805;
      var radius = 0.2;

      var map = L.map("map", {
        // https://github.com/Leaflet/Leaflet/issues/7255#issuecomment-732082150
        tap: false,
      })
        .setView([x, y], 15)
        .setMaxBounds([
          [x - radius, y + radius],
          [x + radius, y - radius],
        ])
        .setMinZoom(12);
      map.zoomControl.setPosition("bottomright");

      // Hack to get popup sizing and autopanning working
      // https://www.drupal.org/project/ip_geoloc/issues/2850978
      map.on("popupopen", function (e) {
        var popupImages = e.popup
          .getElement()
          .getElementsByClassName("popupImage");

        for (var i = 0; i < popupImages.length; i++) {
          var popupImage = popupImages[i];
          popupImage.addEventListener("load", function () {
            e.popup.update();
          });
        }
      });

      L.tileLayer(
        "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}",
        {
          attribution:
            'Data © <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
          maxZoom: 18,
          id: "jdsleppy/ckpj45hgi04z717p85j05u014",
          tileSize: 512,
          zoomOffset: -1,
          accessToken:
            "pk.eyJ1IjoiamRzbGVwcHkiLCJhIjoiY2twaGRpcHMzMGJpZzJ1b2xheDQ5aWE1byJ9.8G_2xnYGoyhBmcLHT2bz-g",
        }
      ).addTo(map);

      var catIcon = L.icon({
        iconUrl: "/static/lostcats/images/map-icon.png",
        iconSize: [22, 20],
        iconAnchor: [11, 10],
        popupAnchor: [0, -10],
      });

      return [map, catIcon];
    },
  };
})();
