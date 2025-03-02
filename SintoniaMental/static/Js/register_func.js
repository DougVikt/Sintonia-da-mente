
// Função para validar se as senhas são idênticas
function validationPassword(){
  let password = document.getElementById('password');
  let checkpassword = document.getElementById('check-password');
  let msmErro = document.getElementById('error');

  // Verifica se as senhas são diferentes
  if (password.value !== checkpassword.value) {
    // Adiciona a classe 'is-invalid' aos campos de senha
    password.classList.add('is-invalid');
    checkpassword.classList.add('is-invalid');
    // Exibe a mensagem de erro
    msmErro.innerHTML = 'As senhas não são idênticas!';
    
    return false;
  }
  
  return true;
}

// formata a caixa input do telefone para o formato correto e limitando apenas a numeros 
document.addEventListener('DOMContentLoaded', function() {
  let foneInput = document.getElementById('fone');

  foneInput.addEventListener('input', function (f) {
      let x = f.target.value.replace(/\D/g, '').match(/(\d{0,2})(\d{0,1})(\d{0,4})(\d{0,4})/);
      f.target.value = !x[2] ? x[1] : '(' + x[1] + ') 9' + x[3] + (x[4] ? '-' + x[4] : '');
  });

  foneInput.addEventListener('keydown', function (f) {
      if (!/[0-9]/.test(f.key) && !['Backspace', 'Delete', 'ArrowLeft', 'ArrowRight', 'Tab'].includes(f.key)) {
          f.preventDefault();
      }
  });
});

// limita a passworda ter no minimo 8 e no maximo 20 caracteres 
document.addEventListener("DOMContentLoaded",function(){
  let passwordInput = document.getElementById('password');
  passwordInput.addEventListener('input',function(p){
      const password = this.value;
      if(password.length < 8 ){
        this.setCustomValidity('A passworddeve ter no mínimo 8 caracteres.');
      }
      else if(password.length > 20){
        this.setCustomValidity('A passworddeve ter no máximo 20 caracteres.');
      }
      else{
        this.setCustomValidity('');
      }
  });
})

document.addEventListener("DOMContentLoaded", function() {
  let type_register = document.getElementById('type_register');
  let number_register = document.getElementById('number_register');

  // Função para formatar o CRP
  function formatCRP(t) {
    let x = t.target.value.replace(/\D/g, '').match(/(\d{0,2})(\d{0,7})/);
    t.target.value = !x[2] ? x[1] : x[1] + '/' + x[2];
  }

  // Função para formatar o CRM
  function formatCRM(t) {
    let value = t.target.value.toUpperCase().replace(/[^A-Z0-9]/g, '');
    let x = value.match(/([A-Z]{0,2})(\d{0,7})/);
    t.target.value = !x[2] ? x[1] : x[1] + '/' + x[2];
  }

  // Função para atualizar o formatador com base no tipo de registro
  function updateFormatter() {
    number_register.removeEventListener('input', formatCRP);
    number_register.removeEventListener('input', formatCRM);

    if (type_register.value == 'CRP') {
      number_register.addEventListener('input', formatCRP);
    } else if (type_register.value == 'CRM') {
      number_register.addEventListener('input', formatCRM);
    }
  }
  updateFormatter();

  // Detecta a mudança no tipo de registro
  type_register.addEventListener('change', updateFormatter);
});