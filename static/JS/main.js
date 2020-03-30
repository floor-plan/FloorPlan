console.log("helloworld");

updateButton = document.getElementById('update-button')

const taskCheckbox = document.getElementById("checkbox");

updateButton.addEventListener("click", function(event) {
    updateTasks();
});

function updateTasks() {
    if (taskCheckbox.checked) {
        task.pk("{% url 'myapp:movieDataUpdate' pk=task.pk %}",


        }
    }

    checkboxes = document.querySelectorAll('taskCheckbox')


    function taskComplete() {

        var taskCheckbox = document.getElementById("taskCheckbox");

        var taskText = document.querySelector("#task-text");

        if (taskCheckbox.checked == true) {
            taskText.classList.add('completed-task');
        } else {
            taskText.style.display = "none";
        }
    }



    // $("#my_checkbox1").change(function() {
    //     if (this.checked) {
    //         $.post("{% url 'myapp:movieDataUpdate' pk=movie.pk %}", {},
    //             function(data, status) {
    //                 console.log("Data: " + data + "\nStatus: " + status);
    //             });
    //     }
    //     // If you want, make an
    //     // else
    // });