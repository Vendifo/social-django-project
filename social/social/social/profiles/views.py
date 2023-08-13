from django.shortcuts import render

def profiles(request):
    context = {
        'title':'Профиль'
    }
    return render(request, 'profiles/profile.html', context)
