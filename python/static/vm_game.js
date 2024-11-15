const form = document.querySelector("form")

let choose = undefined 

async function sleep(ms){
    return new Promise(resolve => setTimeout(resolve, ms));
}

form.addEventListener("submit", (e) => {
    e.preventDefault()
    var xhr = new XMLHttpRequest();
    xhr.open("POST", window.location.href, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        "choose": choose
    }));
    sleep(20)
    .then(() => window.location.reload())
    
})

function setChoose(value){
    choose = value
}