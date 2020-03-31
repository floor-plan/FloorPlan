console.log("helloworld");

updateButton = document.getElementById('update-button')

checkboxes = document.querySelectorAll('.checkbox')

function editThisTask(id) {
    console.log("Where does this show up?")
    console.log(id)
    return fetch(`/complete_task/${id}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    })
        .then(response => response.json())
}


for (let checkbox of checkboxes) {
    checkbox.addEventListener('change', function (event) {
        event.preventDefault()
        console.log("How many times does this happen?")
        editThisTask(checkbox.id)
        checkbox.classList.add("strikethrough")
    })
}

// `/complete_task/${id}`

// .then(json => {
//     if (json.status === 'ok') {
//         document.getElementById(id).classList.add(".strikethrough")
//     }
// }



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