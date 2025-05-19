document.querySelectorAll(".edit-button").forEach((button) => {
  button.addEventListener("click", function (e) {
    e.preventDefault();
    document.getElementById("editId").value = this.dataset.id;
    document.getElementById("editTitle").value = this.dataset.title;
    document.getElementById("editAuthor").value = this.dataset.author;
    document.getElementById("editYear").value = this.dataset.year;
    document.getElementById("editReview").value = this.dataset.review;
    document.getElementById("editDescription").value =
      this.dataset.description || "";
    document.getElementById("editPercentage").value =
      this.dataset.percentage || "";
    document.getElementById("editModal").style.display = "flex";
  });
});

document.querySelector("#editModal .close").addEventListener("click", () => {
  document.getElementById("editModal").style.display = "none";
});

window.addEventListener("click", function (event) {
  if (event.target.id === "editModal") {
    document.getElementById("editModal").style.display = "none";
  }
});
