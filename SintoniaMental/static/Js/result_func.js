function displayResult(result){
    const text = document.getElementById('text');
    const btn_register = document.getElementById('btn-register');
    
    if(result <= 28){
        text.innerHTML = `A pontução foi de ${result} , implica que não corresponde a ter um potencial de Transtorno de Déficit de Atenção e Hiperatividade (TDAH). Agradecemos sua participação !`;
        btn_register.style.display = 'none';
    
    }
    else if (result > 28 && result <= 42 ){
        text.innerHTML = `A pontução foi de ${result} , implica que tem um leve potencial 
        a ter Transtorno de Déficit de Atenção e Hiperatividade (TDAH) . Caso queira participar da nossa plataforma para ter 
        um acompanhamento adequado e so se cadastrar .`;
        btn_register.style.display = 'block';
    }
    else if (result > 42 && result <= 56 ){
        text.innerHTML = `A pontução foi de ${result} , implica que tem um potencial mediano a ter 
        Transtorno de Déficit de Atenção e Hiperatividade (TDAH) . Aconcelhamos a começar um acompanhamento adequado , 
        ao se cadastrar em nossa plataforma pode ter consultas com especialistas da area . `;
        btn_register.style.display = 'block';
    }
    else if (result > 56 && result <= 70 ){
        text.innerHTML = `A pontução foi de ${result} , implica que tem um grande potencial a ter 
        Transtorno de Déficit de Atenção e Hiperatividade (TDAH) .Recomendamos a começar um acompalhamento o mais breve
        possivel , ao se cadastrar em nossa plataforma pode ter consultas com especialistas da area .`;
        btn_register.style.display = 'block';
    }
    else if (result > 70 ){
        text.innerHTML = `A pontução foi de ${result} , implica que tem um alto potencial de ter 
        Transtorno de Déficit de Atenção e Hiperatividade (TDAH) . Recomendamos a comecar um acompanhamento de imediato
        , cadastre-se em nossa plataforma para comerçar agora !.`;
        btn_register.style.display = 'block';
    }
    else{
        text.innerHTML = "nada foi mandado";
        btn_register.style.display = 'none';
    }

}
