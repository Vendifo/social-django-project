from django.shortcuts import render



def dialogue(request):
    context = {
        'title':'Диалог'
    }
    return render(request, 'dialogue/dialogue.html', context)