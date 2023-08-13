from django.shortcuts import render

def register(request):
    context = {
        'title':'Регистрация'
    }
    return render(request, 'register/register.html', context)
