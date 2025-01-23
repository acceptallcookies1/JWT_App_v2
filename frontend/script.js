const loginForm = document.getElementById("loginForm");
const message = document.getElementById("message");

loginForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  const username = event.target.username.value;
  const password = event.target.password.value;

  const response = await fetch("/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  });

  const data = await response.json();

  if (response.ok) {
    message.textContent = `Login successful! Token: ${data.token}`;
    message.style.color = "green";
  } else {
    message.textContent = `Error: ${data.error}`;
    message.style.color = "red";
  }
});
