const reactionButton = document.querySelector(".reactionGameButton")
const scorePar = document.getElementById("score")

let sStartTime = 0
let sEndTime = 0

let cStartTime = 0
let cEndTime = 0

async function sendRequest(type){

    document.getElementById("game").style.backgroundColor = "red";

    let data = {}


    if(type == "newGame"){
        data["action"] = "newGame" 
    }else{
        data["action"] = "clicked"
        cEndTime = new Date().getTime()
        document.getElementById("game").style.backgroundColor = "var(--lightBlue)";
        reactionButton.setAttribute("onclick", 'sendRequest("newGame")')
        reactionButton.textContent = "Start"
    }
    
    let response = await Promise.resolve(fetch(window.location.href, {
        method: "post",
        body: JSON.stringify(data),
        mode: "cors",
        headers: new Headers({
            "Content-Type": "application/json"
        })
    })
    .then(res => res.json()))
    
    if(response["sStartTime"]){
        sStartTime = Math.floor(response["sStartTime"] * 1000)
        cStartTime = new Date().getTime()
        // reactionButton.classList.remove("hidden")
        document.getElementById("game").style.backgroundColor = "rgb(41, 255, 84)";
        reactionButton.setAttribute("onclick", 'sendRequest("clicked")')
        reactionButton.textContent = "Click me!"
    }
    
    if(response["sEndTime"]){
        sEndTime = Math.floor(response["sEndTime"] * 1000)
    }

    if(response["sEndTime"]){
        let status = await Promise.resolve(fetch(window.location.href, {
            method: "post",
            body: JSON.stringify({
                "action": "validation",
                "sStartTime": sStartTime,
                "sEndTime": sEndTime,
                "cStartTime": cStartTime,
                "cEndTime": cEndTime
            }),
            mode: "cors",
            headers: new Headers({
                "Content-Type": "application/json"
            })
        }))
        .then(res => res.json())
        .then(json => json["status"])

        if(status == "You either have bad internet connection or you cheated. Therefore your score won't be saved. Sorry!"){
            alert(status)
        }

        scorePar.textContent = status + " ms"
    }
    
}

function logTimes(){
    console.log("-SERVER-")
    console.log("Start time: " + sStartTime)
    console.log("End time: " + sEndTime)
    console.log("Time Diff: " + (sEndTime - sStartTime))
    console.log("-CLIENT-")
    console.log("Start time: " + cStartTime)
    console.log("End time: " + cEndTime)
    console.log("Time Diff: " + (cEndTime - cStartTime))
    console.log("----------")
}

function reactionGameStart() {
    
}