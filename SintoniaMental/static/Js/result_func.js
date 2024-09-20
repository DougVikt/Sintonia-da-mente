   // Função para obter o valor do parâmetro da URL
function getParametro(name) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(name);
}

// Obtendo o resultado da URL e exibindo no HTML
const resultado = getParametro('resultado');
const titulo = document.getElementById('titulo');

