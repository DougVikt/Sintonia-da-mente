// Seleciona o elemento nav
const nav = document.getElementById('nav');

// posição atual do scroll
let posicion_scroll = 0;

// Adiciona um evento de scroll à janela
window.addEventListener('scroll', function() {
  // Obter a posição da barra de rolagem
  let scrollTop = window.scrollY;

  // Verifica se o usuário rolou para baixo
  if (scrollTop > posicion_scroll) {
    // Esconde o nav
    nav.style.top = '-60px';
    nav.style.opacity = '0.7';
  } else {
    // Exibe o nav
    nav.style.top = '0px';
    nav.style.opacity = '1';
  }
  // Atualiza a posição do scroll
  posicion_scroll = scrollTop;
});