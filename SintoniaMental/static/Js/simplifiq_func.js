function ValidacaoSenha(){
    let senha = document.getElementById('senha');
    let confereSenha = document.getElementById('confere-senha');
    let msmErro = document.getElementById('erro');

    if (senha.value !== confereSenha.value) {
      senha.classList.add('is-invalid');
      confereSenha.classList.add('is-invalid');
      msmErro.innerHTML= 'As senhas não são identicas !'
      
      return false;
    }
    
    return true;
   
  }


  document.addEventListener('DOMContentLoaded', function() {
    var foneInput = document.getElementById('fone');

    foneInput.addEventListener('input', function (e) {
        var x = e.target.value.replace(/\D/g, '').match(/(\d{0,2})(\d{0,1})(\d{0,4})(\d{0,4})/);
        e.target.value = !x[2] ? x[1] : '(' + x[1] + ') 9' + x[3] + (x[4] ? '-' + x[4] : '');
    });

    foneInput.addEventListener('keydown', function (e) {
        if (!/[0-9]/.test(e.key) && !['Backspace', 'Delete', 'ArrowLeft', 'ArrowRight', 'Tab'].includes(e.key)) {
            e.preventDefault();
        }
    });
  });