/* ########
Tout ceci ne marche pas forcement. j'ai juste mieux organisé ke cide
*/// ########


let container = document.querySelector(".liste-container");
let createBtn = document.getElementById(".add-btn")

function loadListes() {
    fetch('api/liste')
    .then(response => response.json())
    .then(data => {
        container.innerHTML = "";

        data.listes.forEach(l => {
            const liste = document.createElement("div");
            liste.classList.add("liste");
            
            texte_liste = document.createElement("span");
            texte_liste.innerText = l.nom

            boutton_modifier = document.createElement("span");
            boutton_modifier.classList.add("bouton-modifier");

            boutton_supprimer = document.createElement("span");
            boutton_supprimer.classList.add("bouton-supprimer");

            liste.appendChild(boutton_modifier)
            liste.appendChild(boutton_supprimer)

            container.appendChild(liste);
        });
    })
    .catch(error => {
        console.log(error);
        // alert(error);
    });
}
document.addEventListener("DOMContentLoaded", loadListes);


function createTask() {
    const nom = prompt ("Nom de la nouvelle liste :");
    if (nom) {
        fetch('/api/liste', {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ nom })
        }).then(() => loadListes());
    }
}

function updateListe(id) {
    const nom = prompt("Nouveau :");
    if (nom) {
        fetch('/api/liste/${id}', {
            method:"PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({nom})
        }).then (() => loadListes());
    }
};

function deleteListe(id) {
    if (confirm("supprimer cette liste ?")){
        fetch('/api/liste/${id}',{
            method:"DELETE"
        }).then(() => loadListes());
    }
};


