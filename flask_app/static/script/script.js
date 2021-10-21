// This file adds classes to the html when the use scrolls away from the top of the page. The classes cause the image to stick to the left and stay on screen, while the text will fit on the right side. (The classes will not do anything if the screen width is < 1200px)

let headTarget;
const classToAddContent = ["flex-on", "justify-content-between", "align-items-start"]
const classToAddImage = ["shift-left-col"]
const classToAddText = ["shift-right-col"]

// add an event to fire when the page loads. Sets head target to our watcher div and runs our function.
window.addEventListener("load", (event) => {
    headTarget = document.querySelector("#target");
    createObserver();
}, false);

// Create an intersection observer that will fire handleIntersect method
function createObserver() {
    let observer;

    let options = {
        root: null,
        rootMargin: "0px",
        threshold: 0,
    };

    observer = new IntersectionObserver(handleIntersect, options);
    observer.observe(headTarget);
}

// removes/adds classes based on whether the target div is visible on the screen
function handleIntersect(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting){
            removeClasses(document.querySelector('#content'), classToAddContent)
            removeClasses(document.querySelector('#image_col'), classToAddImage)
            removeClasses(document.querySelector('#text_col'), classToAddText)
        } else {
            addClasses(document.querySelector('#content'), classToAddContent)
            addClasses(document.querySelector('#image_col'), classToAddImage)
            addClasses(document.querySelector('#text_col'), classToAddText)
        }
    });
}

// Adds classes to target element
function addClasses(target, classes){
    classes.forEach(classToAdd => {
        target.classList.add(classToAdd)
    });
}

// Removes classes from target element
function removeClasses(target, classes){
    classes.forEach(classToAdd => {
        target.classList.remove(classToAdd)
    });
}