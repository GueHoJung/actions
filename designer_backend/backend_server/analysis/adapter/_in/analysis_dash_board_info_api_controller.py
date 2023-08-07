from dependency_injector.wiring import inject
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import APIView

from ...application.service.analysis_dash_board_info_service import AnalysisDashBoardInfoService
from ...serializers import PostRequestSerializer
import config.utils.common_utils as common_utils
from config.utils.decorator import check_token

from config.base_container import BaseContainer


class AnalysisDashBoardInfoApiController(APIView):
    """
    # CLASS : AnalysisDashBoardInfoApiController
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/31 4:56 PM
    # DESCRIPTION
        - AnalysisDashBoardInfoApiController
        - DashBoardInfo API
        - CRM 디렉터리 : analysis
        - CRM 서비스 설명 : 분석 대시보드
        - CRM 서비스 호출 url : /analysis/getDashBoardInfo/
        - CRM 서비스 호출 method : POST
        - CRM 서비스 호출 body : json
        - CRM 서비스 호출 파라미터 :

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/31          jung-gyuho          최초 생성
    """

    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(tags=['CRM SYSTEM - Analysis API'], operation_summary="CRM Analysis DashBoardInfo API",
                         operation_description="# DESIGNER SEVER에서 CRM SYSTEM으로 DashBoardInfo 요청 API\n"
                                               "\n"
                                               "|PARAM NAME|TYPE   |MAX LENGTH|DESC|REQUIRED|ETC     |\n"
                                               "|:--------:|:-----:|:--------:|:--:|:------:|:------:|\n"
                                               "|-      |varchar|20        |TRUE|-   |JN|\n"
                                               "\n"
                                               "### Data type : json\n"
                                               "```\n"
                                               "{\n"
                                               "    \"cpId\": \"**\",\n"
                                               "    \"shopId\": \"***\",\n"
                                               "    \"custId\": \"juno*****\",\n"
                                               "}",
                         request_body=PostRequestSerializer, responses={200: 'Success'})
    @inject
    @check_token
    def post(self, request, *args, **kwargs):
        """
        # API : post
        # AUTHOR : jung-gyuho
        # TIME : 2023/07/27 6:02 PM
        # DESCRIPTION
            - API NAME : DashBoardInfo API
            - API DESC : CRM DashBoardInfo 진입경로
                        ex) 분석 > 대시보드,비교분석,랭크 외 다른 메뉴로 진입 > 하단 비중분석에 항목 클릭 > 하단에 오더목록 > 고객명 클릭
            - API METHOD : POST
            - REQUEST PARAMS : 없음
                (파라미터 이름, 타입, 최대길이, 설명, 필수여부, 비고)
                (ex/ cpId, varchar, 20, 조직ID, TRUE, 주노헤어=JN)
                |PARAM NAME|TYPE   |MAX LENGTH|DESC|REQUIRED|ETC     |
                |:--------:|:-----:|:--------:|:--:|:------:|:------:|
                |cpID      |varchar|20        |TRUE|기업아이디   |주노헤어=JN|
                |shopId    |varchar|20        |TRUE|매장아이디   |아무개=1234123|
                |custId    |varchar|20        |TRUE|고객아이디   |A매장=7|

                -SAMPLE JSON
                ```
                {
                    "cpId": "JN",
                    "loginShopId": "149",
                    "loginId": "11273",
                    "path": "/crm/anlys/anlys-dash-board",
                    "name": "anlys-dash-board",
                    "standard": "multi",
                    "dvsn": "all",
                    "shopNm": "",
                    "shopId": "",
                    "shopList": "'1','10','100','101','102','103','104','105','106','107','108','109','11','110','111','112','12','128','129','13','130','131','132','133','134','135','136','137','139','14','140','141','142','143','144','147','148','149','15','150','151','152','153','154','155','156','157','158','159','16','160','161','162','163','164','165','166','167','168','169','170','171','172','173','174','175','176','177','178','179','18','180','181','182','183','184','185','186','187','188','189','19','190','191','192','193','194','195','196','197','198','199','2','20','200','201','202','203','204','205','206','207','208','209','21','210','211','212','213','214','215','216','217','218','219','22','220','221','222','223','224','23','24','25','26','27','28','29','3','30','31','32','33','34','35','36','37','38','39','4','40','41','42','43','44','45','46','47','48','5','51','52','54','55','56','57','58','59','6','60','61','62','63','64','65','66','67','68','69','7','70','71','72','73','74','75','76','77','78','79','8','80','81','82','83','84','85','86','87','88','89','9','90','91','94','999'",
                    "term": "month",
                    "searchDt": "202307",
                    "searchStDt": "202304",
                    "searchEdDt": "202307"
                }

                ```
            - RESPONSE OBJECTS : JSON
                (파라미터 이름, 타입, 최대길이, 설명, 필수여부, 비고)
                (ex/ code, varchar, 100, 결과 코드, TRUE, -)
                |PARAM NAME|TYPE|MAX LENGTH|DESC|REQUIRED|ETC|
                |:---:|:---:|:---:|:---:|:---:|:---:|
                |code|varchar|100|결과 코드|TRUE| - |
                - SAMPLE JSON :
                ```

                ```
        """

        # token 관리
        kwargs = common_utils.manage_tokens(self, kwargs=kwargs, request=request)

        print(f"{self.__class__.__name__} : Controller post get request.data ==> {request.data}")

        container = BaseContainer()
        service: AnalysisDashBoardInfoService = container.analysisDashBoardInfoCrmServiceProvider()

        try:
            result = service.analysis_dash_board_info_crm(request.data, accessToken=kwargs.get('accessToken', 'None'),
                                                     refreshToken=kwargs.get('refreshToken', 'None'))
        except Exception as ex:
            print(f"{self.__class__.__name__} : Controller post error ==> {ex}")
            return Response(ex.__dict__, status=500)

        return Response(result, status=200)
        # return Response({"result": "CRM CONTROLLER GENERATE TEST"}, status=200)
