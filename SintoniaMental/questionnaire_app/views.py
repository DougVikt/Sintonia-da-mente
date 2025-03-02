from django.shortcuts import render


def quest(request):
    return render(request, 'pages_quest/quest_screening.html') 


def quest_user(request):
    return render(request, 'pages_quest/quest_user.html')


def quest_parent(request):
    return render(request,'pages_quest/quest_parent.html' )


def quest_teacher(request):
    return render(request,'pages_quest/quest_teacher.html' )


def end_result(request):
    return render(request,'pages_quest/end_result.html')