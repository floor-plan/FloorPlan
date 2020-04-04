console.log("helloworld");

updateButton = document.getElementById("update-button");

function showUpdateButton() {
    if (updatButton.classList.contains('hidden')) {
        updateButton.classList.remove('hidden');
        updateButton.classList.add('visible')

        update
        updateButton
    }

    checkboxes = document.querySelectorAll(".checkbox");

    function editThisTask(id) {
        console.log("Where does this show up?");
        console.log(id);
        return fetch(`/complete_task/${id}/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                Accept: "application/json"
            }
        }).then(response => response.json());
    }

    for (let checkbox of checkboxes) {
        checkbox.addEventListener("change", function(event) {
            event.preventDefault();
            console.log("How many times does this happen?");
            editThisTask(checkbox.id);
            checkbox.classList.add("strikethrough");
        });
    }