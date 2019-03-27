from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    fileinput = forms.ImageField()
    class Meta:
        model = User
        fields = ['email','fileinput','password1','password2']
    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data["email"]
        user.email = self.cleaned_data["email"]
        user.fileinput = self.cleaned_data["fileinput"]
        print(user.fileinput)
        if commit:
            user.save()
        return user

