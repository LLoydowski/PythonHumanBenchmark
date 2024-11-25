const randNumberPar = document.getElementById("randNumberPar")
const statusPar = document.getElementById("status")
const timerBar = document.querySelector(".timerBar")
const guessedNumberInput = document.getElementById("guessInput")
const scorePar = document.getElementById("score")

document.querySelector("input").addEventListener("keypress", (e) => {
    if(e.key == "Enter"){
        guess()
    }
})

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function newGame(){
    scorePar.textContent = 1

    gameInfo = await Promise.resolve(fetch(window.location.href, {
        method: "post",
        mode: "cors",
        body: JSON.stringify({"action": "newGame"}),
        headers: new Headers({
            "Content-Type": "application/json"
        })
    })
    .then(response => response.json()))

    guessedNumberInput.value = ''

    randNumberPar.textContent = gameInfo["randNumb"]
    randNumberPar.classList.remove("notDisplayed")
    guessedNumberInput.style.zIndex = "0"
    
    timerBar.style.animation = `bar ${gameInfo["sleepTime"]}s`
    
    await sleep(gameInfo["sleepTime"] * 1000)
    
    timerBar.style.animation = ''
    guessedNumberInput.style.zIndex = "10"
    randNumberPar.classList.add("notDisplayed")
}

async function guess(){
    
    gameInfo = await Promise.resolve(fetch(window.location.href, {
        method: "post",
        mode: "cors",
        body: JSON.stringify({"action": "guess", "guess": Number(guessedNumberInput.value)}),
        headers: new Headers({
            "Content-Type": "application/json"
        })
    })
    .then(response => response.json()))
    
    if(gameInfo["status"] == "lost"){
        alert(gameInfo["status"])
        return
    }
    guessedNumberInput.value = ''
    scorePar.textContent = gameInfo["score"]
    
    randNumberPar.textContent = gameInfo["randNumb"]
    randNumberPar.classList.remove("notDisplayed")
    guessedNumberInput.style.zIndex = "0"
    
    timerBar.style.animation = `bar ${gameInfo["sleepTime"]}s`
    
    await sleep(gameInfo["sleepTime"] * 1000)
    
    timerBar.style.animation = ''
    guessedNumberInput.style.zIndex = "10"
    randNumberPar.classList.add("notDisplayed")
    
}