from django.test import TestCase

class BaseTestCase(TestCase):

    def assertHasAnyType(self, arr, cls):
        self.assertTrue(any([isinstance(item, cls) for item in arr]))