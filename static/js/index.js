function validateForm(form) {
  if (
    confirm(
      "Vous Voulez vraiment Supprimer Ce Conteneur? Cette Action est irreversible"
    )
  ) {
    return true;
  } else {
    form.action = ""; 
    return false;
  }
}

function cleanSelection() {
  let options = Array.from(document.getElementsByTagName("option"));
  options.map((e) => {
    e.textContent = e.textContent.replace(/[^a-zA-Z/:]/g, "");
  });
}
cleanSelection();

function styles() {
  let status = Array.from(document.querySelectorAll(".status"));
  status.map((row) => {
    if (row.textContent == "exited") {
      row.textContent = "Arrêté";
      row.setAttribute("class", "status fs-3 text-danger");
    }
    if (row.textContent == "running") {
      row.textContent = "En Cours d'Execution";
      row.setAttribute("class", "status fs-3 text-success");
      row.setAttribute("action", "/");
    }
    if (row.textContent == "created") {
      row.textContent = "Créé Avec Succès";
      row.setAttribute("class", "status fs-3 text-info");
    }
  });
}

styles();
