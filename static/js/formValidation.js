function validateForm() {
  document.getElementById("error").textContent = "";

  const userName = document.getElementById("userName").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  if (!userName || !email || !password) {
    document.getElementById("error").textContent = "All fields are required!";
    return false;
  }

  if (password.length < 6) {
    document.getElementById("error").textContent =
      "Password must be at least 6 characters long.";
    return false;
  }

  localStorage.setItem("name", userName);
  alert("Welcome " + userName + " :) !");

  return true;
}
