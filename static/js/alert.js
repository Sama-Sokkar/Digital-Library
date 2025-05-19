function showAlert(message, color ) {
  const alertBox = document.createElement("div");
  alertBox.className = "alert";
  alertBox.style.backgroundColor = color;
  alertBox.innerText = message;

  document.body.appendChild(alertBox);

  setTimeout(() => {
    alertBox.style.opacity = "0";
    setTimeout(() => {
      alertBox.remove();
    }, 1000);
  }, 2000);
}
