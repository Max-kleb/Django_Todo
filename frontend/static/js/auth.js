let form = document.querySelector(".form");
let inputs = document.querySelectorAll(".form_input");


let error_frame = document.querySelector(".error_frame");
function display_result(message, positive) {
    error_frame.innerText =message;
    error_frame.classList.add("visible");

    if(positive) error_frame.classList.add("positive");
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
           display_result (data.message, true);
           console.log(data.token);

            setTimeout( () => {
            window.location.replace("/");
           }, 1000);
        }
        else {
            display_result(data.message, false);
            inputs.forEach(input => input.value="");
        }
    })
    .catch( e => {
        inputs.forEach(input => input.value="");
        display_result("Une erreur est survenue. Veuillez reessayer", false);
    });
}

form.addEventListener("submit", event => {
    event.preventDefault();

    error_frame.classList.remove("visible");

    let formData = new FormData(event.target);
    let datas = {};

    formData.forEach((key, value) => {
        datas[value]=key;
    });

    console.log(datas);
    authenticate(form.action, datas);
});