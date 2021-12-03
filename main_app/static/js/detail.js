const progressBarEl = document.querySelector('.progress-bar')
const addWorkoutDateBtn = document.querySelector('.btn.submit')
const didWorkoutInpt = document.querySelector('#id_did_workout')
const progressMsgEl = document.querySelector('.progress-msg')

console.log(progressMsgEl);

let progressNumber = 0

addWorkoutDateBtn.addEventListener("click", (evt) => {
    evt.preventDefault();
    if (progressNumber < 100) {        
        if (didWorkoutInpt.value === "Y") {        
            progressNumber+= 25;
            progressBarEl.setAttribute("style", `width: ${progressNumber}%`)
            if (progressNumber === 100) {
                progressMsgEl.innerText = "It's over 9000! You've done all your workouts for the month and are one step closer to Super Saiyan status";
                progressBarEl.classList.add("bg-warning");
            }
        }
    }
})