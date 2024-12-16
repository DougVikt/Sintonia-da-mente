// verifica se as senhas são identicas 
function ValidacaoSenha(){
    let senha = document.getElementById('password');
    let confereSenha = document.getElementById('check-password');
    let msmErro = document.getElementById('erro');

    if (senha.value !== confereSenha.value) {
      senha.classList.add('is-invalid');
      confereSenha.classList.add('is-invalid');
      msmErro.innerHTML= 'As senhas não são identicas !'
      
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

// limita a senha a ter no minimo 8 e no maximo 20 caracteres 
document.addEventListener("DOMContentLoaded",function(){
  let passwordInput = document.getElementById('password');
  passwordInput.addEventListener('input',function(p){
      const password = this.value;
      if(password.length < 8 ){
        this.setCustomValidity('A senha deve ter no mínimo 8 caracteres.');
      }
      else if(password.length > 20){
        this.setCustomValidity('A senha deve ter no máximo 20 caracteres.');
      }
      else{
        this.setCustomValidity('');
      }
  });
})