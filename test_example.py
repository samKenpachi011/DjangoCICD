from django.test import TestCase


class Mytest(TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def add(self, a, b):
        return a + b

    def test_add(self):
        assert self.add(2, 3) == 5
        assert self.add('space', 'ship') == 'spaceship'
