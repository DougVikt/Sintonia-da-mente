function textos(type=''){
    const user_questions = [
        'Tem dificuldade em prestar atenção em detalhes ou comete erros por descuido no trabalho ou em tarefas escolares?',
        'Acha difícil manter o foco em tarefas ou atividades, como ler um livro ou assistir a uma palestra?',
        'Frequentemente evita ou sente ansiedade em iniciar tarefas que exigem esforço mental prolongado, como preparar relatórios ou fazer lição de casa?',
        'Frequentemente perde objetos necessários para tarefas ou atividades, como chaves, óculos ou celular?',
        'Se sente frequentemente inquieto ou agitado, como se precisasse estar sempre em movimento?',
        'Tem dificuldade em esperar sua vez em filas ou em outras situações que requer espera?',
        'Frequentemente interrompe ou se intromete em conversas ou atividades de outras pessoas?',
        'Se distrai facilmente com estímulos externos, como barulhos ou movimentos ao seu redor?',
        'Frequentemente esquece de cumprir compromissos ou obrigações, como retornar ligações ou pagar contas?',
        'Tem dificuldade em seguir instruções ou completar tarefas, mesmo que sejam simples?',
        'Frequentemente se sente impaciente ou tem dificuldade em ficar sentado por longos períodos?',
        'Tem dificuldade em organizar tarefas e atividades, como planejar seu dia ou manter um cronograma?',
        'Frequentemente fala excessivamente, mesmo em situações onde deveria estar mais calado?',
        'Tem dificuldade em seguir conversas longas ou se perde facilmente durante uma discussão?',
        'Frequentemente se sente desorganizado com tarefas diárias ou responsabilidades?',
        'Tem dificuldade em relaxar ou se sente constantemente “ligado”?',
        'Frequentemente age impulsivamente, como tomar decisões sem pensar nas consequências?',
        'Tem dificuldade em completar projetos ou tarefas que começa?',
        'Frequentemente se sente frustrado ou irritado com facilidade?',
        'Tem dificuldade em lembrar de informações importantes, como datas ou compromissos?',
        
    ];

    const parent_questions= [

        'Não presta atenção aos detalhes ou comete erros por descuido nos trabalhos escolares, no trabalho ou em outras atividades?',
        'Tem dificuldade em manter a atenção em tarefas ou brincadeiras, podendo esquecer as regras facilmente?',
        'Parece ter dificuldade de prestar atenção ou ouvir quando lhe fala diretamente?',
        'Não segue instruções e não termina os trabalhos escolares, tarefas ou deveres no local de trabalho (começa tarefas, mas logo se distrai e se desvia para outras atividades)?',
        'Tem dificuldade em organizar sozinho tarefas e atividades?',
        'Evita, reluta ou se desvia de tarefas que exigem esforço mental sustentado (como trabalhos escolares, lição de casa ou atividades domesticas)?',
        "Perde objetos necessários para tarefas ou atividades (por exemplo, lápis, livros, cadernos, ferramentas, carteiras, chaves, documentos, óculos, celulares)?",
        'É facilmente distraído por estímulos alheios?',
        'É esquecido em relação às atividades diárias?',
        'Mexe as mãos ou os pés, ou se contorce na cadeira constantemente?',
        'Abandona a sua cadeira em lugares fechados ou em outras situações em que se espera que permaneça sentado?',
        'Em situações sociais, costuma correr, subir em algum lugar ou incomodar outras pessoas em seus espaços pessoais (em adolescentes ou adultos, pode se limitar a uma sensação de inquietação constante)?',
        'Tem dificuldade em brincar ou se envolver em atividades de lazer calmamente?',
        'Age como se estivesse "a todo vapor"?',
        'Fala excessivamente, até mesmo em situações indevidas?',
        'Dá respostas precipitadas antes que as perguntas sejam completamente feitas?',
        'Frequentemente tem dificuldade em esperar a sua vez?',
        'Frequentemente intromete-se ou interrompe os outros?',
        'Tem dificuldade de obedecer regras socoais de comportamento adequado em alguns lugares, podendo correr em situações inadequadas ou fica pulando em locais inapropriados (inquietação em adolescentes ou adultos)?',
        'Usa objetos de maneira imprópria ou perigosa ou brinca com fogo? (Apenas para crianças mais novas)',
    ];

    const teacher_questions = [
        'O aluno(a) tem dificuldade em prestar atenção aos detalhes ou comete erros por descuido nas tarefas escolares?',
        'O aluno(a) tem dificuldade em manter a atenção em tarefas ou atividades lúdicas?',
        'O aluno(a) parece não escutar ou prestar atenção quando se fala diretamente com ele?',
        'O aluno(a) não segue instruções e não termina tarefas escolares, tarefas domésticas ou deveres?',
        'O aluno(a) tem dificuldade em organizar tarefas, material escolar e atividades?',
        'O aluno(a) evita, não gosta ou desiste em se envolver em tarefas que exigem esforço mental prolongado?',
        'O aluno(a) perde coisas necessárias para tarefas ou atividades (por exemplo, brinquedos, tarefas escolares, lápis, livros)?',
        'O aluno(a) é facilmente distraído por estímulos externos como: barulhos, brincadeiras ou outras pessoas ao arredor?',
        'O aluno(a) tem dificuldade em seguir as atividades diárias pedidas?',
        'O aluno(a) se mexe ou bate com as mãos ou pés, ou se remexe na cadeira constantemente?',
        'O aluno(a) frequentemente se levanta da cadeira em situações em que se espera que permaneça sentado?',
        'O aluno(a) frequentemente corre ou sobe em lugares inadequados?',
        'O aluno(a) tem dificuldade em brincar ou se envolver em atividades de lazer de forma calma?',
        'O aluno(a) está "a mil" ou frequentemente age como se estivesse "a todo vapor"?',
        'O aluno(a) fala excessivamente, até mesmo em locais inadequados ou mesmo com orientação para se comportar de outra maneira?',
        'O aluno(a) frequentemente responde antes que as perguntas sejam completadas?',
        'O aluno(a) frequentemente tem dificuldade em esperar a sua vez?',
        'O aluno(a) interrompe ou se intromete nas conversas ou jogos de outros colegas ou outras pessoas em geral?',
        'O aluno(a) tem dificuldade em seguir regras ou instruções?',
        'O aluno(a) apresenta comportamentos impulsivos que podem ser perigosos para si mesmo e para outros?',
    ];
    
    if(type == 'user'){
        return user_questions;
    }
    else if(type == 'parent' ){
        return parent_questions;
    }
    else if(type == 'teacher'){
        return teacher_questions;
    }

    
}

