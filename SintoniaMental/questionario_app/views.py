from django.shortcuts import render
from django.views.generic import TemplateView


alternativas = {
    'teste 1':0,
    'teste 2':2,
    'teste 3':4,
    'teste 4':6,
    'teste 5':8,
    }  

def quest(request):
    return render(request, 'questionario.html') 


# Função para exibir as perguntas e alternativas
def quest_usuario(request):
# Verificar se o usuário enviou uma resposta
    if request.method == 'POST':
        # Obter a resposta do usuário
        resposta_atual = request.POST.get('answer')
        
        # Obter a pergunta atual da sessão
        pergunta_atual = request.session.get('pergunta_atual')
        
        # Verificar se a pergunta atual e a resposta do usuário são válidas
        if pergunta_atual is not None and resposta_atual is not None:
            # Armazenar a resposta do usuário na sessão
            request.session['respostas'][pergunta_atual] = resposta_atual
            
            # Incrementar a pergunta atual
            request.session['pergunta_atual'] += 1

    # Definir as perguntas e alternativas
    perguntas = [
        'olgo aqui ?',
        'olgo aqui ?',
        'olgo aqui ?',
        'olgo aqui ?',
        'olgo aqui ?',
    ]

    # Verificar se a pergunta atual está definida na sessão
    if 'pergunta_atual' not in request.session:
        # Definir a pergunta atual como 0 e criar um dicionário para armazenar as respostas
        request.session['pergunta_atual'] = 0
        request.session['respostas'] = {}

    # Obter a pergunta atual da sessão
    pergunta_atual = request.session['pergunta_atual']

    # Renderizar a página com a pergunta atual e suas alternativas
    return render(request, 'quest_usuario.html', {'pergunta': perguntas[pergunta_atual],'alternativas':alternativas})



# from django.shortcuts import render, redirect
# from .models import Question, Answer
# from .forms import QuestionForm

# def questionnaire(request):
#     questions = Question.objects.all()
#     current_question = questions.first()
#     answers = []

#     if request.method == 'POST':
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             answer = form.save(commit=False)
#             answer.question = current_question
#             answer.save()
#             answers.append(answer)
#             current_question = current_question.get_next_question()
#             if not current_question:
#                 return redirect('questionnaire_results')
#     else:
#         form = QuestionForm()

#     return render(request, 'questionnaire.html', {
#         'form': form,
#         'current_question': current_question,
#         'answers': answers,
#     })