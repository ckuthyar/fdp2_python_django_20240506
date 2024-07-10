from django import forms

class inputweb(forms.Form):
    city1=forms.CharField(max_length=3,label="Enter City")
