import datetime as dt

from django.http import request
from django.shortcuts import render

# Create your views here

from schedule.models import Tasks


def select_schedule(request):
    name = "hyunho"
    # col = [i for i in range(0, 1488)]
    start_point = '2019-04-16 00:00'
    end_point = '2019-04-17 00:00'

    pieces = schedule_devider(start_point, end_point)  # 48
    max_tasks = 7

    col = [i for i in range(0, pieces)]
    row = [i for i in range(0, max_tasks)]
    arr = [0] * max_tasks * pieces
    x = [i for i in range(0, max_tasks * pieces)]

    userdata = [["hyunho", 0, ["2019-04-16 10:00", "2019-04-16 12:00"], ["2019-04-16 13:00", "2019-04-16 15:00"], ["2019-04-16 18:00", "2019-04-16 22:30"]],
                ["hyunho", 1, ["2019-04-16 09:30", "2019-04-16 10:30"]]]

    task_data = []

    for line in userdata:
        line_info = line[1]
        data = line[2:]
        task = []
        for item in data:
            task = []
            task.append(schedule_position(start_point, item[0], line_info, pieces))
            task.append(schedule_position(start_point, item[1], line_info, pieces))
            task_data.append(task)

    for task in task_data:
        for item in range(0, len(arr)):
            if task[0] <= item < task[1]:
                arr[item] = 1

    arr = schedule_transform(arr, pieces)

    return render(request, 'greedyRainbow/index.html',
                  {'name': name, 'pieces': pieces, 'col': col, 'row': row,
                   'task_data': task_data, 'arr': arr})


def schedule_devider(start_point, end_point):
    fmt = "%Y-%m-%d %H:%M"

    start = dt.datetime.strptime(start_point, fmt)
    end = dt.datetime.strptime(end_point, fmt)

    pieces = (end - start).total_seconds() / 60 / 60 * 2  # end_point - start_point

    return int(pieces)


def schedule_position(start_standard, start_point, line_num, pieces):
    fmt = "%Y-%m-%d %H:%M"

    start = dt.datetime.strptime(start_standard, fmt)
    end = dt.datetime.strptime(start_point, fmt)

    position = (end - start).total_seconds() / 60 / 60 * 2  # end_point - start_point
    position = position + line_num * pieces
    return int(position)


def schedule_transform(task_data, pieces):
    temp = task_data
    new_data = [0] * len(task_data)
    max_task = 7
    last_num = pieces * max_task - 1

    number = 0
    for item in range(0, max_task):
        for i in range(pieces - 1, -1, -1):
            new_data[last_num - i] = temp[number]
            number += 1
        last_num -= pieces

    task_data = new_data

    return task_data


def insert_to_db(self, task):
    username = "hyunho"
    start_time = '2019-04-16 10:00'
    end_time = '2019-04-16 13:00'

    t = Tasks(username=username, task_start=start_time, task_end=end_time)
    t.save()
