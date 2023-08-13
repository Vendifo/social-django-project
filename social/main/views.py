from django.shortcuts import render

def main(request):
    context = {
        'title':'Главная'
    }
    return render(request, 'main/main.html', context)

def users(request):
    context = {
        'title':'Пользователи'
    }
    return render(request, 'main/users.html', context)

def dialogue(request):
    context = {
        'title':'Диалог'
    }
    return render(request, 'main/dialogue.html', context)

