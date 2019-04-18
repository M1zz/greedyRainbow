import schedule.scheduler.controller as controller
from schedule.tests.BaseTestCase import BaseTestCase

user = "hyunho"


class LogicTest(BaseTestCase):

    def test_스케쥴_입력(self):
        self.assertEqual(0, 1)

    def test_스케쥴_삽입가능(self):
        # Given
        user_data = [user, 0, ["2019-04-16 09:30", "2019-04-16 10:30"], ["2019-04-16 13:00", "2019-04-16 15:00"]]
        insert_data = ["2019-04-16 11:00", "2019-04-16 12:00"]
        expected = True
        c = controller.Controller()

        # When
        result = c.is_insert_able(user_data, insert_data)

        # Then
        self.assertEqual(result, expected)

    def test_스케쥴_삽입_1번째_줄(self):
        # Given
        user_data = [user, 0, ["2019-04-16 09:30", "2019-04-16 10:30"], ["2019-04-16 13:00", "2019-04-16 15:00"]]
        insert_data = ["2019-04-16 11:00", "2019-04-16 12:00"]
        expected = [user, 0, ["2019-04-16 09:30", "2019-04-16 10:30"], ["2019-04-16 13:00", "2019-04-16 15:00"],
                    ["2019-04-16 11:00", "2019-04-16 12:00"]]
        c = controller.Controller()

        # When
        result = c.insert(user_data, insert_data)

        # Then
        self.assertEqual(result, expected)

    def test_스케쥴_삽입_다음_줄(self):
        # Given
        user_data = [user, 0, ["2019-04-16 09:30", "2019-04-16 10:30"], ["2019-04-16 13:00", "2019-04-16 15:00"]]
        insert_data = ["2019-04-16 10:00", "2019-04-16 12:00"]
        expected = [user, 1, ["2019-04-16 10:00", "2019-04-16 12:00"]]
        c = controller.Controller()

        # When
        result = c.insert(user_data, insert_data)

        # Then
        self.assertEqual(result, expected)

    def test_스케쥴_수정(self):
        self.assertEqual(0, 1)
