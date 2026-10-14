function showMap(id, lat, long) {
    const mapLayer = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    });
    const satLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
        maxZoom: 19,
        attribution: '&copy; <a href="https://esri.com">ESRI</a>'
    });
    const map = L.map(id, {
        layers: [mapLayer],
        center: [lat, long],
        zoom: 14,
        scrollWheelZoom: true,
    });
    const markers = L.layerGroup().addTo(map);
    L.marker([52.4786778, -1.9266194444444442]).addTo(markers).bindPopup("<b>Icknield Port Road</b>");
    L.marker([52.4778667, -1.927433333333333]).addTo(markers).bindPopup("<b>Ladywood Fire Station</b>");
    L.marker([52.4756056, -1.9234499999999999]).addTo(markers).bindPopup("<b>Leyburn Road</b>");
    L.marker([52.4800361, -1.9303333333333332]).addTo(markers).bindPopup("<b>Osler Street</b>");
    L.marker([52.4827556, -1.922722222222222]).addTo(markers).bindPopup("<b>Cope Street</b>");
    L.marker([52.480375, -1.9160499999999998]).addTo(markers).bindPopup("<b>Clement Street</b>");
    L.marker([52.4746306, -1.9180944444444443]).addTo(markers).bindPopup("<b>Ruston Street</b>");
    L.marker([52.4772694, -1.915647222222222]).addTo(markers).bindPopup("<b>Crescent Theatre</b>");
    L.marker([52.4842222, -1.9206888888888887]).addTo(markers).bindPopup("<b>King Edwards Road</b>");
    L.marker([52.4843194, -1.918422222222222]).addTo(markers).bindPopup("<b>Spring Hill Island</b>");
}
document.addEventListener("DOMContentLoaded", () => {
    showMap('map', 52.481346, -1.918235);
});