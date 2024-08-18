function Ver_Senha(){
    const senha = document.getElementById("senha");

    const olho_fechado = document.getElementById("olho_fechado");

    const olho_aberto = document.getElementById("olho_aberto")
    
    if (senha.type == "password"){
        senha.type = "text";
        olho_fechado.style.display = "none";
        olho_aberto.style.display = "block";
        
    } else{
        senha.type = "password";
        olho_aberto.style.display = "none";
        olho_fechado.style.display = "block";
    }
}