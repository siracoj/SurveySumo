from django.contrib import admin
from survey import models
# Register your models here.

admin.site.register(models.Question)
admin.site.register(models.Answer)
