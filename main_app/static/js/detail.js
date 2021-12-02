const progressBar = document.querySelector('.progress-bar')
const addWorkoutDateBtn = document.querySelector('.btn.submit')
const didWorkoutInpt = document.querySelector('#id_did_workout')

let progressNumber = 0

addWorkoutDateBtn.addEventListener("click", (evt) => {
    evt.preventDefault();
    if (didWorkoutInpt.value === "Y") {        
        progressNumber+= 25;
        progressBar.setAttribute("style", `width: ${progressNumber}%`)
    }
})