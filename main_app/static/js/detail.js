const progressBar = document.querySelector('.progress-bar')
const logWeekBtn = document.querySelector('.log-week')
const progressBarEl = document.querySelector('.progress-bar')
const addWorkoutDateBtn = document.querySelector('.btn.submit')
const didWorkoutInpt = document.querySelector('#id_did_workout')
const progressMsgEl = document.querySelector('.progress-msg')
console.log(logWeekBtn);
let progressNumber = 0
let weeksLeft = 4

logWeekBtn.addEventListener("click", (evt) => {
    evt.preventDefault();
    if (progressNumber < 100) {        
        if (didWorkoutInpt.value === "Y") {        
            progressNumber+= 25;
            progressBar.setAttribute("style", `width: ${progressNumber}%`)
            progressNumber === 100 ? progressMsgEl.innerText = "It's over 9000! You've done all your workouts for the month and are one step closer to Super Saiyan status" : '';
            progressBarEl.setAttribute("style", `width: ${progressNumber}%`)
            if (progressNumber === 100) {
                progressMsgEl.innerText = "It's over 9000! You've done all your workouts for the month and are one step closer to Super Saiyan status";
                progressBarEl.classList.add("bg-warning");
            }
        }
    }
})
