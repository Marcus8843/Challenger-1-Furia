function mudarTexto() {
   const titulo = document.getElementById("titulo");
   titulo.innerText = "Você clicou no botão! Fúria te saúda!";
}
  function toggleModal() {
    const modal = document.getElementById("menuModal");
    modal.style.display = modal.style.display === "block" ? "none" : "block";
  }

  window.onclick = function(event) {
    const modal = document.getElementById("menuModal");
    if (event.target === modal) {
      modal.style.display = "none";
    }
  }
