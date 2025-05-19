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

  const usernameValid = /[A-Za-z]/.test(userName.value);
  const emailValid = /^[\w.-]+@[A-Za-z0-9.-]+\.(com)$/.test(email.value);

  if (!usernameValid) {
    error.textContent = "Username must include at least one letter.";
    return false;
  }

  if (!emailValid) {
    error.textContent = "Email must end with .com";
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

const togglePassword = document.getElementById("togglePassword");

if (togglePassword) {
  togglePassword.addEventListener("click", function () {
    const passwordField =
      document.getElementById("loginPassword") ||
      document.getElementById("password");

    const type =
      passwordField.getAttribute("type") === "password" ? "text" : "password";

    passwordField.setAttribute("type", type);

    togglePassword.innerHTML = type === "password" ? "🔒" : "🔓";
  });
}

function logout() {
  localStorage.removeItem("name");
}
