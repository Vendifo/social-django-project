from django.shortcuts import render

def users(request):
    context = {
        'title':'Пользователи'
    }
    return render(request, 'users/users.html', context)
