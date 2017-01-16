from django import forms
from survey import models


class UserForm(forms.ModelForm):
    """
    Form used for validation on user creation
    """

    class Meta:
        model = models.User
        fields = ["username", "first_name", "last_name", "email", "password"]

    def clean(self):
        """
        Custom clean function to check if passwords match

        :return:
        """
        clean_data = super(UserForm, self).clean()
        if self.data.get("password") != self.data.get("password_confirm"):
            self.add_error("password", forms.ValidationError("Passwords do not match"))


class QuestionForm(forms.ModelForm):
    """
    Form to clean/validate question creation
    """

    class Meta:
        model = models.Question
        fields = ["question"]

    def clean(self):
        """
        Custom clean function to check if passwords match

        :return:
        """
        clean_data = super(QuestionForm, self).clean()
        if len(self.data.getlist("choice")) < 1:
            self.add_error("Choices", forms.ValidationError("Questions need at least 1 choice"))
