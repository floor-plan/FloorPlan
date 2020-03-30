console.log("helloworld");

function taskComplete() {

    var taskCheckbox = document.getElementById("taskCheckbox");

    var taskText = document.querySelector("#task-text");

    if (taskCheckbox.checked == true) {
        taskText.classList.add('completed-task');
    } else {
        taskText.style.display = "none";
    }
}

// function check(checked = true) {
//     const cbs = document.querySelectorAll('input[name="color"]');
//     cbs.forEach((cb) => {
//         cb.checked = checked;
//     });
// }

// const btn = document.querySelector('#btn');
// btn.onclick = checkAll;

// function checkAll() {
//     check();
//     // reassign click event handler
//     this.onclick = uncheckAll;
// }

// function uncheckAll() {
//     check(false);
//     // reassign click event handler
//     this.onclick = checkAll;
// }