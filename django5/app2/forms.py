from django import forms
from app2.models import icici

class iciciform(forms.ModelForm):
    class Meta:
        model=icici
        fields='__all__'
