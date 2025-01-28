document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("loginForm");
  const postAuthForm = document.getElementById("postAuthForm");
  const loginMessage = document.getElementById("loginMessage");
  const postLoginInstructions = document.getElementById("postLoginInstructions");
  const postAuthMessage = document.getElementById("postAuthMessage");

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
        postAuthForm.style.display = "block"; // Show the post-auth form
      } else {
        loginMessage.textContent = "Invalid credentials.";
        loginMessage.style.color = "red";
        postLoginInstructions.style.display = "none"; // Hide instructions on failure
        postAuthForm.style.display = "none"; // Hide post-auth form on failure
      }
    } catch (error) {
      loginMessage.textContent = "An error occurred during login.";
      loginMessage.style.color = "red";
      postLoginInstructions.style.display = "none"; // Hide instructions on error
      postAuthForm.style.display = "none"; // Hide post-auth form on error
    }
  });

  // Handle post-auth form submission
  postAuthForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const formData = document.getElementById("formData").value;

    try {
      const response = await fetch("/post-auth", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${token}`,
        },
        body: JSON.stringify({ formData }),
      });

      if (response.ok) {
        const data = await response.json();
        postAuthMessage.textContent = data.message;
        postAuthMessage.style.color = "green";
      } else {
        const error = await response.json();
        postAuthMessage.textContent = error.error || "An error occurred.";
        postAuthMessage.style.color = "red";
      }
    } catch (error) {
      postAuthMessage.textContent = "An error occurred during form submission.";
      postAuthMessage.style.color = "red";
    }
  });
});
