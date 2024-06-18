from django import forms
from .models import task

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class":"myinput", "placeholder": "Add new"}))
    class Meta:
        model = task
        fields = ["title"]