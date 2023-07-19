from django.test import TestCase
from .models import DesignerTest

# Create your tests here.
class DesignerTestTestCase(TestCase):
    def setUp(self):
        DesignerTest.objects.create(id=1, name="test1")
        DesignerTest.objects.create(id=2, name="test2")

    def test_designer_test(self):
        test1 = DesignerTest.objects.get(name="test1")
        test2 = DesignerTest.objects.get(name="test2")
        self.assertEqual(test1.name, "test1")
        self.assertEqual(test2.name, "test2")
