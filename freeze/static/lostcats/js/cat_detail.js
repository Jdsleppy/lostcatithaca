var mapCreation = mapCommon.makeMap();
var map = mapCreation[0];
var catIcon = mapCreation[1];

var cat = JSON.parse(document.getElementById("cat-data").textContent);

L.marker([cat.latitude, cat.longitude]).setIcon(catIcon).addTo(map);

map.setView([cat.latitude, cat.longitude], 18);
