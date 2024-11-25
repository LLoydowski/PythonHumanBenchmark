const loggedIn = document.querySelector(".optionsLogged")
const loggedOut = document.querySelector(".optionsNotLogged")

function checkIsLoggedIn(){
    let cookies = decodeURIComponent(document.cookie)
    let username = cookies.split(';')[0]

    if(username){
        loggedIn.classList.remove("hidden")
        loggedOut.classList.add("hidden")

        document.getElementById("nick").textContent = username.substring(9, username.length )
    }
}

checkIsLoggedIn()