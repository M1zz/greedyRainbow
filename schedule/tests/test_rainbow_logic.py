import schedule.scheduler.controller as controller
from schedule.tests.BaseTestCase import BaseTestCase

user = "hyunho"


class LogicTest(BaseTestCase):

    def test_일정길이(self):
        # Given
        single_task = ["2019-04-16 09:30", "2019-04-16 10:30"]
        c = controller.Controller()
        expected = 60

        # When
        time_length = c.get_time_length(single_task)

        # Then
        self.assertEqual(time_length, expected)

    def test_스케쥴_검색(self):
        # Given
        # userdata =

        # When

        # Then

        self.assertEqual(0, 1)

    def test_스케쥴_삽입가능(self):
        # Given
        user_data = ["hyunho", 0, ["2019-04-16 09:30", "2019-04-16 10:30"], ["2019-04-16 13:00", "2019-04-16 15:00"]]
        insert_data = ["2019-04-16 11:00", "2019-04-16 12:00"]
        expected = True
        c = controller.Controller()

        # When
        result = c.is_task_insert_able(user_data, insert_data)

        # Then
        self.assertEqual(result, expected)

    def test_스케쥴_삽입_불가능(self):
        # Given
        user_data = ['hyunho', 0, ['2019-04-16 10:00', '2019-04-16 12:00'], ['2019-04-16 13:00', '2019-04-16 15:00']]
        insert_data = ['2019-04-16 09:30', '2019-04-16 10:30']
        expected = False
        c = controller.Controller()

        # When
        result = c.is_task_insert_able(user_data, insert_data)

        # Then
        self.assertEqual(result, expected)

    def test_스케쥴_삽입_처음(self):
        # Given
        user_data = []
        insert_data = ["2019-04-16 11:00", "2019-04-16 12:00"]
        expected = [["hyunho", 0, ["2019-04-16 11:00", "2019-04-16 12:00"]]]
        c = controller.Controller()

        # When
        result = c.insert(user_data, insert_data)

        # Then
        self.assertEqual(result, expected)

    def test_스케쥴_삽입_1번째_줄(self):
        # Given
        user_data = [["hyunho", 0, ["2019-04-16 09:30", "2019-04-16 10:30"], ["2019-04-16 13:00", "2019-04-16 15:00"]]]
        insert_data = ["2019-04-16 11:00", "2019-04-16 12:00"]
        expected = [["hyunho", 0, ["2019-04-16 09:30", "2019-04-16 10:30"], ["2019-04-16 13:00", "2019-04-16 15:00"],
                     ["2019-04-16 11:00", "2019-04-16 12:00"]]]
        temp = [['hyunho', 0, ['2019-04-16 10:00', '2019-04-16 12:00'], ['2019-04-16 13:00', '2019-04-16 15:00']]]
        c = controller.Controller()

        # When
        result = c.insert(user_data, insert_data)

        # Then
        self.assertCountEqual(result[0], expected[0])

    def test_스케쥴_삽입_2번째_줄(self):
        # Given
        user_data = [["hyunho", 0, ["2019-04-16 09:30", "2019-04-16 10:30"], ["2019-04-16 13:00", "2019-04-16 15:00"]]]
        insert_data = ["2019-04-16 10:00", "2019-04-16 12:00"]
        expected = [["hyunho", 0, ["2019-04-16 10:00", "2019-04-16 12:00"], ["2019-04-16 13:00", "2019-04-16 15:00"]],
                    ["hyunho", 1, ["2019-04-16 09:30", "2019-04-16 10:30"]]]
        c = controller.Controller()

        # When
        result = c.insert(user_data, insert_data)
        # Then
        self.assertCountEqual(result, expected)

    def test_스케쥴_삽입_긴_줄(self):
        # Given
        user_data = [["hyunho", 0, ["2019-04-16 09:30", "2019-04-16 10:30"], ["2019-04-16 13:00", "2019-04-16 15:00"]],
                     ["hyunho", 1, ["2019-04-16 10:00", "2019-04-16 12:00"]]]
        insert_data = ["2019-04-16 01:00", "2019-04-16 23:00"]
        expected = [["hyunho", 0, ["2019-04-16 01:00", "2019-04-16 23:00"]],
                    ["hyunho", 1, ["2019-04-16 10:00", "2019-04-16 12:00"], ["2019-04-16 13:00", "2019-04-16 15:00"]],
                    ["hyunho", 2, ["2019-04-16 09:30", "2019-04-16 10:30"]]]
        c = controller.Controller()

        # When
        result = c.insert(user_data, insert_data)

        print("expected", expected)
        print("result", result)

        # Then
        self.assertCountEqual(result[0], expected[0])
        self.assertCountEqual(result[1], expected[1])
        self.assertCountEqual(result[2], expected[2])

    def test_스케쥴_수정_1째줄(self):
        # Given
        user_data = [["hyunho", 0, ["2019-04-16 09:30", "2019-04-16 10:30"], ["2019-04-16 13:00", "2019-04-16 15:00"]],
                     ["hyunho", 1, ["2019-04-16 10:00", "2019-04-16 12:00"]]]
        origin_data = ["2019-04-16 09:30", "2019-04-16 10:30"]
        update_data = ["2019-04-16 09:30", "2019-04-16 11:30"]
        expected = [["hyunho", 0, ["2019-04-16 09:30", "2019-04-16 11:30"], ["2019-04-16 13:00", "2019-04-16 15:00"]],
                    ["hyunho", 1, ["2019-04-16 10:00", "2019-04-16 12:00"]]]
        c = controller.Controller()

        # When
        result = c.update(user_data, origin_data, update_data)

        # Then
        self.assertCountEqual(result[0], expected[0])

    def test_스케쥴_수정_2째줄로(self):  # Given
        # Given
        user_data = [["hyunho", 0, ["2019-04-16 09:30", "2019-04-16 10:30"], ["2019-04-16 13:00", "2019-04-16 15:00"]],
                     ["hyunho", 1, ["2019-04-16 10:00", "2019-04-16 12:00"]]]
        origin_task = ["2019-04-16 09:30", "2019-04-16 10:30"]
        update_task = ["2019-04-16 09:30", "2019-04-16 15:30"]
        expected = [["hyunho", 0, ["2019-04-16 09:30", "2019-04-16 15:30"]],
                    ["hyunho", 1, ["2019-04-16 10:00", "2019-04-16 12:00"], ["2019-04-16 13:00", "2019-04-16 15:00"]]]
        c = controller.Controller()

        # When
        result = c.update(user_data, origin_task, update_task)

        print(result)
        print(expected)
        # Then
        self.assertCountEqual(result[0], expected[0])
        self.assertCountEqual(result[1], expected[1])

    def test_일정_삭제(self):
        # Given
        user_data = [["hyunho", 0, ["2019-04-16 09:30", "2019-04-16 10:30"], ["2019-04-16 13:00", "2019-04-16 15:00"]],
                     ["hyunho", 1, ["2019-04-16 10:00", "2019-04-16 12:00"]]]
        remove_target_task = ["2019-04-16 09:30", "2019-04-16 10:30"]
        expected = [["hyunho", 0, ["2019-04-16 13:00", "2019-04-16 15:00"]],
                    ["hyunho", 1, ["2019-04-16 10:00", "2019-04-16 12:00"]]]
        c = controller.Controller()
        # When
        result = c.remove_task(user_data, remove_target_task)

        # Then
        self.assertEqual(result, expected)

    def test_스케쥴_삭제(self):
        self.assertEqual(0, 1)


'''
    def test_일정_정렬_라인(self):
        # Given
        unsorted_task = ['hyunho', 0, ['2019-04-16 13:00', '2019-04-16 15:00'], ['2019-04-16 09:30', '2019-04-16 11:30']]
        expected = ['hyunho', 0, ['2019-04-16 09:30', '2019-04-16 11:30'],['2019-04-16 13:00', '2019-04-16 15:00']]
        c = controller.Controller()

        # When
        result = c.sort_task(unsorted_task)

        # Then
        self.assertEqual(expected, result)
'''
