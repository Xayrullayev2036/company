from django import forms

from branch.models import Branch


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "manager": forms.TextInput(attrs={"class": "form-control"}),
            "branch_phone": forms.TextInput(attrs={"class": "form-control"}),
            "branch_email": forms.TextInput(attrs={"class": "form-control"}),
        }