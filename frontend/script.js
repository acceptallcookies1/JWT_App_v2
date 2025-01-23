const loginForm = document.getElementById("loginForm");
const message = document.getElementById("message");

// Handle login form submission
loginForm.addEventListener("submit", async (event) => {
  event.preventDefault(); // Prevent form from reloading the page

  const username = event.target.username.value; // Get username from form
  const password = event.target.password.value; // Get password from form

  // Send a POST request to the /login endpoint
  const response = await fetch("/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  });

  const data = await response.json();

  if (response.ok) {
    // Save the token in localStorage
    localStorage.setItem("token", data.token);

    // Display success message
    message.textContent = "Login successful! Token stored securely.";
    message.style.color = "green";
  } else {
    // Display error message
    message.textContent = `Error: ${data.error}`;
    message.style.color = "red";
  }
});

// Handle access to the protected route
document.getElementById("protectedRoute").addEventListener("click", async () => {
  const token = localStorage.getItem("token"); // Retrieve the token from localStorage

  if (!token) {
    alert("You must log in first!"); // Warn if the user isn't logged in
    return;
  }

  // Send a GET request to the /post-auth endpoint with the token
  const response = await fetch("/post-auth", {
    method: "GET",
    headers: { Authorization: `Bearer ${token}` },
  });

  const data = await response.json();

  if (response.ok) {
    alert(`Protected Route Accessed: ${data.message}`); // Display success message
  } else {
    alert(`Error: ${data.error}`); // Display error message
  }
});

// Handle logout
document.getElementById("logout").addEventListener("click", () => {
  localStorage.removeItem("token"); // Remove the token from localStorage
  message.textContent = "Logged out successfully!";
  message.style.color = "blue";
});
