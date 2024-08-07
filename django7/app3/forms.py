from django import forms
class inputform(forms.Form):
    num1=forms.IntegerField(min_value=2,max_value=100)