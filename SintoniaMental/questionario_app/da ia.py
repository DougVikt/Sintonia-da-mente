Aqui está uma versão ajustada do projeto Django para lidar com perguntas de múltipla escolha:

1. Estrutura do Projeto
Assumindo que você já tenha a estrutura do projeto Django configurada, o arquivo questions.py será a principal fonte de dados para o quiz.

2. Arquivo questions.py
Vamos definir as perguntas e alternativas com valores de pontos:

python
Copy code
# quiz/questions.py

QUESTIONS = [
    {
        'question': 'Qual é a capital do Brasil?',
        'choices': [
            {'text': 'São Paulo', 'points': 1},
            {'text': 'Rio de Janeiro', 'points': 2},
            {'text': 'Brasília', 'points': 5},
            {'text': 'Salvador', 'points': 3},
            {'text': 'Belo Horizonte', 'points': 2},
            {'text': 'Porto Alegre', 'points': 1},
        ]
    },
    {
        'question': 'Qual é o maior planeta do sistema solar?',
        'choices': [
            {'text': 'Terra', 'points': 1},
            {'text': 'Marte', 'points': 2},
            {'text': 'Júpiter', 'points': 5},
            {'text': 'Saturno', 'points': 3},
            {'text': 'Urano', 'points': 2},
            {'text': 'Netuno', 'points': 1},
        ]
    },
    # Adicione mais perguntas aqui
]
3. View
Em quiz/views.py, a view deve lidar com o envio das respostas e acumular os pontos:

python
Copy code
from django.shortcuts import render
from django.http import JsonResponse
from .questions import QUESTIONS

def quiz_view(request, question_index=0):
    # Verifica se o índice da pergunta é válido
    if question_index >= len(QUESTIONS):
        return render(request, 'quiz/finished.html')

    # Obtém a pergunta atual
    question = QUESTIONS[question_index]

    if request.method == 'POST':
        # Processa a resposta e acumula os pontos
        choice_index = int(request.POST.get('choice'))
        choice = question['choices'][choice_index]
        points = choice['points']

        # Armazena os pontos na sessão ou banco de dados
        if 'total_points' not in request.session:
            request.session['total_points'] = 0
        request.session['total_points'] += points

        # Define o índice da próxima pergunta
        next_index = question_index + 1
        next_url = request.build_absolute_uri(f'/quiz/{next_index}/')

        return JsonResponse({'next_url': next_url})

    context = {
        'question': question,
        'question_index': question_index,
    }
    return render(request, 'quiz/quiz.html', context)
4. URLs
Em quiz/urls.py, defina as URLs para o quiz:

python
Copy code
from django.urls import path
from . import views

urlpatterns = [
    path('quiz/', views.quiz_view, name='quiz_start'),
    path('quiz/<int:question_index>/', views.quiz_view, name='quiz_question'),
]
5. Template HTML
Crie o template quiz.html em quiz/templates/quiz/quiz.html:

html
Copy code
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quiz</title>
    <style>
        .question {
            margin-bottom: 20px;
        }
        button {
            margin-top: 10px;
        }
    </style>
</head>
<body>

<div id="quiz">
    {% if question %}
        <div class="question">
            <p>{{ question.question }}</p>
            <form method="post">
                {% csrf_token %}
                {% for choice in question.choices %}
                    <input type="radio" name="choice" value="{{ forloop.counter0 }}" id="choice{{ forloop.counter0 }}">
                    <label for="choice{{ forloop.counter0 }}">{{ choice.text }}</label><br>
                {% endfor %}
                <button type="submit">Próxima</button>
            </form>
        </div>
    {% else %}
        <p>Quiz terminado!</p>
        <p>Total de Pontos: {{ request.session.total_points }}</p>
    {% endif %}
</div>

<script>
    document.querySelector('form').addEventListener('submit', function (event) {
        event.preventDefault();
        const formData = new FormData(this);
        fetch(window.location.href, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.next_url) {
                window.location.href = data.next_url;
            }
        });
    });
</script>

</body>
</html>
6. Template para Quiz Terminado
Crie o template finished.html em quiz/templates/quiz/finished.html para mostrar o resultado final:

html
Copy code
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quiz Finalizado</title>
</head>
<body>

<div>
    <h1>Quiz Terminado!</h1>
    <p>Total de Pontos: {{ request.session.total_points }}</p>
</div>

</body>
</html>
Resumo das Alterações
questions.py: Define perguntas e alternativas com valores em pontos.
View: Atualizada para processar a resposta e acumular pontos. Também fornece a próxima URL para navegação.
URLs: Definem rotas para acessar as perguntas do quiz.
Template HTML: Exibe perguntas e alternativas de múltipla escolha e usa JavaScript para navegação assíncrona.
Template Final: Mostra o total de pontos ao final do quiz.
Essa configuração deve ser adequada para um quiz de múltipla escolha com pontos associados a cada alternativa. Se precisar de mais ajustes ou tiver outras perguntas, é só me avisar!




