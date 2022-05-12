from django.shortcuts import render


def index (request):
    return render(request, 'to_doo/index.html')

def add_task (request):
    return render (request,  'to_doo/add_task.html')
