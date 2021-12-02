const progressBar = document.querySelector('.progress-bar')
const addWorkoutDateBtn = document.querySelector('.btn.submit')
console.log(progressBar);
console.log(addWorkoutDateBtn);
console.log('hello');


addWorkoutDateBtn.addEventListener("click", (evt) => {
    evt.preventDefault();
    progressBar.setAttribute("style", "width: 5%")
})