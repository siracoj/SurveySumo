from django.shortcuts import Http404, redirect, render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from survey import models, forms
from django.contrib.auth import authenticate, logout, login
import random


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


def login_user(request):
    """
    Handles loading the login page and authenticating the user

    :param request:
    :return:
    """

    if request.method == "GET":

        # Log out user if one is logged in already
        if request.user.is_authenticated:
            print "logging in"
            logout(request)

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
            login(request, user)
            return redirect("question")
        else:
            return render(request, "login.html", {
                "user_form": forms.UserForm(),
                "error": "Incorrect username or password"
            })

    return Http404()


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

    return Http404()


@login_required(login_url='login')
def question(request):
    """
    View to query for a new question the user has not answered yet

    :param request:
    :return:
    """
    if request.method == "GET":
        # Gets a set of all questions already answered
        answered_questions = set([a.question.id for a in models.Answer.objects.filter(user=request.user)])

        # Gets a question from a list of already answered questions
        question = random.choice(models.Question.objects.exclude(id__in=answered_questions))

        return render(request, "question.html", {"question": question})

    return Http404()


@staff_member_required()
def add_question(request):
    """
    View for admins to add questions

    :param request:
    :return:
    """

    if request.method == "GET":
        return render(request, "survey_admin/question_add.html")

    elif request.method == "POST":
        question_forms = forms.QuestionForm(request.POST)

        print request.POST

        if question_forms.is_valid():
            data = question_forms.cleaned_data

            question = models.Question()
            question.question = data.get("question")
            question.choices = request.POST.getlist("choice")

            question.save()

            return render(request, "survey_admin/question_add.html", {"message": "Question Saved!"})
        else:
            return render(request, "survey_admin/question_add.html", {"message": question_forms.errors})

    return Http404()


@staff_member_required()
def answers(request):
    """
    View to query for a new question the user has not answered yet

    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, "survey_admin/answer_view.html")
