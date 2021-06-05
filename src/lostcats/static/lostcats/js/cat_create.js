var mapCreation = mapCommon.makeMap();
var map = mapCreation[0];
var catIcon = mapCreation[1];

var cat = JSON.parse(document.getElementById("cat-data").textContent);

L.marker([cat.latitude, cat.longitude]).setIcon(catIcon).addTo(map);

map.setView([cat.latitude, cat.longitude], 18);

/** @type {HTMLButtonElement)} */
var submitButton = document.getElementById("submit-button");

submitButton.addEventListener("click", function (e) {
  var submitButtonHeight = submitButton.clientHeight;
  submitButton.classList.add("d-none");
  var spinner = document.getElementsByClassName("spinner").item(0);
  spinner.setAttribute("style", `height: ${submitButtonHeight.toString()}px`);
  document.getElementsByClassName("spinner").item(0).classList.remove("d-none");
});
