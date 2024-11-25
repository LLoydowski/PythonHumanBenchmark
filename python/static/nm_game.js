const randNumberPar = document.getElementById("randNumberPar")
const statusPar = document.getElementById("status")
const timerBar = document.querySelector(".bar")

document.querySelector("input").addEventListener("keypress", (e) => {
    if(e.key == "Enter"){
        guess()
    }
})

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function newGame(){
    gameInfo = await Promise.resolve(fetch(window.location.href, {
        method: "post",
        mode: "cors",
        body: JSON.stringify({"action": "newGame"}),
        headers: new Headers({
            "Content-Type": "application/json"
        })
    })
    .then(response => response.json()))

    statusPar.textContent = ""

    randNumberPar.textContent = gameInfo["randNumb"]
    randNumberPar.classList.remove("hidden")

    timerBar.style.animation = `bar ${gameInfo["sleepTime"]}s`

    await sleep(gameInfo["sleepTime"] * 1000)

    timerBar.style.animation = ''
    randNumberPar.classList.add("hidden")
}

async function guess(){
    const guessedNumber = Number(document.getElementById("guessInput").value)

    gameInfo = await Promise.resolve(fetch(window.location.href, {
        method: "post",
        mode: "cors",
        body: JSON.stringify({"action": "guess", "guess": guessedNumber}),
        headers: new Headers({
            "Content-Type": "application/json"
        })
    })
    .then(response => response.json()))

    if(gameInfo["status"] == "lost"){
        statusPar.textContent = "You have lost!"
        return
    }

    randNumberPar.textContent = gameInfo["randNumb"]
    randNumberPar.classList.remove("hidden")

    timerBar.style.animation = `bar ${gameInfo["sleepTime"]}s`

    await sleep(gameInfo["sleepTime"] * 1000)

    timerBar.style.animation = ''
    randNumberPar.classList.add("hidden")
}