let headTarget;
const classToAddContent = ["d-flex", "justify-content-between", "align-items-start"]
const classToAddImage = ["col-6", "stickied"]
const classToAddText = ["col-6", "mt-5"]

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

function handleIntersect(entries, observer) {
    entries.forEach(entry => {
        if (entry.isIntersecting){
            removeClasses(document.querySelector('#content'), classToAddContent)
            removeClasses(document.querySelector('#text_col'), classToAddText)
            removeClasses(document.querySelector('#image_col'), classToAddImage)
        } else {
            addClasses(document.querySelector('#content'), classToAddContent)
            addClasses(document.querySelector('#text_col'), classToAddText)
            addClasses(document.querySelector('#image_col'), classToAddImage)
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