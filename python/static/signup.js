async function sleep(ms){
    return new Promise(resolve => setTimeout(resolve, ms));
}

function arePasswordsSame(){
    let pass1 = document.getElementById("password1").value
    let pass2 = document.getElementById("password2").value

    if(pass1 == pass2){
        return true 
    }

    return false
}

function arePassesBlank(){
    let pass = document.getElementById("password1").value

    if(pass.trim() == ""){
        return true
    }

    return false
}

function checkIsPasswordCorrect(){
    let pass = document.getElementById("password1").value

    let length = pass.length

    let numbersCounter = 0
    let specialSignCounter = 0
    let upperCaseCounter = 0

    let numbers = "123456789"
    let letters = "qwertyuiopasdfghjklzxcvbnm"
    let upperLetters = "QWERTYUIOPASDFGHJKLZXCVBNM"
    let specialCharacters = "!@#$%^&*(()_+"

    for(let i = 0; i < length; i++){
        let char = pass[i]

        let isCharValid = false

        if(letters.includes(char)){
            isCharValid = true
        }

        if(numbers.includes(char)){
            isCharValid = true
            numbersCounter++
        }

        if(upperLetters.includes(char)){
            upperCaseCounter++
            isCharValid = false
        }

        if(specialCharacters.includes(char)){
            specialSignCounter++
            isCharValid = false
        }

        if(!isCharValid){
            alert("You cant use character " + char + " in your password")
            return false
        }

    }

    if(length < 8){
        alert("Your password neets to be at least 8 characters long")
        return false
    }

    if(numbersCounter < 3){
        alert("Your password needs to have at least 3 numbers")
        return false
    }

    if(upperCaseCounter == 0){
        alert("Your password needs to have at least 1 upper case letter")
        return false
    }


    if(specialSignCounter == 0){
        alert("Your password needs to have at least 1 special sign")
        return false
    }


    return true
}

const form = document.querySelector("form")

form.addEventListener("submit", async (event) => {
    event.preventDefault()

    const username = document.getElementById("username").value.trim()
    const password = document.getElementById("password1").value.trim()

    if(!arePasswordsSame()){
        alert("Passwords need to be the same")
        return
    }

    if(arePassesBlank()){
        alert("Password can't be blank")
        return
    }

    let data = {
        "name": username,
        "password": password
    }

    const responseParagraph = document.getElementById("response")

    let status = await Promise.resolve(fetch(window.location.href, {
        method: "post",
        body: JSON.stringify(data),
        mode: "cors",
        headers: new Headers({
            "Content-Type": "application/json"
        })
    })
    .then(response => response.json()))

    status = status["status"]

    responseParagraph.textContent = status

    const date = new Date();
    date.setTime(date.getTime() + 24*60*60*1000)


    document.cookie = `username=${data["name"]}; expires=${date.toUTCString()}`
   
})      