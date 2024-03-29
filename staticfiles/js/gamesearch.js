const searchForm = document.getElementById('search-form');
const loadingMessage = document.getElementById('loading-message');
const gameSearchResults = document.getElementsByClassName('game-search-results');

searchForm.addEventListener('submit', function() {
    loadingMessage.classList.remove('d-none');
    Array.from(gameSearchResults).forEach((element) => {
        element.classList.add('d-none');
    });
});

window.setInterval(() => {
    let wait = document.getElementById("wait");
    if (wait.innerHTML.length > 2) 
        wait.innerHTML = "";
    else 
        wait.innerHTML += ".";
}, 500);