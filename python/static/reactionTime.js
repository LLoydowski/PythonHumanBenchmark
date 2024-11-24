const reactionButton = document.getElementById("reactionButton")

document.querySelector("form").addEventListener("submit", (e) => {
    e.preventDefault()
})

let sStartTime = 0
let sEndTime = 0

let cStartTime = 0
let cEndTime = 0

async function sendRequest(type){

    let data = {}


    if(type == "newGame"){
        data["action"] = "newGame" 
        reactionButton.classList.add("hidden")
    }else{
        data["action"] = "clicked"
        cEndTime = new Date().getTime()
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
        reactionButton.classList.remove("hidden")
    }
    
    if(response["sEndTime"]){
        sEndTime = Math.floor(response["sEndTime"] * 1000)
    }

    if(response["sEndTime"]){
        logTimes()
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

        alert(status)

        reactionButton.classList.add("hidden")
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