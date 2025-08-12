let form = document.querySelector(".form");
let information = document.querySelectorAll(".information");

function display_result(message, positive) {
    information.innertext =message;
    information.style.display = "block";

    if(positive) information.classList.toggle("positive");
}


function authenticate(path, datas) {
    fetch(path,
        {
            headers:{"content-Type": 'application/json'},
            method: "POST",
            body: JSON.stringify(datas)
        }
    ).then(response => response.json()
    ).then( (data) => {
        if(data.success){
           display_result (data.message, true) ;

           setTimeout( () => {
            window.location.replace("/");
           }, 1000);
        }
        else display_result(data.message, false);
    })
    .catch( e => {
        display_result("An error occured. Try again later", false);
    });
}

form.addEventListener("submit", event => {
    event.preventDefault();

    information.style.dasplay = "none";

    let formData = new FormData(event.target);
    let datas = {};

    formData.forEach((KeyboardEvent, value) => {
        data[value]=key;
    });

    console.log(datas);
    authenticate(form.action, datas);
});