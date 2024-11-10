function arePasswordsSame(){
    let pass1 = document.getElementById("password1").value
    let pass2 = document.getElementById("password2").value

    if(pass1 == pass2){
        return true 
    }

    return false
}

function areNotBlank(){
    let pass = document.getElementById("password1").value

    if(pass.trim() == ""){
        return false
    }

    return true
}

const form = document.querySelector("form")

form.addEventListener("submit", (event) => {
    event.preventDefault()
    arePassesSame = arePasswordsSame()

    const username = document.getElementById("username").value.trim()
    const password = document.getElementById("password1").value.trim()

    if(arePassesSame && areNotBlank()){
        var xhr = new XMLHttpRequest();
        xhr.open("POST", window.location.href, true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(JSON.stringify({
            "name": username,
            "password": password
        }));
        console.log(arePassesSame)   
    }

})