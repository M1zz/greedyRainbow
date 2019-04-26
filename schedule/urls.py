

from django.http import HttpResponse
from django.urls import path

from schedule import views
from schedule.scheduler import controller

urlpatterns = [
    path('ping', lambda r: HttpResponse('OK')),
    path('', views.select_schedule),
    #path('insert', controller.Controller.),
]