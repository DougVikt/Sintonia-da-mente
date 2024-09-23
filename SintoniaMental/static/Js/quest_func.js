function textos(tipo=''){
    const perguntas_usu = [
        'Tem dificuldade em prestar atenção em detalhes ou comete erros por descuido no trabalho ou em tarefas escolares?',
        'Acha difícil manter o foco em tarefas ou atividades, como ler um livro ou assistir a uma palestra?',
        'Frequentemente evita ou se sente relutante em iniciar tarefas que exigem esforço mental prolongado, como preparar relatórios ou fazer lição de casa?',
        'Frequentemente perde objetos necessários para tarefas ou atividades, como chaves, óculos ou celular?',
        'Se sente frequentemente inquieto ou agitado, como se precisasse estar sempre em movimento?',
        'Tem dificuldade em esperar sua vez em filas ou em outras situações?',
        'Frequentemente interrompe ou se intromete em conversas ou atividades de outras pessoas?',
        'Se distrai facilmente com estímulos externos, como barulhos ou movimentos ao seu redor?',
        'Frequentemente esquece de cumprir compromissos ou obrigações, como retornar ligações ou pagar contas?',
        'Tem dificuldade em seguir instruções ou completar tarefas, mesmo que sejam simples?',
        'Frequentemente se sente impaciente ou tem dificuldade em ficar sentado por longos períodos?',
        'Tem dificuldade em organizar tarefas e atividades, como planejar seu dia ou manter um cronograma?',
        'Frequentemente fala excessivamente, mesmo em situações onde deveria estar mais calado?',
        'Tem dificuldade em seguir conversas longas ou se perde facilmente durante uma discussão?',
        'Frequentemente se sente sobrecarregado com tarefas diárias ou responsabilidades?',
        'Tem dificuldade em relaxar ou se sente constantemente “ligado”?',
        'Frequentemente age impulsivamente, como tomar decisões sem pensar nas consequências?',
        'Tem dificuldade em completar projetos ou tarefas que começa?',
        'Frequentemente se sente frustrado ou irritado com facilidade?',
        'Tem dificuldade em lembrar de informações importantes, como datas ou compromissos?',
        
    ];

    const perguntas_pais= [

        'Não presta atenção aos detalhes ou comete erros por descuido nos trabalhos escolares, no trabalho ou em outras atividades?',
        'Tem dificuldade em manter a atenção em tarefas ou brincadeiras?',
        'Parece não ouvir quando se lhe fala diretamente?',
        'Não segue instruções e não termina os trabalhos escolares, tarefas ou deveres no local de trabalho (começa tarefas, mas logo se distrai e se desvia para outras atividades)?',
        'Tem dificuldade em organizar tarefas e atividades?',
        'Evita, reluta ou se desvia de tarefas que exigem esforço mental sustentado (como trabalhos escolares ou deveres de casa)?',
        "Perde objetos necessários para tarefas ou atividades (por exemplo, lápis, livros, cadernos, ferramentas, carteiras, chaves, documentos, óculos, celulares)?",
        'É facilmente distraído por estímulos alheios?',
        'É esquecido em relação às atividades diárias?',
        'Mexe as mãos ou os pés, ou se contorce na cadeira?',
        'Abandona a sua cadeira em lugares fechados ou em outras situações em que se espera que permaneça sentado?',
        'Corre ou escala em demasia em situações inapropriadas (em adolescentes ou adultos, pode se limitar a uma sensação de inquietação)?',
        'Tem dificuldade em brincar ou se envolver em atividades de lazer calmamente?',
        'Age como se estivesse "a todo vapor"?',
        'Fala excessivamente?',
        'Dá respostas precipitadas antes que as perguntas sejam completamente feitas?',
        'Tem dificuldade em esperar a sua vez?',
        'Intromete-se ou interrompe os outros?',
        'Corre desmedidamente em situações inadequadas ou fica pulando em locais inapropriados (ou se sente inquieto em adolescentes ou adultos)?',
        'Usa objetos de maneira imprópria ou perigosa ou brinca com fogo? (Apenas para crianças mais novas)',
    ];

    const perguntas_prof = [
        'O aluno(a) tem dificuldade em prestar atenção aos detalhes ou comete erros por descuido nas tarefas escolares?',
        'O aluno(a) tem dificuldade em manter a atenção em tarefas ou atividades lúdicas?',
        'O aluno(a) parece não escutar quando se fala diretamente com ele?',
        'O aluno(a) não segue instruções e não termina tarefas escolares, tarefas domésticas ou deveres?',
        'O aluno(a) tem dificuldade em organizar tarefas e atividades?',
        'O aluno(a) evita, não gosta ou reluta em se envolver em tarefas que exigem esforço mental prolongado?',
        'O aluno(a) perde coisas necessárias para tarefas ou atividades (por exemplo, brinquedos, tarefas escolares, lápis, livros)?',
        'O aluno(a) é facilmente distraído por estímulos externos?',
        'O aluno(a) é esquecido em atividades diárias?',
        'O aluno(a) se mexe ou bate com as mãos ou pés, ou se remexe na cadeira?',
        'O aluno(a) se levanta da cadeira em situações em que se espera que permaneça sentado?',
        'O aluno(a) corre ou sobe em lugares inadequados?',
        'O aluno(a) tem dificuldade em brincar ou se envolver em atividades de lazer de forma calma?',
        'O aluno(a) está "a mil" ou frequentemente age como se estivesse "a todo vapor"?',
        'O aluno(a) fala excessivamente?',
        'O aluno(a) responde antes que as perguntas sejam completadas?',
        'O aluno(a) tem dificuldade em esperar a sua vez?',
        'O aluno(a) interrompe ou se intromete nas conversas ou jogos dos outros?',
        'O aluno(a) tem dificuldade em seguir regras ou instruções?',
        'O aluno(a) apresenta comportamentos impulsivos que podem ser perigosos?',
    ];
    
    if(tipo == 'user'){
        return perguntas_usu;
    }
    else if(tipo == 'pais' ){
        return perguntas_pais;
    }
    else if(tipo == 'prof'){
        return perguntas_prof;
    }

    
}

