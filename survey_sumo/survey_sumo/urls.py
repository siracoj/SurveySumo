"""survey_sumo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r"^$", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r"^$", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r"^blog/", include("blog.urls"))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from survey import views

urlpatterns = [
    url(r"^$", views.main, name="main"),
    url(r"^admin/", admin.site.urls, name="admin"),
    url(r"^login/$", views.login_user, name="login"),
    url(r"^question/$", views.question, name="question"),
    url(r"^register/$", views.register, name="register"),
    url(r"^question/add/$", views.add_question, name="question_add"),
    url(r"^answers/$", views.answers, name="answers"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

