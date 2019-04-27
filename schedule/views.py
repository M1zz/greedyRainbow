from django.http import request
from django.shortcuts import render

# Create your views here.
from schedule.models import Tasks


def select_schedule(request):
    name = "hyunho"
    col = [i for i in range(0, 1488)]
    row = [i for i in range(0, 7)]
    return render(request, 'greedyRainbow/index.html', {'name': name, 'col': col, 'row': row})


def insert_to_db(self, task):
    username = "hyunho"
    start_time = '2019-04-16 10:00'
    end_time = '2019-04-16 13:00'
    t = Tasks(username=username, task_start=start_time, task_end=end_time)
    t.save()
