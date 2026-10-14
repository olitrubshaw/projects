const busStops = [
    { name: "Icknield Port Road", slug: "icknield-port-road" },
    { name: "Ladywood Fire Station", slug: "ladywood-fire-station" },
    { name: "Leyburn Road", slug: "leyburn-road" },
    { name: "Osler Street", slug: "osler-street" },
    { name: "Cope Street", slug: "cope-street" },
    { name: "Clement Street", slug: "clement-street" },
    { name: "Ruston Street", slug: "ruston-street" },
    { name: "Crescent Theatre", slug: "crescent-theatre" },
    { name: "King Edwards Road", slug: "king-edwards-road" },
    { name: "Spring Hill Island", slug: "spring-hill-island" }
];
document.addEventListener("DOMContentLoaded", () => {
    renderTimetable(busStops);
    setupTableSearch();
});
function renderTimetable(stopsList) {
    const tableBody = document.querySelector('.timetable tbody');
    if (!tableBody) return;
    tableBody.innerHTML = '';
    stopsList.forEach(stop => {
        const row = document.createElement('tr');
        const nameCell = document.createElement('td');
        nameCell.textContent = stop.name;
        const actionCell = document.createElement('td');
        const link = document.createElement('a');
        link.href = `${stop.slug}.html`;
        link.className = 'btn-stop';
        link.textContent = 'View Timetable';
        actionCell.appendChild(link);
        row.appendChild(nameCell);
        row.appendChild(actionCell);
        tableBody.appendChild(row);
    });
}
