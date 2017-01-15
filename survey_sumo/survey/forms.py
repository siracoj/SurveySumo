from django import forms
from django.contrib.auth.models import User
from survey import models


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def clean(self):
        clean_data = super(UserForm, self).clean()
        if clean_data.get('password') != clean_data.get("password_confirm"):
            raise forms.ValidationError("Passwords do not match")
