const formID = document.getElementById("login_form");

var onSendClick = function (event) {
    if (formID.checkValidity()) {
      event.target.parentNode.classList.add("disabled");
      event.target.removeEventListener("click", onSendClick);
    }
}

formID.addEventListener('submit', function(e) {
    e.preventDefault();

    window.location.href = "home";
});
  
send.addEventListener("click", onSendClick);

