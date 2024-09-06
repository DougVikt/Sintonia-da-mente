from django.shortcuts import render

# Create your views here.
def quest(request):
    return render(request, 'questinario.html') 


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