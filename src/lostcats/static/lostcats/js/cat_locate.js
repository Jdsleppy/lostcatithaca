var mapCreation = mapCommon.makeMap();
var map = mapCreation[0];
var catIcon = mapCreation[1];

/** @type {HTMLButtonElement)} */
var okButton = document.getElementById("interactionButton");
/** @type {HTMLFormElement)} */
var form = document.getElementById("catLocateForm");
/** @type {HTMLInputElement)} */
var latitudeInput = document.getElementById("id_latitude");
/** @type {HTMLInputElement)} */
var longitudeInput = document.getElementById("id_longitude");

function setCenter() {
  var center = map.getCenter();
  latitudeInput.value = center.lat;
  longitudeInput.value = center.lng;
}

map.on("moveend", function () {
  setCenter();
});

okButton.addEventListener("click", function () {
  form.submit();
});

setCenter();
