from dependency_injector.wiring import inject
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import APIView

# from ...application.service.customer_service import CustomerService
from ...serializers import PostRequestSerializer

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
    def post(self, request, *args, **kwargs):
        print(f"{self.__class__.__name__} : Controller post get request.data ==> {request.data}")

        container = BaseContainer()
        service: CustomerService = container.customerCrmServiceProvider()
        result = service.customer_info_crm(request.data)

        return Response(result, status=200)