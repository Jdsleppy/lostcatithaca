var mapCreation = mapCommon.makeMap();
var map = mapCreation[0];
var catIcon = mapCreation[1];

var cats = JSON.parse(document.getElementById("cats-data").textContent);

for (var cat of cats) {
  L.marker([cat.latitude, cat.longitude])
    .setIcon(catIcon)
    .bindPopup(
      `<div class="popupContainer">
        <h1>${cat.title}</h1>
        <a class="d-flex flex-column align-items-center" href="${cat.url}">
          <span>
            details<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" fill="currentColor" class="bi bi-chevron-double-right" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M3.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L9.293 8 3.646 2.354a.5.5 0 0 1 0-.708z"/>
              <path fill-rule="evenodd" d="M7.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L13.293 8 7.646 2.354a.5.5 0 0 1 0-.708z"/>
            </svg>
          </span>
          <img class="popupImage rounded shadow" src="${cat.thumbnail_url}">
        </a>
      </div>`,
      {
        closeOnEscapeKey: true,
        autoPanPadding: L.point(10, 10),
      }
    )
    .addTo(map);
}
