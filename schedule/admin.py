from django.contrib import admin

# Register your models here.
from schedule.models import Tasks

admin.site.register(Tasks)