let container = document.querySelector(".liste-container");
let listeInput = document.querySelector(".liste-input");
let addButton = document.querySelector(".bouton-ajouter");


/*
function updateListItem(id, texte_liste) {
    let nouveauNom = prompt("Nouveau nom :", texte_liste.innerText);
    if (!nouveauNom || !nouveauNom.trim()) return;

    fetch(`/api/liste/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nom: nouveauNom.trim() })
    })
    .then(r => r.json())
    .then(data => {
        if (data.success) {
            texte_liste.innerText = data.nom;
        } else {
            alert(data.message || "Erreur lors de la mise à jour");
        }
    })
    .catch(() => alert("Erreur réseau"));
}

function deleteListItem(id, item) {
    if (!confirm("Supprimer cette liste ?")) return;

    fetch(`/api/liste/${id}`, { method: "DELETE" })
    .then(r => r.json())
    .then(data => {
        if (data.success) {
            item.remove();
        } else {
            alert(data.message || "Erreur lors de la suppression");
        }
    })
    .catch(() => alert("Erreur réseau"));
}

function createListItem(id, name) {
    let item = document.createElement("div");
    item.classList.add("liste-item");
    item.id = id;

    let texte_liste = document.createElement("span");
    texte_liste.innerText = name;

    let bouton_modifier = document.createElement("button");
    bouton_modifier.classList.add("bouton-modifier");
    bouton_modifier.innerText = "Modifier";
    bouton_modifier.addEventListener("click", () => {
        updateListItem(id, texte_liste);
    });

    let bouton_supprimer = document.createElement("button");
    bouton_supprimer.classList.add("bouton-supprimer");
    bouton_supprimer.innerText = "Supprimer";
    bouton_supprimer.addEventListener("click", () => {
        deleteListItem(id, item);
    });

    item.appendChild(texte_liste);
    item.appendChild(bouton_modifier);
    item.appendChild(bouton_supprimer);

    return item;
}

function loadListes() {
    console.log("Loading lists");
    fetch("/api/liste")
    .then(r => r.json())
    .then(data => {
        container.innerHTML = "";
        data.listes.forEach(l => {
            console.log("Hello world");
            let liste = createListItem(l.id, l.nom);
            container.appendChild(liste);
        });
    })
    .catch(e => console.log(e));
}

addButton.addEventListener("click", ()=> {
    let name = listeInput.value.trim();
    if (!name) return;

    fetch("/api/liste", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nom: name })
    })
    .then(r => r.json())
    .then(data => {
        if (data.success) {
            listeInput.value = "";
            loadListes();
        } else {
            alert(data.message || "Erreur lors de la création");
        }
    })
    .catch(e => console.log(e));
});

document.addEventListener("DOMContentLoaded", loadListes); */

/****************************************************/

document.addEventListener("DOMContentLoaded", function(){
    loadLists();
}); 

async function loadLists(){

    try {
        const response = await fetch('api/liste');
        console.log("debut du chagement !!")
        const data = await response.json();

        console.log("Données reçues:", data);

        displayLists(data.listes);
        console.log(" c'est bon ");
    } catch (error) {
        console.log(" impossible de charger les listes");
    }
}

function displayLists(lists){
    const container = document.querySelector(".lists-container");
    
    if (lists.length === 0){
        container.innerHTML = '<div class="empty">Aucune liste disponible</div>'; 
        return;
    }

    container.innerHTML = '';

    lists.forEach(list =>{
        const listItem = document.createElement('div');
        listItem.className = "list-item" ;
        listItem.innerHTML =  `<input type="checkbox" id="list-${list.id}">
        <label>${list.nom}</label> `;

        container.appendChild(listItem);
    });
}