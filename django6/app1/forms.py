from django import forms
from app1.models import hdfc
class hdfcforms(forms.ModelForm):
    class Meta:
        model = hdfc
        fields = "__all__"