var submit = document.getElementById('submitButton')
var endpoint = "https://api.djdisaster.uk"
var errorBox = document.getElementById('errorBox')

submit.addEventListener("click", function (e) {
    e.preventDefault()

    var email = document.getElementById('name').value
    var password = document.getElementById('password').value

    var toCall = endpoint + "/login/" + encodeURIComponent(email) + "/" + encodeURIComponent(password)

    fetch(toCall, {
        credentials: "include"
    })
        .then(function (response) {
            return response.json()
        })
        .then(function (json) {
            console.log(json)
            errorBox.innerText = json.result
            if (json.result == "authenticated") {
                location.reload()
            }
        })
        .catch(function (err) {
            console.error(err)
            errorBox.innerText = "Request failed"
        })
})

function checkIfSignedIn() {
    var toCall = endpoint + "/isAuthRoute"

    fetch(toCall, {
        credentials: "include"
    })
        .then(function (response) {
            return response.json()
        })
        .then(function (json) {

            if (json.result == 'auth') {
                // User is authorised.
                document.getElementById('myForm').style.display = 'none'
                document.getElementById('myForm').style.display = 'none'
                document.getElementById('h3title').innerHTML = "You are already logged into your account! <a href='../tickets.html'>View tickets</a>"
            }

        })
        .catch(function (err) {
            console.error(err)
            errorBox.innerText = "Request failed"
        })
}

checkIfSignedIn()
