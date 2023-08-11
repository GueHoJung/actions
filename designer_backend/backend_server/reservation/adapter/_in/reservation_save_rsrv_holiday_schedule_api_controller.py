from dependency_injector.wiring import inject
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import APIView

from ...application.service.reservation_save_rsrv_holiday_schedule_service import \
    ReservationSaveRsrvHolidayScheduleService
from ...serializers import PostRequestSerializer
import config.utils.common_utils as common_utils
from config.utils.decorator import check_token

from config.base_container import BaseContainer


class ReservationSaveRsrvHolidayScheduleApiController(APIView):
    """
    # CLASS : ReservationSaveRsrvHolidayScheduleApiController
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/08 10:41 PM
    # DESCRIPTION
        - ReservationSaveRsrvHolidayScheduleApiController
        - SaveRsrvHolidaySchedule API
        - CRM 디렉터리 : reservation
        - CRM 서비스 설명 : 휴무일정 등록
        - CRM 서비스 호출 url : /reservation/saveRsrvHolidaySchedule/
        - CRM 서비스 호출 method : POST
        - CRM 서비스 호출 body : json
        - CRM 서비스 호출 파라미터 :
            cpId (기업아이디)
            shopId (매장아이디)
            userId (디자이너아이디)
            daySet (요일설정)
            weekSet (주차설정)
            hldyInf (휴무정보)
            hldyNm (휴무명)
            dfltYn (기본여부)
            useYn (사용여부)
            regUserId (등록자아이디)
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/08          jung-gyuho          최초 생성
    """

    # permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(tags=['CRM SYSTEM - Reservation API'],
                         operation_summary="CRM Reservation SaveRsrvHolidaySchedule API",
                         operation_description="# DESIGNER SEVER에서 CRM SYSTEM으로 SaveRsrvHolidaySchedule 요청 API\n"
                                               "\n"
                                               "|PARAM NAME|TYPE   |MAX LENGTH|REQUIRED|DESC|ETC     |\n"
                                               "|:--------:|:-----:|:--------:|:--:|:------:|:------:|\n"
                                               "|cpID      |varchar|20        |TRUE|기업아이디   |JN|\n"
                                               "|shopId      |varchar|20        |TRUE|매장아이디   |80|\n"
                                               "|userId      |varchar|20        |TRUE|디자이너아이디   |883|\n"
                                               "|daySet      |varchar|20        |TRUE|요일설정   |0111110|\n"
                                               "|weekSet      |varchar|20        |TRUE|주차설정   |101000|\n"
                                               "|hldyInf      |varchar|20        |TRUE|휴무정보   |월요일,화요일,수요일,목요일,금요일 / 1주차,3주차|\n"
                                               "|hldyNm      |varchar|20        |TRUE|휴무명   |테스트 휴일 설정|\n"
                                               "|dfltYn      |varchar|20        |TRUE|기본여부   |Y|\n"
                                               "|useYn      |varchar|20        |TRUE|사용여부   |Y|\n"
                                               "|regUserId      |varchar|20        |TRUE|등록자아이디   |11273|\n"
                                               "\n"
                                               "### Data type : json\n"
                                               "```\n"
                                               "{\n"
                                               "        \"cpId\": \"JN\",\n"
                                               "        \"shopId\": \"80\",\n"
                                               "        \"userId\": \"883\",\n"
                                               "        \"daySet\": \"0111110\",\n"
                                               "        \"weekSet\": \"101000\",\n"
                                               "        \"hldyInf\": \"월요일,화요일,수요일,목요일,금요일 / 1주차,3주차\",\n"
                                               "        \"hldyNm\": \"테스트 휴일 설정\",\n"
                                               "        \"dfltYn\": \"Y\",\n"
                                               "        \"useYn\": \"Y\",\n"
                                               "        \"regUserId\": \"11273\"\n"
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
            - API NAME : SaveRsrvHolidaySchedule API
            - API DESC : CRM SaveRsrvHolidaySchedule 진입경로
                        ex) 분석 > 대시보드,비교분석,랭크 외 다른 메뉴로 진입 > 하단 비중분석에 항목 클릭 > 하단에 오더목록 > 고객명 클릭
            - API METHOD : POST
            - REQUEST PARAMS :
                (파라미터 이름, 타입, 최대길이, 설명, 필수여부, 비고)
                (ex/ cpId, varchar, 20, 조직ID, TRUE, 주노헤어=JN)
                |PARAM NAME|TYPE   |MAX LENGTH|REQUIRED|DESC|ETC     |
                |:--------:|:-----:|:--------:|:--:|:------:|:------:|
                |cpID      |varchar|20        |TRUE|기업아이디   |JN|
                |shopId      |varchar|20        |TRUE|매장아이디   |80|
                |userId      |varchar|20        |TRUE|디자이너아이디   |883|
                |daySet      |varchar|20        |TRUE|요일설정   |0111110|
                |weekSet      |varchar|20        |TRUE|주차설정   |101000|
                |hldyInf      |varchar|20        |TRUE|휴무정보   |월요일,화요일,수요일,목요일,금요일 / 1주차,3주차|
                |hldyNm      |varchar|20        |TRUE|휴무명   |테스트 휴일 설정|
                |dfltYn      |varchar|20        |TRUE|기본여부   |Y|
                |useYn      |varchar|20        |TRUE|사용여부   |Y|
                |regUserId      |varchar|20        |TRUE|등록자아이디   |11273|

                -SAMPLE JSON
                ```
                {
                    "cpId": "JN",
                    "shopId": "80",
                    "userId": "883",
                    "daySet": "0111110",
                    "weekSet": "101000",
                    "hldyInf": "월요일,화요일,수요일,목요일,금요일 / 1주차,3주차",
                    "hldyNm": "테스트 휴일 설정",
                    "dfltYn": "Y",
                    "useYn": "Y",
                    "regUserId": "11273"
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
        service: ReservationSaveRsrvHolidayScheduleService = container.reservationSaveRsrvHolidayScheduleCrmServiceProvider()

        try:
            result = service.reservation_save_rsrv_holiday_schedule_crm(request.data, accessToken=kwargs.get('accessToken', 'None'),
                                                     refreshToken=kwargs.get('refreshToken', 'None'))
        except Exception as ex:
            print(f"{self.__class__.__name__} : Controller post error ==> {ex}")
            return Response(ex.__dict__, status=500)

        return Response(result, status=200)
        # return Response({"result": "CRM CONTROLLER GENERATE TEST"}, status=200)
