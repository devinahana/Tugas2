from socket import fromshare
from django import forms

class TaskForm(forms.Form):
    task_title = forms.CharField()
    task_description = forms.CharField()