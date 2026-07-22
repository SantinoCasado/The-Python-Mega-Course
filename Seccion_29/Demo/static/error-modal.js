document.addEventListener("DOMContentLoaded", function () {
  const modalElement = document.getElementById("errorModal");

  if (!modalElement || typeof bootstrap === "undefined") {
    return;
  }

  const errorModal = new bootstrap.Modal(modalElement);
  errorModal.show();
});
