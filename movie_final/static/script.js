function getCSRFToken() {
    return document.cookie.split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
}

fetch('/your-api-endpoint/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCSRFToken()  // Include CSRF token
    },
    body: JSON.stringify({ key: 'value' })
});


function searchMovie() {
    let input = document.getElementById("searchInput").value.toLowerCase();
    let movies = document.querySelectorAll(".movie-card");

    movies.forEach(movie => {
        let title = movie.querySelector("h3").innerText.toLowerCase();
        if (title.includes(input)) {
            movie.style.display = "block";
        } else {
            movie.style.display = "none";
        }
    });
}
document.getElementById("registerForm")?.addEventListener("submit", function(event) {
    event.preventDefault();

    let username = document.getElementById("username").value.trim();
    let email = document.getElementById("registerEmail").value.trim();
    let password = document.getElementById("registerPassword").value;
    let confirmPassword = document.getElementById("confirmPassword").value;

    if (password !== confirmPassword) {
        alert("Passwords do not match!");
        return;
    }

    alert("Registration successful! Now login.");
    window.location.href = "login.html";
});

document.getElementById("loginForm")?.addEventListener("submit", function(event) {
    event.preventDefault();

    let email = document.getElementById("email").value.trim();
    let password = document.getElementById("password").value;

    if (email === "test@example.com" && password === "password123") {
        alert("Login successful!");
        window.location.href = "index.html";
    } else {
        alert("Invalid email or password.");
    }
});
document.getElementById("reviewForm")?.addEventListener("submit", function(event) {
    event.preventDefault();

    let movieTitle = document.getElementById("movieTitle").value.trim();
    let genre = document.getElementById("genre").value;
    let rating = document.getElementById("rating").value;
    let reviewText = document.getElementById("reviewText").value.trim();

    if (movieTitle === "" || reviewText === "") {
        alert("Please fill in all fields.");
        return;
    }

    let reviewCard = document.createElement("div");
    reviewCard.classList.add("review-card");
    reviewCard.setAttribute("data-genre", genre);
    reviewCard.innerHTML = `
        <h3>${movieTitle}</h3>
        <p><strong>Genre:</strong> ${genre}</p>
        <p>⭐`.repeat(rating) + `</p>
        <p>${reviewText}</p>
    `;

    document.getElementById("reviewsContainer").appendChild(reviewCard);
    document.getElementById("reviewForm").reset();
});

document.getElementById("filterGenre")?.addEventListener("change", function() {
    let selectedGenre = this.value;
    let reviews = document.querySelectorAll(".review-card");

    reviews.forEach(review => {
        let genre = review.getAttribute("data-genre");
        review.style.display = (selectedGenre === "All" || genre === selectedGenre) ? "block" : "none";
    });
}); 