// function addGameToDatabase(bgg_id) {
//     const form = document.getElementById(`game-form-${bgg_id}`);
//     const formData = new FormData(form);

//     fetch('/library/add-game-to-database/', {
//         method: 'POST',
//         body: formData,
//     })
//     .then(response => response.json())
//     .then(data => {
//         if (data.success) {
//             alert("Game added to the library successfully.");
//         } else {
//             alert("Failed to add the game. Please try again.");
//         }
//     })
//     .catch(error => console.error('Error:', error));
// }
