from django.shortcuts import render, redirect

from to_doo.forms import *


def index (request):
    return render(request, 'to_doo/index.html')

def add_task (request):
    if request.method == 'POST':
        form = AddTasksForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                form.edd_error()
                return redirect(None, 'not valid')

    else:
        form = AddTasksForm()
    return render (request,  'to_doo/add_task.html', {'form': form})
