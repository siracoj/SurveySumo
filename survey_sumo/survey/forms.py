from django import forms
from django.contrib.auth.models import User
from survey import models


class UserForm(forms.ModelForm):
    """
    Form used for validation on user creation
    """

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def clean(self):
        """
        Custom clean function to check if passwords match

        :return:
        """
        clean_data = super(UserForm, self).clean()
        if self.data.get('password') != self.data.get("password_confirm"):
            self.add_error("password", forms.ValidationError("Passwords do not match"))
