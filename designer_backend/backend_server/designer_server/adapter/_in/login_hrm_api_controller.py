from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, serializers

from ..out.login_hrm_api_adapter import LoginHrmApiAdapter, convert_json_to_obj

import json

from ...serializers import PostRequestSerializer, PostResponseSerializer


class LoginHRMAPIController(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema()
    def get(self, request):
        print(f"LoginHRMAPI get request ==> {request}")

        result = LoginHrmApiAdapter().login_hrm_api(path="/login/login", method="POST")
        print(f"LoginHRMAPI get result ==> {result}")
        return Response(convert_json_to_obj(result))

    @swagger_auto_schema(request_body=PostRequestSerializer, responses={"201": PostResponseSerializer})
    def post(self, request, *args, **kwargs):
        print(f"LoginHRMAPI get request.data ==> {request.data}")

        result = LoginHrmApiAdapter().login_hrm_api(path="/login/login", method="POST", data=request.data)
        print(f"LoginHRMAPI get result ==> {result}")
        return Response(convert_json_to_obj(result))
