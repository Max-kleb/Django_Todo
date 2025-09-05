let revelButton = document.querySelector(".reveal");
let revealIcon = document.querySelector(".reveal-icon");

let listsContainer = document.querySelector(".lists-container");


revelButton.addEventListener("click", (event) => {
    event.preventDefault();

    listsContainer.classList.toggle("hidden");
    revealIcon.classList.toggle("arrow-up");
});