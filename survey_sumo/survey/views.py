from django.shortcuts import render, render_to_response




def login(request):

    if request.method == 'GET':

        return render_to_response('login.html')