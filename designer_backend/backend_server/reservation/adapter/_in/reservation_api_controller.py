from dependency_injector.wiring import inject
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import APIView

from ...application.service.reservation_service import ReservationService
from ...serializers import PostRequestSerializer

from config.base_container import BaseContainer


class ReservationApiController(APIView):
    """
    # CLASS : ReservationApiController
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/21 6:39 PM
    # DESCRIPTION
        - 예약 관련 API Controller

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/21          jung-gyuho          최초 생성
    """

    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(tags=['CRM SYSTEM - RESERVATION API'], operation_summary="CRM RESERVATION API",
                         operation_description="# DESIGNER SEVER에서 CRM SYSTEM으로 예약 요청 API\n"
                                               "### Data type : json\n"
                                               "```\n"
                                               "{\n"
                                               "    \"cpId\": \"**\",\n"
                                               "    \"shopId\": \"***\",\n"
                                               "    \"rsrvNo\": \"juno*****\",\n"
                                               "}",
                         request_body=PostRequestSerializer, responses={200: 'Success'})
    @inject
    def post(self, request, *args, **kwargs):
        print(f"RESERVATION : Controller post get request.data ==> {request.data}")

        container = BaseContainer()
        service: ReservationService = container.reservationCrmServiceProvider()
        result = service.reservation_crm(request.data)

        return Response(result, status=200)
