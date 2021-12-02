const progressBar = document.querySelector('.progress-bar')
const addWorkoutDateBtn = document.querySelector('.btn.submit')
console.log(progressBar);
console.log(addWorkoutDateBtn);
console.log('hello');

let progressNumber = 0

addWorkoutDateBtn.addEventListener("click", (evt) => {
    evt.preventDefault();
    progressNumber++;
    console.log(progressNumber);
    progressBar.setAttribute("style", "width: 5%")
})