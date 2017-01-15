from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from survey import models, forms
from django.contrib.auth import authenticate


def main(request):
    """
    Handles the root url

    :param request:
    :return:
    """

    if request.user.is_authenticated:
        return redirect("question")
    else:
        return redirect("login")


def login(request):
    """
    Handles loading the login page and authenticating the user

    :param request:
    :return:
    """

    if request.method == "GET":
        # Load login page
        return render(request, "login.html", {"user_form": forms.UserForm()})

    elif request.method == "POST":
        login_data = request.POST
        # Authenticate user with Django"s built in authentication
        user = authenticate(
            username=login_data.get("username"),
            password=login_data.get("password")
        )

        if user is not None:
            return redirect("question")
        else:
            return render(request, "login.html", {
                "user_form": forms.UserForm(),
                "error": "Incorrect username or password"
            })


def register(request):
    """
    View for loading the registration page and adding a registered user

    :param request:
    :return:
    """

    if request.method == "GET":
        # load the registration page
        user_form = forms.UserForm()
        return render(request, "register.html", {"user_form": user_form})

    elif request.method == "POST":
        data = request.POST
        user_form = forms.UserForm(data)

        # Validate and save the user
        if user_form.is_valid():
            user_data = user_form.cleaned_data

            user = models.User()

            user.username = user_data.get("username")
            user.email = user_data.get("email")
            user.first_name = user_data.get("first_name")
            user.last_name = user_data.get("last_name")
            user.set_password(user_data.get("password"))

            user.save()

            return redirect("login")
        else:
            return render(request, "register.html", {"errors": user_form.errors})


def question(request):
    """
    View to query for a new question the user has not answered yet

    :param request:
    :return:
    """

    return render(request, "question.html")