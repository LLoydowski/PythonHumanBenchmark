const scorePar = document.getElementById("score")
const wordPar = document.getElementById("verbalWord")

const newButton = document.querySelector(".gameVerbalNewWordButton")
const seenButton = document.querySelector(".gameVerbalSeenWordButton")
const newGameButton = document.querySelector(".gameVerbalNewGameButton")

const life1 = document.getElementById("lifeOne")
const life2 = document.getElementById("lifeTwo")
const life3 = document.getElementById("lifeThree")


async function sendRequest(type){
    let gameInfo = await Promise.resolve(fetch(window.location.href, {
        method: "post",
        mode: "cors",
        headers: new Headers({
            "Content-Type": "application/json"
        }),
        body: JSON.stringify({
            "chooice": type
        })
    })
    .then(res => res.json()))

    scorePar.textContent = gameInfo["score"]
    wordPar.textContent = gameInfo["randWord"]

    setLivesColor(gameInfo["lives"])

    newButton.classList.remove("hidden")
    seenButton.classList.remove("hidden")
    newGameButton.classList.add("hidden")
    
    if(gameInfo["status"] != ""){
        setLivesColor(0)
        alert(gameInfo["status"])
        newButton.classList.add("hidden")
        seenButton.classList.add("hidden")
        newGameButton.classList.remove("hidden")
        wordPar.textContent = ''
    }
}


function setLivesColor(lives){
    switch(lives){
        case 0:
            life1.classList.add("disabledHeart")
            life2.classList.add("disabledHeart")
            life3.classList.add("disabledHeart")
            break
        case 1:
            life1.classList.remove("disabledHeart")
            life2.classList.add("disabledHeart")
            life3.classList.add("disabledHeart")
            break
        case 2:
            life1.classList.remove("disabledHeart")
            life2.classList.remove("disabledHeart")
            life3.classList.add("disabledHeart")
            break
        case 3:
            life1.classList.remove("disabledHeart")
            life2.classList.remove("disabledHeart")
            life3.classList.remove("disabledHeart")
            break
    }
    console.log(lives)
}
