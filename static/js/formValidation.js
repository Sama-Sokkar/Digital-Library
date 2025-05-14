// register constants
const error = document.getElementById("error");
const userName = document.getElementById("userName");
const email = document.getElementById("email");
const password = document.getElementById("password");

// Login constants
const loginEmail = document.getElementById("loginEmail");
const loginPassword = document.getElementById("loginPassword");

function validateForm() {
  if (!userName.value || !email.value || !password.value) {
    error.textContent = "All fields are required!";
    return false;
  }

  if (password.value.length < 6) {
    error.textContent = "Password must be at least 6 characters long.";
    return false;
  }
  return true;
}
function validateLogin() {
  if (!loginEmail.value || !loginPassword.value) {
    error.textContent = "Both email and password are required!";
    return false;
  }

  return true;
}

function logout() {
  localStorage.removeItem("name");
}

document.addEventListener("DOMContentLoaded", () => {
  const nameValue = localStorage.getItem("name");
  if (nameValue) {
    document.getElementById("usernameDisplay").innerText =
      "Hello, " + nameValue + "!";
  }
});
