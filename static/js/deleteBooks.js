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
    const capitalized =
      nameValue.charAt(0).toUpperCase() + nameValue.slice(1).toLowerCase();
    document.getElementById("usernameDisplay").innerText =
      "Hello, " + capitalized + "!";
  }
});
