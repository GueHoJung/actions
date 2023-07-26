# LoginCrmApiAdapter.login_crm_api() 메쏘드를 호출하는 테스트 코드입니다.
from django.test import TestCase
from django.conf import settings

from designer_server.adapter.out.login_crm_api_adapter import LoginCrmApiAdapter


class AdapterTest(TestCase):

    # setUpTestData() 는 클래스 전체에서 사용되는 설정을 위해서 테스트 시작 때 딱 한 번만 실행됩니다.
    # 테스트 메쏘드가 실행되면서 수정되거나 변경되지 않을 객체들을 이곳에서 생성할 수 있습니다.
    @classmethod
    def setUpTestData(cls):
        print(f"{cls.__name__} setUpTestData: Run once to set up non-modified data for all class methods.")

        # cls.crmAdapter = LoginCrmApiAdapter()

    def setUp(self):
        print(f"{self.__class__.__name__} setUp: Run once for every test method to setup clean data.")
        self.json = {
            "cpId": "JN",
            "system": "CRM",
            "userId": "juno11273",
            "password": "e4f3f6f18e26b69acc799adf12b75957ab18b699b613a277280b8dc6764be90aa2750ad616477880ade169b4b883bad5e97b22d3a59c15f21b629fcf769b023c",
            "client": "PC"
        }
        self.API_HOST = getattr(settings, "CRM_HOST_IP", None)
        self.API_PORT = getattr(settings, "CRM_HOST_PORT", None)
        self.API_ADR = self.API_HOST + ":" + self.API_PORT
        print(f"Api adr ==> {self.API_ADR}")

    # def test_adapter(self):
    #     print(f"{self.__class__.__name__} test_adapter: exec")
    #     self.crmAdapter.login_crm_api(self.API_ADR, "/login/login/", "POST", self.json)
