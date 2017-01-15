from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from survey import models, forms

def main(request):
    """
    Handles the root url

    :param request:
    :return:
    """

    if request.user.is_authenticated:
        return redirect('question')
    else:
        return redirect('login')


def login(request):
    """
    Handles loading the login page and authenticating the user

    :param request:
    :return:
    """

    if request.method == 'GET':

        return render(request, 'login.html', {'user_form': forms.UserForm()})


def register(request):
    """
    View for loading the registration page and adding a registered user

    :param request:
    :return:
    """

    if request.method == 'GET':
        # load the registration page
        user_form = forms.UserForm()
        return render(request, 'register.html')

    elif request.method == 'POST':
        data = request.POST
        user_form = forms.UserForm(data)

        # Validate and save the user
        if user_form.is_valid():
            user_form.save(commit=True)
            return redirect('login')
        else:
            return render(request, 'register.html', {'errors': user_form.errors})



def question(request):
    """
    View to query for a new question the user has not answered yet

    :param request:
    :return:
    """