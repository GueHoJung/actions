from dependency_injector.wiring import inject
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import APIView

from ...application.service.customer_service import CustomerService
from ...serializers import PostRequestSerializer
import config.utils.common_utils as common_utils
from config.utils.decorator import check_token

from config.base_container import BaseContainer


class CustomerApiController(APIView):
    """
    # CLASS : CustomerApiController
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/21 10:01 PM
    # DESCRIPTION
        - 고객 관련 API Controller
        /customer/getCustInfoWithAgr/
            cpId (기업아이디)
            shopId (매장아이디)
            custId (고객아이디)
            isInActive (휴면여부 => true/false)
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/21          jung-gyuho          최초 생성
    """

    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(tags=['CRM SYSTEM - CUSTOMER API'], operation_summary="CRM CUSTOMER INFO API",
                         operation_description="# DESIGNER SEVER에서 CRM SYSTEM으로 고객 정보 요청 API\n"
                                               "### Data type : json\n"
                                               "```\n"
                                               "{\n"
                                               "    \"cpId\": \"**\",\n"
                                               "    \"shopId\": \"***\",\n"
                                               "    \"custId\": \"juno*****\",\n"
                                               "    \"isInActive\": \"juno*****\",\n"
                                               "}",
                         request_body=PostRequestSerializer, responses={200: 'Success'})
    @inject
    @check_token
    def post(self, request, *args, **kwargs):
        """
        # API : post
        # AUTHOR : jung-gyuho
        # TIME : 2023/07/26 6:29 PM
        # DESCRIPTION
            - API NAME :
            - API DESC :
            - API METHOD :
            - REQUEST PARAMS :
                (파라미터 이름, 타입, 최대길이, 설명, 필수여부, 비고)
                (ex/ cpId, varchar, 20, 조직ID, TRUE, 주노헤어=JN)
                |PARAM NAME|TYPE   |MAX LENGTH|DESC|REQUIRED|ETC     |
                |:--------:|:-----:|:--------:|:--:|:------:|:------:|
                |cpID      |varchar|20        |TRUE|조직ID   |주노헤어=JN|

                -SAMPLE JSON
                ```
                {
                    "cpId": "JN",
                    "system": "CRM",
                    "userId": "juno***",
                    "password": "***",
                    "client": "PC"
                }

                ```
            - RESPONSE OBJECTS :
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
        # print(f"{self.__class__.__name__} : Controller post get request.COOKIES ==> {request.COOKIES}")
        # print(f"{self.__class__.__name__} : Controller post get request.META.get('HTTP_COOKIE') ==> {request.META.get('HTTP_COOKIE')}")

        container = BaseContainer()
        service: CustomerService = container.customerCrmServiceProvider()
        try:
            result = service.customer_info_crm(request.data, accessToken=kwargs.get('accessToken', 'None'),
                                               refreshToken=kwargs.get('refreshToken', 'None'))
            # if result.get('message') == '0000':
        except Exception as e:
            return Response(e, status=500)

        return Response(result, status=200)
