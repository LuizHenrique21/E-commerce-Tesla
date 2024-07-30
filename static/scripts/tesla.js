const opcao1 = document.getElementById("descer1");
const opcao2 = document.getElementById("descer2");

//descer1 = região
//descer2 = usuário

function handleDropdownRegiao(){
    if(opcao2.classList.contains("active")){
        opcao2.classList.toggle("active");//desativa
        opcao1.classList.toggle("active");//ativa
    }
    else{
        opcao1.classList.toggle("active");
    }
}

function handleDropdownUsuario(){
    if(opcao1.classList.contains("active")){
        opcao1.classList.toggle("active");//desativa
        opcao2.classList.toggle("active");//ativa
    }
    else{
        opcao2.classList.toggle("active");
    }
}

function testDriveInativo(){
    alert("Opa! Parece que esse serviço está indisponível no momento, tente novamente mais tarde.")
    
} 