from django import forms

from profession.models import Profession


class ProfessionForm(forms.ModelForm):
    class Meta:
        model = Profession
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "salary": forms.NumberInput(attrs={"class": "form-control"}),
        }
