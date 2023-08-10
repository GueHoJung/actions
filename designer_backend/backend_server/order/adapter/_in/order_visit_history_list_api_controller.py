from dependency_injector.wiring import inject
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import APIView

from ...application.service.order_visit_history_list_service import OrderVisitHistoryListService
from ...serializers import PostRequestSerializer
import config.utils.common_utils as common_utils
from config.utils.decorator import check_token

from config.base_container import BaseContainer


class OrderVisitHistoryListApiController(APIView):
    """
    # CLASS : OrderVisitHistoryListApiController
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/31 3:35 PM
    # DESCRIPTION
        - OrderVisitHistoryListApiController
        - VisitHistoryList API
        - CRM 디렉터리 : order
        - CRM 서비스 호출 url : /order/getOrderGridList/
        - CRM 서비스 호출 method : POST
        - CRM 서비스 호출 body : json
        - CRM 서비스 호출 파라미터 :
            cpId (기업아이디)
            shopId (매장아이디)
            custId (고객아이디)
            ordDt (오더일자)
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/31          jung-gyuho          최초 생성
    """

    # permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(tags=['CRM SYSTEM - Order API'], operation_summary="CRM Order VisitHistoryList API",
                         operation_description="# DESIGNER SEVER에서 CRM SYSTEM으로 VisitHistoryList 요청 API\n"
                                               "\n"
                                               "|PARAM NAME|TYPE   |MAX LENGTH|DESC|REQUIRED|ETC     |\n"
                                               "|:--------:|:-----:|:--------:|:--:|:------:|:------:|\n"
                                               "|cpID      |varchar|20        |TRUE|기업아이디   |JN|\n"
                                               "|shopId    |varchar|20        |TRUE|매장아이디   |20200801|\n"
                                               "|searchEdDt    |varchar|20        |TRUE|검색시작일   |20200801|\n"
                                               "|searchStDt    |varchar|20        |TRUE|검색종료일   |20200801|\n"
                                               "|ordMemo    |varchar|20        |TRUE|시술메모   |20200801|\n"
                                               "|custParam    |varchar|20        |TRUE|고객명/고객아이디   |PR000000001801141D001|\n"
                                               "|cpTelNo    |varchar|20        |TRUE|고객 전화번호   |1801141|\n"
                                               "|ordTpCd    |varchar|20        |TRUE|오더유형   |20200801|\n"
                                               "|itemGrpCd    |varchar|20        |TRUE|1차메뉴   |20200801|\n"
                                               "|itemCd    |varchar|20        |TRUE|1차메뉴   |20200801|\n"
                                               "|prntItemCd    |varchar|20        |TRUE|3차메뉴   |20200801|\n"
                                               "|ordStateCd    |varchar|20        |TRUE|확인중   |20200801|\n"
                                               "|salesUserId    |varchar|20        |TRUE|확인중   |20200801|\n"

                                               "\n"
                                               "### Data type : json\n"
                                               "```\n"
                                               "{\n"
                                               "    \"cpId\": \"**\",\n"
                                               "    \"shopId\": \"***\",\n"
                                               "    \"searchEdDt\": \"juno*****\",\n"
                                               "    \"searchStDt\": \"juno*****\",\n"
                                               "    \"ordMemo\": \"juno*****\",\n"
                                               "    \"custParam\": \"juno*****\",\n"
                                               "    \"cpTelNo\": \"juno*****\",\n"
                                               "    \"ordTpCd\": \"juno*****\",\n"
                                               "    \"itemGrpCd\": \"juno*****\",\n"
                                               "    \"itemCd\": \"juno*****\",\n"
                                               "    \"prntItemCd\": \"juno*****\",\n"
                                               "    \"ordStateCd\": \"juno*****\",\n"
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
            - API NAME : VisitHistoryList API
            - API DESC : CRM VisitHistoryList 진입경로
                        ex) 분석 > 대시보드,비교분석,랭크 외 다른 메뉴로 진입 > 하단 비중분석에 항목 클릭 > 하단에 오더목록 > 고객명 클릭
            - API METHOD : POST
            - REQUEST PARAMS :
                (파라미터 이름, 타입, 최대길이, 설명, 필수여부, 비고)
                (ex/ cpId, varchar, 20, 조직ID, TRUE, 주노헤어=JN)
                |PARAM NAME|TYPE   |MAX LENGTH|DESC|REQUIRED|ETC     |
                |:--------:|:-----:|:--------:|:--:|:------:|:------:|
                |cpID      |varchar|20        |TRUE|기업아이디   |주노헤어=JN|
                |shopId    |varchar|20        |TRUE|매장아이디   |아무개=1234123|
                |searchStDt    |varchar|20        |TRUE|검색시작일   |A매장=7|
                |searchEdDt    |varchar|20        |TRUE|검색종료일   |A매장=7|
                |ordMemo    |varchar|20        |TRUE|시술메모   |A매장=7|
                |custParam    |varchar|20        |TRUE|고객명/고객아이디   |A매장=7|
                |cpTelNo    |varchar|20        |TRUE|고객 전화번호   |A매장=7|
                |ordTpCd    |varchar|20        |TRUE|오더유형   |A매장=7|
                |itemGrpCd    |varchar|20        |TRUE|1차메뉴   |A매장=7|
                |itemCd    |varchar|20        |TRUE|2차메뉴   |A매장=7|
                |prntItemCd    |varchar|20        |TRUE|3차메뉴   |A매장=7|
                |ordStateCd    |varchar|20        |TRUE|확인중   |A매장=7|
                |salesUserId    |varchar|20        |TRUE|확인중   |A매장=7|

                -SAMPLE JSON
                ```
                {
                    "cpId": "JN",
                    "shopId": "149",
                    "searchStDt": "20200101",
                    "searchEdDt": "20230731",
                    "ordMemo": "",
                    "custParam": "",
                    "cpTelNo": "",
                    "ordTpCd": "",
                    "itemGrpCd": "",
                    "prntItemCd": "",
                    "itemCd": "",
                    "ordStateCd": "",
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
        service: OrderVisitHistoryListService = container.orderVisitHistoryListCrmServiceProvider()

        try:
            result = service.order_visit_history_list_crm(request.data, accessToken=kwargs.get('accessToken', 'None'),
                                                          refreshToken=kwargs.get('refreshToken', 'None'))
        except Exception as ex:
            print(f"{self.__class__.__name__} : Controller post error ==> {ex}")
            return Response(ex.__dict__, status=500)

        return Response(result, status=200)
        # return Response({"result": "CRM CONTROLLER GENERATE TEST"}, status=200)
