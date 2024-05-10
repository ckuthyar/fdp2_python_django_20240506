from django import forms
from .models import students
class inputform(forms.ModelForm):
    class Meta:
        model=students
        fields=['name1','college1','course1']