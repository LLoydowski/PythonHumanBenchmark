const form = document.querySelector("form")

form.addEventListener("submit", async (event) => {
    event.preventDefault()

    const username = document.getElementById("username").value.trim()
    const password = document.getElementById("password").value.trim()

    let data = {
        "name": username,
        "password": password
    }

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

    const statusParagraph = document.getElementById('status')

    if(status != ""){
        alert(status)
    }

    const date = new Date();
    date.setTime(date.getTime() + 24*60*60*1000)

    if(status == ""){
        document.cookie = `username=${data["name"]}; expires=${date.toUTCString()}`
    }
})