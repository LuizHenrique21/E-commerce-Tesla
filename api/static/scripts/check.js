
function selecionarBotao(btn) {
    var buttons = document.getElementsByClassName('opcao');
    for (var i = 0; i < buttons.length; i++) {
        buttons[i].classList.remove('ativo'); // Remove a classe 'selected' de todos os botões
    }
    btn.classList.add('ativo'); // Adiciona a classe 'selected' apenas ao botão clicado
}

function mudarCor(deslocamento) {
    var carousel = document.querySelector('.carousel');
    carousel.style.transform = 'translateX(' + deslocamento + '%)';
}

function compraRealizada(){
    alert("Sua compra foi realizada!")

    window.location.href = 'home';
    
}    