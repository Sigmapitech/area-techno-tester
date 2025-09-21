const loginBtn = document.getElementById("loginBtn");
const message = document.getElementById("message");

// Fake "database" of one user
const USERNAME = "admin";
const PASSWORD = "12345";

loginBtn.addEventListener("click", () => {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  if (username === USERNAME && password === PASSWORD) {
    message.textContent = "✅ Login successful!";
    message.style.color = "green";
    // Redirect to a protected page
    setTimeout(() => {
      window.location.href = "dashboard.html";
    }, 1000);
  } else {
    message.textContent = "❌ Invalid credentials";
    message.style.color = "red";
  }
});