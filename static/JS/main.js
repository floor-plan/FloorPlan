console.log("helloworld");

function showUpdateButton() {
    updateButton = document.getElementById("update-button");
    updateButton.classList.remove("hidden");
    updateButton.classList.add("visible");
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
        editThisTask(checkbox.id);
        // checkbox.classList.add("strikethrough");
        showUpdateButton();
    });
}