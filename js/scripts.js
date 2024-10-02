const frm = document.querySelector ("form")
const Resp1 = document.querySelector ("h1")
const Resp3 = document.querySelector ("h1")

frm.addEventListener( "submit", (e) => {
    e.preventDefault ();
    
    if (empty($nome) || empty($email) || empty($senha)) {
        Resp1.innerText = "Usuário Criado Com Sucesso"; // Defina o texto que deseja exibir
    } else {
        Resp1.innerText = "Ops! Houve um erro tente novamente mais tarde"; // Texto alternativo se a condição não for atendida
    }
    
})