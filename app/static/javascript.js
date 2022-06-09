(function (win, doc) {
  "use strict";

  // Verifica se o usuario quer realmente deletar o dado
  if (doc.querySelector(".btnDel")) {
    let btnDel = doc.querySelectorAll(".btnDel");
    for (let i = 0; i < btnDel.length; i++) {
      btnDel[i].addEventListener("click", function (event) {
        if (
          confirm(
            "Essa ação excluirá permanentemente a vaga. Tem certeza que deseja excluí-la?"
          )
        ) {
          return true;
        } else {
          event.preventDefault();
        }
      });
    }
  }

  // Ajax do Form
  if (doc.querySelector("#form")) {
    let form = doc.querySelector("#form");
    function sendForm(event) {
      event.preventDefault();
      let data = new FormData(form);
      let ajax = new XMLHttpRequest();
      let token = doc.querySelectorAll("input")[0].value;
      ajax.open("POST", form.action);
      ajax.setRequestHeader("X-CSRF-TOKEN", token);
      ajax.onreadystatechange = function () {
        if (ajax.status === 200 && ajax.readyState === 4) {
          let result = doc.querySelector("#result");
          result.innerHTML = "Vaga cadastrada com sucesso!";
          result.classList.add("alert");
          result.classList.add("alert-success");
        }
      };
      ajax.send(data);
      form.reset();
    }
    form.addEventListener("submit", sendForm, false);
  }

  if (doc.getElementById("#dateField")) {
    let dataInput = doc.getElementById("#dateField");
    function date() {
      let data = new Date(dataInput);
      let dataFormatada = data.toLocaleDateString("pt_BR", { timeZone: "UTC" });
      
      return dataFormatada;
    }
  }
})(window, document);
