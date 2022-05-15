from django import forms
from .models import *

class AddTasksForm (forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'content', 'cat' ]

