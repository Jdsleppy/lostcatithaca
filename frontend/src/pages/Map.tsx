import React from 'react';
import L from 'leaflet';

import mapIcon from '../images/down-arrow.png';

import './Map.css';

class Map extends React.Component {
  render() {
    return (
      <div id="map"></div>
    );
  }

  componentDidMount() {
    const x = 42.4436853
    const y = -76.4971411;
    const radius = 0.05;
    const map = L.map('map')
      .setView([x, y], 14)
      .setMaxBounds([[x - radius, y + radius], [x + radius, y - radius]])
      .setMinZoom(12);

    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
      attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
      maxZoom: 18,
      id: 'mapbox/streets-v11',
      tileSize: 512,
      zoomOffset: -1,
      accessToken: 'pk.eyJ1IjoiamRzbGVwcHkiLCJhIjoiY2twaGRpcHMzMGJpZzJ1b2xheDQ5aWE1byJ9.8G_2xnYGoyhBmcLHT2bz-g'
    }).addTo(map);

    const catIcon = L.icon({
      iconUrl: mapIcon,
      iconSize: [16, 29],
      iconAnchor: [8, 29],
      popupAnchor: [0, -14],
    })
    L.marker([42.438121, -76.501687])
      .setIcon(catIcon)
      .bindPopup(`<div class="popup-container"><a href="#">Cat on pole</a><img src="${mapIcon}"></div>`)
      .addTo(map);
  }
}
export default Map;