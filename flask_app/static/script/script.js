let headTarget;
const classToAddContent = ["flex-on", "justify-content-between", "align-items-start"]
const classToAddImage = ["shift-left-col"]
const classToAddText = ["shift-right-col"]

window.addEventListener("load", (event) => {
    headTarget = document.querySelector("#target");
    createObserver();
}, false);

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

function addClasses(target, classes){
    classes.forEach(classToAdd => {
        target.classList.add(classToAdd)
    });
}

function removeClasses(target, classes){
    classes.forEach(classToAdd => {
        target.classList.remove(classToAdd)
    });
}