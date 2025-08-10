document.addEventListener("DOMContentLoaded", () => {
    const container = document.getElementById("liste-container");

    function loadListes() {
        fetch('/api/liste')
            .then(res => res.json())
            .then(data => {
                container.innerHTML = ""; //vider la liste
                data.listes.forEach(liste => {
                    const li = document.createElement("li");
                    li.innerHTML = `
                        ${liste.nom}
                        <button onclick="modifier(${liste.id}) "> Modifier </button>
                        <button onclick="suprimer(${liste.id})"> Supprimer</button>
                    `;
                    container.appendChild(li);
                });
            });
    }


    createBtn.addEventListener("click", () => {
        const nom = prompt ("Nom de la nouvelle liste :");
        if (nom) {
            fetch('/api/liste', {
                method: "post",
                headers: {
                    "content-Type": "application/json"
                },
                body: JSON.stringify({ nom })
            }).then(() => loadListes());
        }
    });

    window.modifier = function(id) {
        const nom = prompt("Nouveau :");
        if (nom) {
            fetch('/api/liste/${id}', {
                method:"PUT",
                headers: {
                    "content-Type": "application/json"
                },
                body: JSON.stringify({nom})
            }).then (() => loadListes());
        }
    };

    window.supprimer = function(id) {
        if (confirm("supprimer cette liste ?")){
            fetch('/api/liste/${id}',{
                method:"DELETE"
            }).then(() => loadListes());
        }
    };

        loadListes();
})    