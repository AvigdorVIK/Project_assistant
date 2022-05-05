from django.shortcuts import render



def index (request):
    return render(request, 'to_doo/index.html')
