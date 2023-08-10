from dependency_injector.wiring import inject
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import APIView

from ...application.service.reservation_mod_rsrv_holiday_schedule_service import \
    ReservationModRsrvHolidayScheduleService
from ...serializers import PostRequestSerializer
import config.utils.common_utils as common_utils
from config.utils.decorator import check_token

from config.base_container import BaseContainer


class ReservationModRsrvHolidayScheduleApiController(APIView):
    """
    # CLASS : ReservationModRsrvHolidayScheduleApiController
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/08 10:11 PM
    # DESCRIPTION
        - ReservationModRsrvHolidayScheduleApiController
        - ModRsrvHolidaySchedule API
        - CRM 디렉터리 : reservation
        - CRM 서비스 설명 : 휴무일정 수정
        - CRM 서비스 호출 url : /reservation/modRsrvHolidaySchedule/
        - CRM 서비스 호출 method : POST
        - CRM 서비스 호출 body : json
        - CRM 서비스 호출 파라미터 :
            cpId (기업아이디)
            shopId (매장아이디)
            userId (디자이너아이디)
            lineNo (라인번호)
            daySet (요일설정)
            weekSet (주차설정)
            hldyInf (휴무정보)
            hldyNm (휴무명)
            dfltYn (기본여부)

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/08          jung-gyuho          최초 생성
    """

    # permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(tags=['CRM SYSTEM - Reservation API'],
                         operation_summary="CRM Reservation ModRsrvHolidaySchedule API",
                         operation_description="# DESIGNER SEVER에서 CRM SYSTEM으로 ModRsrvHolidaySchedule 요청 API\n"
                                               "\n"
                                               "|PARAM NAME|TYPE   |MAX LENGTH|REQUIRED|DESC|ETC     |\n"
                                               "|:--------:|:-----:|:--------:|:--:|:------:|:------:|\n"
                                               "|cpID      |varchar|20        |TRUE|기업아이디   |JN|\n"
                                               "|shopId      |varchar|20        |TRUE|매장아이디   |80|\n"
                                               "|userId      |varchar|20        |TRUE|디자이너아이디   |2408|\n"
                                               "|lineNo      |varchar|20        |TRUE|라인번호   |1|\n"
                                               "|daySet      |varchar|20        |TRUE|요일설정   |1100000|\n"
                                               "|weekSet      |varchar|20        |TRUE|주차설정  |100000|\n"
                                               "|hldyInf      |varchar|20        |TRUE|휴무정보   |일요일,월요일 / 1주차|\n"
                                               "|hldyNm      |varchar|20        |TRUE|휴무명   |기본 휴일 설정|\n"
                                               "|dfltYn      |varchar|20        |TRUE|기본여부   |Y|\n"
                                               "|useYn      |varchar|20        |TRUE|사용여부   |Y|\n"
                                               "|updUserId      |varchar|20        |TRUE|업데이트사용자아이디   |11273|\n"
                                               "\n"
                                               "### Data type : json\n"
                                               "```\n"
                                               "{\n"
                                               "        \"cpId\": \"JN\",\n"
                                               "        \"shopId\": \"80\",\n"
                                               "        \"userId\": \"2408\",\n"
                                               "        \"lineNo\": \"1\",\n"
                                               "        \"daySet\": \"1100000\",\n"
                                               "        \"weekSet\": \"100000\",\n"
                                               "        \"hldyInf\": \"일요일,월요일 / 1주차\",\n"
                                               "        \"hldyNm\": \"기본 휴일 설정\",\n"
                                               "        \"dfltYn\": \"Y\",\n"
                                               "        \"useYn\": \"Y\",\n"
                                               "        \"updUserId\": \"11273\"\n"
                                               "    }\n",

    request_body = PostRequestSerializer, responses = {200: 'Success'})

    @inject
    @check_token
    def post(self, request, *args, **kwargs):
        """
        # API : post
        # AUTHOR : jung-gyuho
        # TIME : 2023/07/27 6:02 PM
        # DESCRIPTION
            - API NAME : ModRsrvHolidaySchedule API
            - API DESC : CRM ModRsrvHolidaySchedule 진입경로
                        ex) 분석 > 대시보드,비교분석,랭크 외 다른 메뉴로 진입 > 하단 비중분석에 항목 클릭 > 하단에 오더목록 > 고객명 클릭
            - API METHOD : POST
            - REQUEST PARAMS :
                (파라미터 이름, 타입, 최대길이, 설명, 필수여부, 비고)
                (ex/ cpId, varchar, 20, 조직ID, TRUE, 주노헤어=JN)
                |PARAM NAME|TYPE   |MAX LENGTH|REQUIRED|DESC|ETC     |
                |:--------:|:-----:|:--------:|:--:|:------:|:------:|
                |cpID      |varchar|20        |TRUE|기업아이디   |JN|
                |shopId      |varchar|20        |TRUE|매장아이디   |80|
                |userId      |varchar|20        |TRUE|디자이너아이디   |2408|
                |lineNo      |varchar|20        |TRUE|라인번호   |1|
                |daySet      |varchar|20        |TRUE|요일설정   |1100000|
                |weekSet      |varchar|20        |TRUE|주차설정  |100000|
                |hldyInf      |varchar|20        |TRUE|휴무정보   |일요일,월요일 / 1주차|
                |hldyNm      |varchar|20        |TRUE|휴무명   |기본 휴일 설정|
                |dfltYn      |varchar|20        |TRUE|기본여부   |Y|
                |useYn      |varchar|20        |TRUE|사용여부   |Y|
                |updUserId      |varchar|20        |TRUE|업데이트사용자아이디   |11273|

                -SAMPLE JSON
                ```
                {
                    "cpId": "JN",
                    "shopId": "80",
                    "userId": "2408",
                    "lineNo": "1",
                    "daySet": "1100000",
                    "weekSet": "100000",
                    "hldyInf": "일요일,월요일 / 1주차",
                    "hldyNm": "기본 휴일 설정",
                    "dfltYn": "Y",
                    "useYn": "Y",
                    "updUserId": "11273"
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
        service: ReservationModRsrvHolidayScheduleService = container.reservationModRsrvHolidayScheduleCrmServiceProvider()

        try:
            result = service.reservation_mod_rsrv_holiday_schedule_crm(request.data,
                                                                       accessToken=kwargs.get('accessToken', 'None'),
                                                                       refreshToken=kwargs.get('refreshToken', 'None'))
        except Exception as ex:
            print(f"{self.__class__.__name__} : Controller post error ==> {ex}")
            return Response(ex.__dict__, status=500)

        return Response(result, status=200)
        # return Response({"result": "CRM CONTROLLER GENERATE TEST"}, status=200)
