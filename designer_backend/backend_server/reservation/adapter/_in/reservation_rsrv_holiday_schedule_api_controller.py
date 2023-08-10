from dependency_injector.wiring import inject
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import APIView

from ...application.service.reservation_rsrv_holiday_schedule_service import ReservationRsrvHolidayScheduleService
from ...serializers import PostRequestSerializer
import config.utils.common_utils as common_utils
from config.utils.decorator import check_token

from config.base_container import BaseContainer


class ReservationRsrvHolidayScheduleApiController(APIView):
    """
    # CLASS : ReservationRsrvHolidayScheduleApiController
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/08 10:00 PM
    # DESCRIPTION
        - ReservationRsrvHolidayScheduleApiController
        - RsrvHolidaySchedule API
        - CRM 디렉터리 : reservation
        - CRM 서비스 설명 : 휴무일정 조회
        - CRM 서비스 호출 url : /reservation/getRsrvHolidaySchedule/
        - CRM 서비스 호출 method : POST
        - CRM 서비스 호출 body : json
        - CRM 서비스 호출 파라미터 :
            cpId (기업아이디)
            shopId (매장아이디)
            userId (디자이너아이디)
            dfltYn (기본여부)
            useYn (사용여부)
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/08          jung-gyuho          최초 생성
    """

    # permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(tags=['CRM SYSTEM - Reservation API'],
                         operation_summary="CRM Reservation RsrvHolidaySchedule API",
                         operation_description="# DESIGNER SEVER에서 CRM SYSTEM으로 RsrvHolidaySchedule 요청 API\n"
                                               "\n"
                                               "|PARAM NAME|TYPE   |MAX LENGTH|REQUIRED|DESC|ETC     |\n"
                                               "|:--------:|:-----:|:--------:|:--:|:------:|:------:|\n"
                                               "|cpID      |varchar|20        |TRUE|기업아이디   |JN|\n"
                                               "|shopId    |varchar|20        |TRUE|매방아이디   |80|\n"
                                               "|userId    |varchar|20        |TRUE|디자이너아이디   |883|\n"
                                               "\n"
                                               "### Data type : json\n"
                                               "```\n"
                                               "{\n"
                                               "        \"cpId\": \"JN\",\n"
                                               "        \"shopId\": \"80\",\n"
                                               "        \"userId\": \"883\"\n"
                                               "    }\n",
                         request_body=PostRequestSerializer, responses={200: 'Success'})
    @inject
    @check_token
    def post(self, request, *args, **kwargs):
        """
        # API : post
        # AUTHOR : jung-gyuho
        # TIME : 2023/07/27 6:02 PM
        # DESCRIPTION
            - API NAME : RsrvHolidaySchedule API
            - API DESC : CRM RsrvHolidaySchedule 진입경로
                        ex) 분석 > 대시보드,비교분석,랭크 외 다른 메뉴로 진입 > 하단 비중분석에 항목 클릭 > 하단에 오더목록 > 고객명 클릭
            - API METHOD : POST
            - REQUEST PARAMS :
                (파라미터 이름, 타입, 최대길이, 설명, 필수여부, 비고)
                (ex/ cpId, varchar, 20, 조직ID, TRUE, 주노헤어=JN)
                |PARAM NAME|TYPE   |MAX LENGTH|REQUIRED|DESC|ETC     |
                |:--------:|:-----:|:--------:|:--:|:------:|:------:|
                |cpID      |varchar|20        |TRUE|기업아이디   |JN|
                |shopId    |varchar|20        |TRUE|매장아이디   |80|
                |userId    |varchar|20        |TRUE|디자이너아이디   |883|

                -SAMPLE JSON
                ```
                {
                    "cpId": "JN",
                    "shopId": "80",
                    "userId": "883"
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
        service: ReservationRsrvHolidayScheduleService = container.reservationRsrvHolidayScheduleCrmServiceProvider()

        try:
            result = service.reservation_rsrv_holiday_schedule_crm(request.data,
                                                                   accessToken=kwargs.get('accessToken', 'None'),
                                                                   refreshToken=kwargs.get('refreshToken', 'None'))
        except Exception as ex:
            print(f"{self.__class__.__name__} : Controller post error ==> {ex}")
            return Response(ex.__dict__, status=500)

        return Response(result, status=200)
        # return Response({"result": "CRM CONTROLLER GENERATE TEST"}, status=200)
