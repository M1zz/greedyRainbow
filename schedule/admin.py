from django.contrib import admin

# Register your models here.
from schedule.models import Task

admin.site.register(Task)