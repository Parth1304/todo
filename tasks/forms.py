# forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))
    
   
    complete = forms.BooleanField(
        label='Complete', 
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'checkbox'})
    )

    class Meta:
        model = Task
        fields = '__all__'
    