const alternatives = [
    {'text':'Nunca','pontos':0},
    {'text':'As vezes','pontos':2},
    {'text':'Raramente','pontos':1},
    {'text':'Frequentemente','pontos':3},
    {'text':'Sempre','pontos':4},
];

let index_questions = 0;
let sum_points =  0;
let percentages = 0;
let directing = false;
function quest(questions) {
    let alternativesHtml = '';
    alternatives.forEach((alternatives) => { 
        alternativesHtml += `
        <div class="form-check w-25 col align-self-center">
            <input class="form-check-input sty-radio" type="radio" name="q${index_questions + 1}" value="${alternatives.pontos}" id="radioquest${index_questions}">
            <label class="form-check-label " for="radioquest${index_questions}">
            ${alternatives.texto}
            </label>
        </div>`;
    });
    
    document.getElementById("pergunta").innerHTML = `
        <h2>${perguntas[index_questions]}</h2><hr>
        ${alternativesHtml}
    `;
    document.getElementById("alerta").innerHTML = "";
    percentages = Math.round((index_questions*100)/perguntas.length);
}

function next(event, perguntas) {
    event.preventDefault();
    const radios = document.querySelectorAll(`input[name="q${index_questions + 1}"]:checked`);
    if(directing){
        window.location.href = 'end_result.html';
        localStorage.setItem('resultado', sum_points);     
        
    }
    if (radios.length > 0) {
        sum_points += parseInt(radios[0].value);
    
        index_questions++;
        if (index_questions < perguntas.length) {
            quest(perguntas);
            document.getElementById("progresso").innerHTML = `
            <div class="progress-bar progress-bar-striped rounded" role="progressbar" aria-label="Example with label" style="width: ${percentages}%;" aria-valuemin="0" aria-valuemax="100">${percentages}%</div>
            `;
        } 
        else if(index_questions == perguntas.length) {
            document.getElementById("pergunta").innerHTML = `
                <h2>CONCLUIDO !</h2>
            `;
            document.getElementById("progresso").innerHTML = `
            <div class="progress-bar progress-bar-striped rounded" role="progressbar" aria-label="Example with label" style="width: 100%;" aria-valuemin="0" aria-valuemax="100">100%</div>
            `;
            document.getElementById('proximo').innerHTML = 'Resultado'
            
            directing = true;
        }
        else {
            window.location.href = 'home.html';
        }
    }else {
        if(index_questions < perguntas.length){
            document.getElementById("alert-------------------------------------------------------").innerHTML = `
            <div id="alerta" class="alert alert-warning align-items-center" role="alert">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi flex-shrink-0 me-2 bi-exclamation-triangle-fill" role="img" aria-label="Warning:" viewBox="0 0 16 16">
                <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5m.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2"/>
                </svg>
                <div>
                Por favor, selecione uma alternativas antes de prosseguir.
                </div>
            </div>`
        }
          
    }
  
}

