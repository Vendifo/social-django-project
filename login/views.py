from django.shortcuts import render

def login(request):
    context = {
        'title':'Вход'
    }
    return render(request, 'login/login.html', context)
