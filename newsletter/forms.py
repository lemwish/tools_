from django import forms
from .models import SignUp


class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['email', 'full_name', ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split('@')
        domain, extension = provider.split('.')
        if not extension == 'edu':
            raise forms.ValidationError("please use a valid .EDU email address")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name")
        if len(full_name) <= 3:
            raise forms.ValidationError("Make sure your name is longer than 3 characters")
        return full_name










