from dependency_injector.wiring import inject
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import APIView

from ...application.service.order_ticket_history_list_service import OrderTicketHistoryListService
from ...serializers import PostRequestSerializer
import config.utils.common_utils as common_utils
from config.utils.decorator import check_token

from config.base_container import BaseContainer


class OrderTicketHistoryListApiController(APIView):
    """
    # CLASS : OrderTicketHistoryListApiController
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/28 9:15 PM
    # DESCRIPTION
        - OrderTicketHistoryListApiController
        - Ticket History List API
        - CRM 디렉터리 : oreder
        - CRM 서비스 호출 url : /order/getTicketHistoryList/
        - CRM 서비스 호출 method : POST
        - CRM 서비스 호출 body : json
        - CRM 서비스 호출 파라미터 :
            cpId (기업아이디)
            custId (고객아이디)
            searchStDt (조회시작일)
            searchEdDt (조회종료일)
            tktNo (횟수권번호)
            tktHisDivCd (횟수권이력구분코드)
            userId (디자이너아이디)
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/28          jung-gyuho          최초 생성
    """

    # permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(tags=['CRM SYSTEM - Order API'], operation_summary="CRM Order Ticket History List API",
                         operation_description="# DESIGNER SEVER에서 CRM SYSTEM으로 Ticket History List 요청 API\n"
                                               "\n"
                                               "|PARAM NAME|TYPE   |MAX LENGTH|DESC|REQUIRED|ETC     |\n"
                                               "|:--------:|:-----:|:--------:|:--:|:------:|:------:|\n"
                                               "|cpID      |varchar|20        |TRUE|기업아이디   |JN|\n"
                                               "|custId    |varchar|20        |TRUE|고객아이디   |1801141|\n"
                                               "|searchStDt    |varchar|20        |TRUE|조회시작일   |20200801|\n"
                                               "|searchEdDt    |varchar|20        |TRUE|조회종료일   |20220801|\n"
                                               "|tktNo    |varchar|20        |TRUE|횟수권번호   |PR000000001801141D001|\n"
                                               "|tktHisDivCd    |varchar|20        |TRUE|횟수권이력구분코드   |\"\"|\n"
                                               "|userId    |varchar|20        |TRUE|고객아이디   |\"\"|\n"
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
            - API NAME : Ticket History List API
            - API DESC : CRM Ticket History List 진입경로
                        ex) 분석 > 대시보드,비교분석,랭크 외 다른 메뉴로 진입 > 하단 비중분석에 항목 클릭 > 하단에 오더목록 > 고객명 클릭
            - API METHOD : POST
            - REQUEST PARAMS :
                (파라미터 이름, 타입, 최대길이, 설명, 필수여부, 비고)
                (ex/ cpId, varchar, 20, 조직ID, TRUE, 주노헤어=JN)
                |PARAM NAME|TYPE   |MAX LENGTH|DESC|REQUIRED|ETC     |
                |:--------:|:-----:|:--------:|:--:|:------:|:------:|
                |cpID      |varchar|20        |TRUE|기업아이디   |주노헤어=JN|
                |custId    |varchar|20        |TRUE|고객아이디   |1801141|
                |searchStDt    |varchar|20        |TRUE|조회시작일   |20210619|
                |searchEdDt    |varchar|20        |TRUE|조회종료일   |20230728|
                |tktNo    |varchar|20        |TRUE|횟수권번호   |ORD0103-2106190036|
                |tktHisDivCd    |varchar|20        |TRUE|횟수권이력구분코드   |""|
                |userId    |varchar|20        |TRUE|고객아이디   |""|

                -SAMPLE JSON (** searchShop 같이 보내지 않아도 Return 함)
                ```
                {
                    "cpId": "JN",
                    "custId": "1801141",
                    "searchStDt": "20210619",
                    "searchEdDt": "20230728",
                    "tktNo": "ORD0103-2106190036",
                    "tktHisDivCd": "",
                    "userId": ""
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
        service: OrderTicketHistoryListService = container.orderTicketHistoryListCrmServiceProvider()

        try:
            result = service.order_ticket_history_list_crm(request.data, accessToken=kwargs.get('accessToken', 'None'),
                                                           refreshToken=kwargs.get('refreshToken', 'None'))
        except Exception as ex:
            print(f"{self.__class__.__name__} : Controller post error ==> {ex}")
            return Response(ex.__dict__, status=500)

        return Response(result, status=200)
        # return Response({"result": "CRM CONTROLLER GENERATE TEST"}, status=200)
