const endpoint = "https://api.djdisaster.uk";
const dateInput = document.getElementById("date");
const errorBox = document.getElementById("errorBox");
const form = document.getElementById("myForm");
const ticketsBody = document.getElementById("ticketsBody");

dateInput.min = new Date().toISOString().split("T")[0];
form.style.display = "none";

function checkIfSignedIn() {
    fetch(endpoint + "/isAuthRoute", {
        credentials: "include"
    })
        .then(function (response) {
            return response.json();
        })
        .then(function (json) {
            if (json.result != "auth") {
                form.style.display = "none";
                document.getElementById("h3title").innerText = "You must be logged in to book tickets!";
            } else {
                form.style.display = "";
                document.getElementById("h3title").innerText = "Book Tickets!";
                loadTickets();
            }
        })
        .catch(function (err) {
            console.error(err);
            errorBox.innerText = "Request failed";
        });
}

function bookTicket(event) {
    event.preventDefault();

    const date = document.getElementById("date").value;
    const startLocation = document.getElementById("start_location").value;
    const endLocation = document.getElementById("end_location").value;

    if (date == "" || startLocation == "" || endLocation == "") {
        errorBox.innerText = "Please fill in all required fields";
        return;
    }

    if (startLocation == endLocation) {
        errorBox.innerText = "Start and end location cannot be the same";
        return;
    }

    fetch(endpoint + "/bookTicket", {
        method: "POST",
        credentials: "include",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            date: date,
            startLocation: startLocation,
            endLocation: endLocation
        })
    })
        .then(function (response) {
            return response.json();
        })
        .then(function (json) {
            if (json.result == "success") {
                errorBox.innerText = "Ticket booked";
                form.reset();
                dateInput.min = new Date().toISOString().split("T")[0];
                loadTickets();
            } else {
                errorBox.innerText = json.message || "Could not book ticket";
            }
        })
        .catch(function (err) {
            console.error(err);
            errorBox.innerText = "Request failed";
        });
}

function loadTickets() {
    fetch(endpoint + "/tickets", {
        credentials: "include"
    })
        .then(function (response) {
            return response.json();
        })
        .then(function (json) {
            ticketsBody.innerHTML = "";

            if (json.result != "success") {
                return;
            }

            json.tickets.forEach(function (ticket) {
                const row = document.createElement("tr");

                const dateCell = document.createElement("td");
                dateCell.innerText = ticket.date;

                const startCell = document.createElement("td");
                startCell.innerText = ticket.startLocation;

                const endCell = document.createElement("td");
                endCell.innerText = ticket.endLocation;

                row.appendChild(dateCell);
                row.appendChild(startCell);
                row.appendChild(endCell);

                ticketsBody.appendChild(row);
            });
        })
        .catch(function (err) {
            console.error(err);
            errorBox.innerText = "Could not load tickets";
        });
}

form.addEventListener("submit", bookTicket);
checkIfSignedIn();
