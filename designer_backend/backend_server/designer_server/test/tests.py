# Test case for DesignerTest model
from designer_server.models import DesignerTest

from django.test import TestCase


# Create your tests here.
class DesignerTestTestCase(TestCase):
    """
    Test case for DesignerTest model
    """

    # setUpTestData() 는 클래스 전체에서 사용되는 설정을 위해서 테스트 시작 때 딱 한 번만 실행됩니다.
    # 테스트 메쏘드가 실행되면서 수정되거나 변경되지 않을 객체들을 이곳에서 생성할 수 있습니다.
    @classmethod
    def setUpTestData(cls):
        print(f"{cls.__name__} setUpTestData: Run once to set up non-modified data for all class methods.")
        DesignerTest.objects.create(id=1, name="test1")
        DesignerTest.objects.create(id=2, name="test2")

    # setUp() 은 각각의 테스트 메쏘드가 실행될 때마다 실행됩니다.
    # 테스트 중 내용이 변경될 수 있는 객체를 이곳에서 생성할 수 있습니다
    # (모든 테스트 메쏘드는 방금 막 생성된 ("fresh") 오브젝트를 입력받게 됩니다).
    def setUp(self):
        print(f"{self.__class__.__name__} setUp: Run once for every test method to setup clean data.")
        # DesignerTest.objects.create(id=1, name="test1")
        # DesignerTest.objects.create(id=2, name="test2")

    def test_designer_test(self):
        print(f"{self.__class__.__name__} test_designer_test: exec")
        test1 = DesignerTest.objects.get(name="test1")
        test2 = DesignerTest.objects.get(name="test2")
        self.assertEqual(test1.name, "test1")
        self.assertEqual(test2.name, "test2")
