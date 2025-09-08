let revelButton = document.querySelector(".reveal");
let revealIcon = document.querySelector(".reveal-icon");
let hamburgerButton = document.querySelector(".hamburger");

let listsContainer = document.querySelector(".lists-container");

let sidebar = document.querySelector(".sidebar");


 console.log("Sidebar:", sidebar);
 console.log("Hamburger button:", hamburgerButton);

revelButton.addEventListener("click", (event) => {
    event.preventDefault();

    listsContainer.classList.toggle("hidden");
    revealIcon.classList.toggle("arrow-up");

});


hamburgerButton.addEventListener("click" , (event) => {
    event.preventDefault();

    sidebar.classList.toggle("hide");
    
    console.log("Classes de la sidebar:", sidebar.classList);
    console.log("Style display:", window.getComputedStyle(sidebar).display);
} ) ;
