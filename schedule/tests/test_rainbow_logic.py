import schedule.scheduler.controller as controller
from schedule.tests.BaseTestCase import BaseTestCase




class LogicTest(BaseTestCase):
    def test_스케쥴_삽입가능(self):
        # Given
        insert_data = ["11:00","12:00"]

        # When
        user_data = ['hyunho', "2019", "4", "16", ["09:30", "10:30"], ["13:00", "15:00"]]

        # Then
        result = controller.isInsertable(user_data,insert_data)
        self.assertEqual(result, True)
