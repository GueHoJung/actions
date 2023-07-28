from dependency_injector.wiring import inject
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import APIView

from ...application.service.employ_service import EmployService
from ...serializers import PostRequestSerializer
import config.utils.common_utils as common_utils
from config.utils.decorator import check_token

from config.base_container import BaseContainer


class EmployApiController(APIView):
    """
    # CLASS : EmployApiController
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/28 6:17 PM
    # DESCRIPTION
        - EmployApiController
        - APNT LIST API
        - HRM 디렉터리 :
        - HRM 서비스 호출 url :
        - HRM 서비스 호출 method : POST
        - HRM 서비스 호출 body : json
        - HRM 서비스 호출 파라미터 :
            cpId (기업아이디)
            shopId (매장아이디)
            custId (고객아이디)
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/28          jung-gyuho          최초 생성
    """

    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(tags=['HRM SYSTEM - Employ API'], operation_summary="HRM Employ APNT LIST API",
                         operation_description="# DESIGNER SEVER에서 HRM SYSTEM으로 APNT LIST 요청 API\n"
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
            - API NAME : APNT LIST API
            - API DESC : HRM APNT LIST 진입경로
                        ex) 분석 > 대시보드,비교분석,랭크 외 다른 메뉴로 진입 > 하단 비중분석에 항목 클릭 > 하단에 오더목록 > 고객명 클릭
            - API METHOD : POST
            - REQUEST PARAMS :
                (파라미터 이름, 타입, 최대길이, 설명, 필수여부, 비고)
                (ex/ cpId, varchar, 20, 조직ID, TRUE, 주노헤어=JN)
                |PARAM NAME|TYPE   |MAX LENGTH|DESC|REQUIRED|ETC     |
                |:--------:|:-----:|:--------:|:--:|:------:|:------:|
                |cpID      |varchar|20        |TRUE|기업아이디   |주노헤어=JN|
                |shopId    |varchar|20        |TRUE|매장아이디   |아무개=1234123|
                |custId    |varchar|20        |TRUE|고객아이디   |A매장=7|

                -SAMPLE JSON (** searchShop 같이 보내지 않아도 Return 함)
                ```
                {
                    "cpId": "JN",
                    "custId": "1916685",
                    "shopId": "1",
                    "searchShop": "order"
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
        service: EmployService = container.employHrmServiceProvider()

        try:
            result = service.employ_apnt_list_hrm(request.data, accessToken=kwargs.get('accessToken', 'None'),
                                                  refreshToken=kwargs.get('refreshToken', 'None'))
        except Exception as ex:
            print(f"{self.__class__.__name__} : Controller post error ==> {ex}")
            return Response(ex.__dict__, status=500)

        return Response(result, status=200)
        # return Response({"result": "HRM CONTROLLER GENERATE TEST"}, status=200)
