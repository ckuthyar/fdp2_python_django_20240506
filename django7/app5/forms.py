from django import forms
from app5.models import students

class studentform1(forms.ModelForm):
    class Meta:
        model=students
        fields=['name1','college1','course1']