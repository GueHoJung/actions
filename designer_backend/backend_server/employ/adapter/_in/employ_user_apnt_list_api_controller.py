from dependency_injector.wiring import inject
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import APIView

from ...application.service.employ_user_apnt_list_service import EmployUserApntListService
from ...serializers import PostRequestSerializer
import config.utils.common_utils as common_utils
from config.utils.decorator import check_token

from config.base_container import BaseContainer


class EmployUserApntListApiController(APIView):
    """
    # CLASS : EmployUserApntListApiController
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/09 3:32 PM
    # DESCRIPTION
        - EmployUserApntListApiController
        - UserApntList API
        - HRM 디렉터리 : employ
        - HRM 서비스 설명 : 발령이력내역 상세
        - HRM 서비스 호출 url : /emply/getUserApntList/
        - HRM 서비스 호출 method : POST
        - HRM 서비스 호출 body : json
        - HRM 서비스 호출 파라미터 :
            cpId (기업아이디)
            userId (사용자아이디)
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/09          jung-gyuho          최초 생성
    """

    # permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(tags=['HRM SYSTEM - Employ API'], operation_summary="HRM Employ UserApntList API",
                         operation_description="# DESIGNER SEVER에서 HRM SYSTEM으로 UserApntList 요청 API\n"
                                               "\n"
                                               "|PARAM NAME|TYPE   |MAX LENGTH|REQUIRED|DESC|ETC     |\n"
                                               "|:--------:|:-----:|:--------:|:--:|:------:|:------:|\n"
                                               "|cpID      |varchar|20        |TRUE|기업아이디   |JN|\n"
                                               "|userId    |varchar|20        |TRUE|사용자아이디   |JNS01305|\n"
                                               "\n"
                                               "### Data type : json\n"
                                               "```\n"
                                               "{\n"
                                               "    \"cpId\": \"JN\",\n"
                                               "    \"userId\": \"JNS01305\",\n"
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
            - API NAME : UserApntList API
            - API DESC : HRM UserApntList 진입경로
                        ex) 분석 > 대시보드,비교분석,랭크 외 다른 메뉴로 진입 > 하단 비중분석에 항목 클릭 > 하단에 오더목록 > 고객명 클릭
            - API METHOD : POST
            - REQUEST PARAMS :
                (파라미터 이름, 타입, 최대길이, 설명, 필수여부, 비고)
                (ex/ cpId, varchar, 20, 조직ID, TRUE, 주노헤어=JN)
                |PARAM NAME|TYPE   |MAX LENGTH|REQUIRED|DESC|ETC     |
                |:--------:|:-----:|:--------:|:--:|:------:|:------:|
                |cpID      |varchar|20        |TRUE|기업아이디   |JN|
                |userId    |varchar|20        |TRUE|사용자아이디   |JNS01305|

                -SAMPLE JSON
                ```
                {
                    "cpId": "JN",
                    "userId": "JNS01305"
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
        service: EmployUserApntListService = container.employUserApntListHrmServiceProvider()

        try:
            result = service.employ_user_apnt_list_hrm(request.data, accessToken=kwargs.get('accessToken', 'None'),
                                                     refreshToken=kwargs.get('refreshToken', 'None'))
        except Exception as ex:
            print(f"{self.__class__.__name__} : Controller post error ==> {ex}")
            return Response(ex.__dict__, status=500)

        return Response(result, status=200)
        # return Response({"result": "HRM CONTROLLER GENERATE TEST"}, status=200)
