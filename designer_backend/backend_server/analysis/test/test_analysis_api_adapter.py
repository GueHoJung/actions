# AnalysisApiAdapter.login_crm_api() 메쏘드를 호출하는 테스트 코드입니다.
from django.test import TestCase
from django.conf import settings

from analysis.adapter.out.analysis_api_adapter import AnalysisApiAdapter

class AdapterTest(TestCase):

    # setUpTestData() 는 클래스 전체에서 사용되는 설정을 위해서 테스트 시작 때 딱 한 번만 실행됩니다.
    # 테스트 메쏘드가 실행되면서 수정되거나 변경되지 않을 객체들을 이곳에서 생성할 수 있습니다.
    @classmethod
    def setUpTestData(cls):
        print(f"{cls.__name__} setUpTestData: Run once to set up non-modified data for all class methods.")

        cls.apiAdapter = AnalysisApiAdapter()

    def setUp(self):
        print(f"{self.__class__.__name__} setUp: Run once for every test method to setup clean data.")
        self.json = {
                    "cpId": "JN",
                    "custId": "1916685",
                    "shopId": "1"
                    # ,
                    # "searchShop": "order"
                }
        self.API_HOST = getattr(settings, "CRM_HOST_IP", None)
        self.API_PORT = getattr(settings, "CRM_HOST_PORT", None)
        self.API_ADR = self.API_HOST + ":" + self.API_PORT
        print(f"Api adr ==> {self.API_ADR}")

    def test_adapter(self, *args, **kwargs):
        print(f"{self.__class__.__name__} test_adapter: exec")
        kwargs['accessToken'] = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjcElkIjoiSk4iLCJ1c2VySWQiOiIxMTI3MyIsImNsbnRUcENkIjoiUEMiLCJzeXN0bVRwQ2QiOiJDUk0iLCJpYXQiOjE2OTA1MDcxMTksImV4cCI6MTY5MDU1MDMxOX0.s-Bq-l8twUd_pQ1GXJEwV5XAu_hx6jS2KHu_6DRVTE0"
        kwargs['refreshToken'] = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjcElkIjoiSk4iLCJ1c2VySWQiOiIxMTI3MyIsImNsbnRUcENkIjoiUEMiLCJzeXN0bVRwQ2QiOiJDUk0iLCJpYXQiOjE2OTA1MDcxMTksImV4cCI6MTY5MDU5MzUxOX0.wJX-2__grxFH0HAKBgUso1hpAjn26Be0R9XFuK75LOE"
        self.apiAdapter.analysis_cust_detail_crm_api(self.API_ADR, "/analysis/getCustDetailAnlys/", "POST", self.json, accessToken=kwargs['accessToken'], refreshToken=kwargs['refreshToken'])
