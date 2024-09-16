from django.shortcuts import render
from .perg_alter import perguntas_usu , alternativas 



def quest(request):
    return render(request, 'questionario.html') 

def quest_user(request):
  
    context = {
        'perguntas': perguntas_usu,
        'alternativas': alternativas
    }
    return render(request, 'quest_usuario.html', context)





# from django.shortcuts import render, redirect
# from .models import Question, Answer
# from .forms import QuestionForm

# def questionnaire(request):
#     perguntas_usu = Question.objects.all()
#     current_question = perguntas_usu.first()
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