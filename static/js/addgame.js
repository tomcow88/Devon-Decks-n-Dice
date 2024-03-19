document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('form[id^="game-form-"]').forEach(form => {
        form.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent the default form submission action

            const bgg_id = this.id.replace('game-form-', ''); // Extract the bgg_id from the form's id

            addGameToDatabase(bgg_id); // Call the function to handle the form submission
        });
    });
});

function addGameToDatabase(bgg_id) {
    const form = document.getElementById(`game-form-${bgg_id}`);
    const formData = new FormData(form);

    // Log each item in the FormData object
    for (let [key, value] of formData.entries()) {
        console.log(`${key}: ${value}`);
    }

    // Make the POST request to the server
    fetch('/library/add-game-to-database/', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Game added to the library successfully.");
        } else {
            alert("Failed to add the game. Please try again.");
        }
    })
    .catch(error => console.error('Error:', error));
}