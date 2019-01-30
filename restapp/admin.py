from django.contrib import admin
from django.db import models

# Register your models here.
from restapp.models import Task

admin.site.register(Task)


