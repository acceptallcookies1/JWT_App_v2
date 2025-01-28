document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("loginForm");
  const loginMessage = document.getElementById("loginMessage");
  const postLoginInstructions = document.getElementById("postLoginInstructions");

  let token = ""; // Store the JWT token

  // Handle login
  loginForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    try {
      const response = await fetch("/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, password }),
      });

      if (response.ok) {
        const data = await response.json();
        token = data.token;

        // Update the UI
        loginMessage.textContent = "Login successful!";
        loginMessage.style.color = "green";
        postLoginInstructions.style.display = "block"; // Show the instructions
      } else {
        loginMessage.textContent = "Invalid credentials.";
        loginMessage.style.color = "red";
        postLoginInstructions.style.display = "none"; // Hide instructions on failure
      }
    } catch (error) {
      loginMessage.textContent = "An error occurred during login.";
      loginMessage.style.color = "red";
      postLoginInstructions.style.display = "none"; // Hide instructions on error
    }
  });
});
