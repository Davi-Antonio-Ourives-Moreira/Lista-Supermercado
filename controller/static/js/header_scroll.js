window.addEventListener('scroll', function() {
    const nav = document.getElementById('nav');

    const logo = document.getElementById('logo');

    const menu_nav = this.document.getElementById('menu_nav');
    
    if (window.scrollY > 50) { // Ajuste o valor conforme necessário
        nav.style.backgroundColor = "#2c2525";
        logo.style.width = "200px";
        menu_nav.style.top = "40px";
    } else {
        nav.style.backgroundColor = "transparent";
        logo.style.width = "250px";
        menu_nav.style.top = "50px";
    }
});