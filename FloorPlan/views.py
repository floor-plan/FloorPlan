from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def project(request, pk):
    pass
    # return render(request, "core/project.html", {'deck': deck, 'cards': cards, 'pk': pk})

