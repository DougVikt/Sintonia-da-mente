// Seleciona o elemento nav
const nav = document.getElementById('nav');

// Adiciona um evento de scroll à janela
window.addEventListener('scroll', function() {
  // Obter a posição da barra de rolagem
  const scrollTop = window.scrollY;

  // Verifica se o usuário rolou para baixo
  if (scrollTop > nav.offsetHeight) {
    // Esconde o nav
    nav.style.top = '-100px';
    nav.style.opacity = '0.7';
  } else {
    // Exibe o nav
    nav.style.top = '0px';
    nav.style.opacity = '1';
  }
});