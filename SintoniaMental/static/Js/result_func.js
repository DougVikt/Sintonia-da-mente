function exibirResultado(resultado){
    const texto = document.getElementById('text');
    const btn_cadastrar = document.getElementById('btn-register');
    
    if(resultado <= 28){
        texto.innerHTML = `A pontução foi de ${resultado} , implica que não corresponde a ter um potencial de Transtorno de Déficit de Atenção e Hiperatividade (TDAH). Agradecemos sua participação !`;
        btn_cadastrar.style.display = 'none';
    
    }
    else if (resultado > 28 && resultado <= 42 ){
        texto.innerHTML = `A pontução foi de ${resultado} , implica que tem um leve potencial 
        a ter Transtorno de Déficit de Atenção e Hiperatividade (TDAH) . Caso queira participar da nossa plataforma para ter 
        um acompanhamento adequado e so se cadastrar .`;
        btn_cadastrar.style.display = 'block';
    }
    else if (resultado > 42 && resultado <= 56 ){
        texto.innerHTML = `A pontução foi de ${resultado} , implica que tem um potencial mediano a ter 
        Transtorno de Déficit de Atenção e Hiperatividade (TDAH) . Aconcelhamos a começar um acompanhamento adequado , 
        ao se cadastrar em nossa plataforma pode ter consultas com especialistas da area . `;
        btn_cadastrar.style.display = 'block';
    }
    else if (resultado > 56 && resultado <= 70 ){
        texto.innerHTML = `A pontução foi de ${resultado} , implica que tem um grande potencial a ter 
        Transtorno de Déficit de Atenção e Hiperatividade (TDAH) .Recomendamos a começar um acompalhamento o mais breve
        possivel , ao se cadastrar em nossa plataforma pode ter consultas com especialistas da area .`;
        btn_cadastrar.style.display = 'block';
    }
    else if (resultado > 70 ){
        texto.innerHTML = `A pontução foi de ${resultado} , implica que tem um alto potencial de ter 
        Transtorno de Déficit de Atenção e Hiperatividade (TDAH) . Recomendamos a comecar um acompanhamento de imediato
        , cadastre-se em nossa plataforma para comerçar agora !.`;
        btn_cadastrar.style.display = 'block';
    }
    else{
        texto.innerHTML = "nada foi mandado";
        btn_cadastrar.style.display = 'none';
    }

}
