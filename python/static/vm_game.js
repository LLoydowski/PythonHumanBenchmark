const form = document.querySelector("form")

let choose = undefined 

form.addEventListener("submit", (e) => {
    e.preventDefault()
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:85/verbal", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        "choose": choose
    }));
    window.location.reload()
})

function setChoose(value){
    choose = value
}