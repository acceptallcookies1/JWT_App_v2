document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("loginForm");
  const tokenDisplay = document.getElementById("tokenDisplay");
  const postAuthButton = document.getElementById("postAuthButton");
  const messageElement = document.getElementById("message");
  const postAuthMessage = document.getElementById("postAuthMessage");

  let token = ""; // Store the token after login

  // Login Form Submission
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

        // Display token and enable post-auth button
        tokenDisplay.value = token;
        postAuthButton.disabled = false;
        messageElement.textContent = "Login successful! Token generated.";
        messageElement.style.color = "green";
      } else {
        const error = await response.json();
        messageElement.textContent = error.error || "Login failed.";
        messageElement.style.color = "red";
      }
    } catch (err) {
      messageElement.textContent = "An error occurred during login.";
      messageElement.style.color = "red";
    }
  });

  // Post-Auth Verification
  postAuthButton.addEventListener("click", async () => {
    try {
      const response = await fetch("/post-auth", {
        method: "GET",
        headers: {
          "Authorization": `Bearer ${token}`,
        },
      });

      if (response.ok) {
        const data = await response.json();
        postAuthMessage.textContent = data.message;
        postAuthMessage.style.color = "green";
      } else {
        const error = await response.json();
        postAuthMessage.textContent = error.error || "Token verification failed.";
        postAuthMessage.style.color = "red";
      }
    } catch (err) {
      postAuthMessage.textContent = "An error occurred during token verification.";
      postAuthMessage.style.color = "red";
    }
  });
});
