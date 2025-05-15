document.addEventListener("DOMContentLoaded", function () {
  const deleteButtons = document.querySelectorAll(".delete-button");
  const deleteForm = document.getElementById("deleteForm");

  deleteButtons.forEach(button => {
    button.addEventListener("click", function (e) {
      e.preventDefault();
      const confirmed = confirm("Are you sure you want to delete this book?");
      if (confirmed) {
        const bookId = button.dataset.id;
        deleteForm.action = `/delete_book/${bookId}`;
        deleteForm.submit();
      }
    });
  });
});
