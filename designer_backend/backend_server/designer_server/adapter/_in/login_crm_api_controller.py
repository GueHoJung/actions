from dependency_injector.wiring import inject
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from ...application.service.login_service import LoginService
from ...serializers import PostRequestSerializer
from config.base_container import BaseContainer


class LoginCrmApiController(APIView):
    """
    # CLASS : LoginCrmApiController
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/21 2:37 PM
    # DESCRIPTION
        - LoginCrmApiController
        - CRM Login API 호출

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/21          jung-gyuho          최초 생성
    """

    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(tags=['CRM SYSTEM - LOGIN API'], operation_summary="CRM LOGIN API",
                         operation_description="# DESIGNER SEVER에서 CRM SYSTEM으로 로그인 요청 API\n"
                                               "## accessToken 과 refreshToken 을 받아서 response 객체에 저장\n"
                                               "## accessToken 은 12시간 유효, refreshToken 은 1일 유효\n\n"
                                               "### Data type : json\n"
                                               "```\n"
                                               "{\n"
                                               "    \"cpId\": \"**\",\n"
                                               "    \"system\": \"***\",\n"
                                               "    \"userId\": \"juno*****\",\n"
                                               "    \"password\": \"***************\",\n"
                                               "    \"client\": \"**\"\n"
                                               "}",
                         request_body=PostRequestSerializer, responses={200: 'Success'})
    @inject
    def post(self, request, *args, **kwargs):
        print(f"Controller post get request.data ==> {request.data}")

        container = BaseContainer()
        service: LoginService = container.loginCrmServiceProvider()
        result = service.login_crm(request.data)

        return Response(result, status=200)
