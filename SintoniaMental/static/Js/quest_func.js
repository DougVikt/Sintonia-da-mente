const alternativas = [
    {'texto':'Nunca','pontos':0},
    {'texto':'Às vezes','pontos':2},
    {'texto':'Raramente','pontos':1},
    {'texto':'Frequentimente','pontos':3},
    {'texto':'sempre','pontos':4},
];


let indice_perguntas = 0;
let soma_pontos =  0;
let porcentagem = 0;

function quest(perguntas) {
    let alternativasHtml = '';
    alternativas.forEach((alternativa) => { 
        alternativasHtml += `
        <div class="form-check w-25 col align-self-center">
            <input class="form-check-input sty-radio" type="radio" name="q${indice_perguntas + 1}" value="${alternativa.pontos}" id="radioquest${indice_perguntas}">
            <label class="form-check-label " for="radioquest${indice_perguntas}">
            ${alternativa.texto}
            </label>
        </div>`;
    });
    
    document.getElementById("pergunta").innerHTML = `
        <h2>${perguntas[indice_perguntas]}</h2><hr>
        ${alternativasHtml}
    `;
    document.getElementById("alerta").innerHTML = "";
    porcentagem = Math.round((indice_perguntas*100)/perguntas.length);
}

function next(event, perguntas) {
    event.preventDefault();
    const barra_progresso = document.getElementById("progresso");
    const radios = document.querySelectorAll(`input[name="q${indice_perguntas + 1}"]:checked`);
    if (radios.length > 0) {
        soma_pontos += parseInt(radios[0].value);
    
        indice_perguntas++;
        if (indice_perguntas < perguntas.length) {
            quest(perguntas);
            barra_progresso.innerHTML = `
            <div class="progress-bar progress-bar-striped rounded" role="progressbar" aria-label="Example with label" style="width: ${porcentagem}%;" aria-valuemin="0" aria-valuemax="100">${porcentagem}%</div>
            `;
        } 
        else if(indice_perguntas == perguntas.length) {
            document.getElementById("pergunta").innerHTML = `
                <h2>CONCLUIDO !</h2>
            `;
            barra_progresso.innerHTML = `
            <div class="progress-bar progress-bar-striped rounded" role="progressbar" aria-label="Example with label" style="width: 100%;" aria-valuemin="0" aria-valuemax="100">100%</div>
            `;
            document.getElementById('proximo').innerHTML = 'Resultado'

        }
        else {
            window.location.href = `result_func.js?resultado=${soma_pontos}`;
        }
    }else {
        if(indice_perguntas < perguntas.length){
            document.getElementById("alerta").innerHTML = `
            <div id="alerta" class="alert alert-warning align-items-center" role="alert">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi flex-shrink-0 me-2 bi-exclamation-triangle-fill" role="img" aria-label="Warning:" viewBox="0 0 16 16">
                <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5m.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2"/>
                </svg>
                <div>
                Por favor, selecione uma alternativa antes de prosseguir.
                </div>
            </div>`
        }
          
    }
}