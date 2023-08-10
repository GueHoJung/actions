from dependency_injector.wiring import inject
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import APIView

from ...application.service.stats_daily_sales_user_performance_service import StatsDailySalesUserPerformanceService
from ...serializers import PostRequestSerializer
import config.utils.common_utils as common_utils
from config.utils.decorator import check_token

from config.base_container import BaseContainer


class StatsDailySalesUserPerformanceApiController(APIView):
    """
    # CLASS : StatsDailySalesUserPerformanceApiController
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/31 5:58 PM
    # DESCRIPTION
        - StatsDailySalesUserPerformanceApiController
        - DailySalesUserPerformance API
        - CRM 디렉터리 : stats
        - CRM 서비스 설명 : 통계 디자이너 매출조회 매출일보
        - CRM 서비스 호출 url : /stats/getDailySalesUserPerformance/
        - CRM 서비스 호출 method : POST
        - CRM 서비스 호출 body : json
        - CRM 서비스 호출 파라미터 :
            cpId (기업아이디)
            shopId (매장아이디)
            searchStDt (조회시작일)
            searchEdDt (조회종료일)
            term (월 / 일 => month / day)
            salesUserId (디자이너아이디)
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/31          jung-gyuho          최초 생성
    """

    # permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(tags=['CRM SYSTEM - Stats API'], operation_summary="CRM Stats DailySalesUserPerformance API",
                         operation_description="# DESIGNER SEVER에서 CRM SYSTEM으로 DailySalesUserPerformance 요청 API\n"
                                               "\n"
                                               "|PARAM NAME|TYPE   |MAX LENGTH|DESC|REQUIRED|ETC     |\n"
                                               "|:--------:|:-----:|:--------:|:--:|:------:|:------:|\n"
                                               "|cpID      |varchar|20        |TRUE|기업아이디   |JN|\n"
                                               "|shopId    |varchar|20        |TRUE|매장아이디   |1801141|\n"
                                               "|searchStDt    |varchar|20        |TRUE|조회시작일   |PR000000001801141D001|\n"
                                               "|searchEdDt    |varchar|20        |TRUE|조회종료일   |20200801|\n"
                                               "|term    |varchar|20        |TRUE|월 / 일 => month / day   |20220801|\n"
                                               "|salesUserId    |varchar|20        |TRUE|디자이너아이디   |\"\"|\n"
                                               "\n"
                                               "### Data type : json\n"
                                               "```\n"
                                               "{\n"
                                               "    \"cpId\": \"**\",\n"
                                               "    \"shopId\": \"***\",\n"
                                               "    \"searchStDt\": \"juno*****\",\n"
                                               "    \"searchEdDt\": \"juno*****\",\n"
                                               "    \"term\": \"juno*****\",\n"
                                               "    \"salesUserId\": \"juno*****\",\n"
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
            - API NAME : DailySalesUserPerformance API
            - API DESC : CRM DailySalesUserPerformance 진입경로
                        ex) 분석 > 대시보드,비교분석,랭크 외 다른 메뉴로 진입 > 하단 비중분석에 항목 클릭 > 하단에 오더목록 > 고객명 클릭
            - API METHOD : POST
            - REQUEST PARAMS :
                (파라미터 이름, 타입, 최대길이, 설명, 필수여부, 비고)
                (ex/ cpId, varchar, 20, 조직ID, TRUE, 주노헤어=JN)
                |PARAM NAME|TYPE   |MAX LENGTH|DESC|REQUIRED|ETC     |
                |:--------:|:-----:|:--------:|:--:|:------:|:------:|
                |cpID      |varchar|20        |TRUE|기업아이디   |주노헤어=JN|
                |shopId    |varchar|20        |TRUE|매장아이디   |아무개=1234123|
                |searchStDt    |varchar|20        |TRUE|조회시작일   |A매장=7|
                |searchEdDt    |varchar|20        |TRUE|조회종료일   |A매장=7|
                |term    |varchar|20        |TRUE|월 / 일 => month / day   |A매장=7|
                |salesUserId    |varchar|20        |TRUE|디자이너아이디   |A매장=7|

                -SAMPLE JSON
                ```
                {
                    "cpId": "JN",
                    "shopId": "149",
                    "searchStDt": "20220801",
                    "searchEdDt": "20220831",
                    "term": "day",
                    "salesUserId": ""
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
        service: StatsDailySalesUserPerformanceService = container.statsDailySalesUserPerformanceCrmServiceProvider()

        try:
            result = service.stats_daily_sales_user_performance_crm(request.data, accessToken=kwargs.get('accessToken', 'None'),
                                                     refreshToken=kwargs.get('refreshToken', 'None'))
        except Exception as ex:
            print(f"{self.__class__.__name__} : Controller post error ==> {ex}")
            return Response(ex.__dict__, status=500)

        return Response(result, status=200)
        # return Response({"result": "CRM CONTROLLER GENERATE TEST"}, status=200)
