document.addEventListener("DOMContentLoaded", function () {
  const deleteButtons = document.querySelectorAll(".delete-button");
  const deleteForm = document.getElementById("deleteForm");

  deleteButtons.forEach((button) => {
    button.addEventListener("click", function (e) {
      e.preventDefault();
      const bookId = button.dataset.id;
      deleteForm.action = `/delete_book/${bookId}`;
      deleteForm.submit();
    });
  });
});

document.addEventListener("DOMContentLoaded", () => {
  const nameValue = localStorage.getItem("name");
  if (nameValue) {
    document.getElementById("usernameDisplay").innerText =
      "Hello, " + nameValue + "!";
  }
});
