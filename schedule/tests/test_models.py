import schedule.scheduler.controller as controller
from schedule.tests.BaseTestCase import BaseTestCase
from schedule.models import Task

user = "hyunho"


class ModelTest(BaseTestCase):
    def test_테스크_삽입(self):
        # Given
        username = "hyunho"
        start_time = '2019-04-16 10:00'
        end_time = '2019-04-16 13:00'
        task = [start_time,end_time]
        c = controller.Controller()

        # When
        c.insert_to_db(task)

        # Then
        t = Task.objects.get(username=username)
        print(t.username, t.task_start, t.task_end)
        self.assertEqual(t.username,"hyunho")
        self.assertEqual(t.task_start,'2019-04-16 10:00')
        self.assertEqual(t.end_time, '2019-04-16 13:00')


