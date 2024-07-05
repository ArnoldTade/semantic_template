from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Employee


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            classes = "ui input"
            if field.widget.__class__.__name__ == "Select":
                classes = "ui dropdown"

            field.widget.attrs.update(
                {
                    "class": classes,
                    "placeholder": f"Enter your {field.label}",
                    "style": "width: auto; display: inline-block;",
                }
            )
        self.fields["birthDate"].widget = forms.DateInput(
            attrs={
                "class": "ui input",
                "placholder": "Enter date of birth",
                "type": "date",
                "style": "width: auto; display: inline-block;",
            }
        )