const alternativas = [
    {'texto':'Nunca','pontos':0},
    {'texto':'As vezes','pontos':2},
    {'texto':'Raramente','pontos':1},
    {'texto':'Frequentemente','pontos':3},
    {'texto':'Sempre','pontos':4},
];

let indice_perguntas = 0;
let soma_pontos =  0;
let porcentagem = 0;
let direcionanado = false;
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
    const radios = document.querySelectorAll(`input[name="q${indice_perguntas + 1}"]:checked`);
    if(direcionanado){
        window.location.href = 'resultado.html';
        localStorage.setItem('resultado', soma_pontos);     
        
    }
    if (radios.length > 0) {
        soma_pontos += parseInt(radios[0].value);
    
        indice_perguntas++;
        if (indice_perguntas < perguntas.length) {
            quest(perguntas);
            document.getElementById("progresso").innerHTML = `
            <div class="progress-bar progress-bar-striped rounded" role="progressbar" aria-label="Example with label" style="width: ${porcentagem}%;" aria-valuemin="0" aria-valuemax="100">${porcentagem}%</div>
            `;
        } 
        else if(indice_perguntas == perguntas.length) {
            document.getElementById("pergunta").innerHTML = `
                <h2>CONCLUIDO !</h2>
            `;
            document.getElementById("progresso").innerHTML = `
            <div class="progress-bar progress-bar-striped rounded" role="progressbar" aria-label="Example with label" style="width: 100%;" aria-valuemin="0" aria-valuemax="100">100%</div>
            `;
            document.getElementById('proximo').innerHTML = 'Resultado'
            
            direcionanado = true;
        }
        else {
            window.location.href = 'index.html';
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

