var navbar = document.getElementsByTagName("nav")[0];
var dropdown_container = document.getElementsByClassName("dropdownicon-container")[0];

function mouseLeft() {
    console.log("mouse left")
}

function dropdownEndEvent() {
    console.log("mouse left")
    dropdown_container.removeEventListener("animationend", dropdownEndEvent);
    dropdown_container.removeEventListener('mouseleave', dropupEndEvent)

    navbar.addEventListener('mouseleave', toggleNavbar)

    navbar.classList.remove("drop-animation");
    dropdown_container.classList.remove("drop-animation");
}

function dropupEndEvent() {
    dropdown_container.removeEventListener("animationend", dropupEndEvent);

    navbar.classList.remove("dropup-animation");
    dropdown_container.classList.remove("dropup-animation");
}

function toggleNavbar() {
    navbar.removeEventListener('mouseleave', toggleNavbar)
    if (!dropdown_container.classList.contains("dropped")) {
        console.log("go down")
        // go down
        dropdown_container.classList.add("dropped");
        navbar.classList.add("dropped")

        dropdown_container.classList.remove("dropdownicon-hoverdrop");  // no more hover feedback

        // start drop animation
        navbar.classList.add("drop-animation");
        dropdown_container.classList.add("drop-animation");
        dropdown_container.addEventListener('animationend', dropdownEndEvent)
    }
    else if (dropdown_container.classList.contains("dropped")) {
        navbar.classList.remove("dropped");
        dropdown_container.classList.remove("dropped");

        dropdown_container.classList.add("dropdownicon-hoverdrop");  // avtivate hover feedback

        navbar.classList.add("dropup-animation");
        dropdown_container.classList.add("dropup-animation");
        dropdown_container.addEventListener('animationend', dropupEndEvent)
    }
}

var body = document.getElementsByTagName("body")[0]
var flash_container = document.getElementsByClassName("flash")[0]
var flash_exists = flash_container.childNodes

if (flash_exists.length != 1) {
    body.style.marginTop = "90px";
}
