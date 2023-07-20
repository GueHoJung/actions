import sys

from dependency_injector.wiring import inject, Provide
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, serializers

from ..out.login_hrm_api_adapter import LoginHrmApiAdapter
from ...application.service.login_hrm_service import LoginHRMService
from config.base_container import BaseContainer

from ...serializers import PostRequestSerializer, PostResponseSerializer, GetRequestSerializer
from ...util.utils import convert_json_to_obj


class LoginHRMAPIController(APIView):
    # init_app()
    permission_classes = [permissions.AllowAny]

    # manual_parameters = [] 방식 : Path Parameter 방식 => 파라미터 아주 간단할 때 사용
    task_id_path = openapi.Parameter('task_id', in_=openapi.IN_PATH, description='task_id _in path', required=True,
                                     type=openapi.TYPE_NUMBER)

    # manual_parameters = [] 방식 : Query Parameter 방식 => 파라미터가 너무 많지 않을 때 사용, 파라미터 설정을 바로 보고 싶은 경우 등
    task_id_query = openapi.Parameter('task_id', in_=openapi.IN_QUERY, description='task_id _in path', required=True,
                                      type=openapi.TYPE_NUMBER)

    # offset      = openapi.Parameter('offset', openapi.IN_QUERY, description='offset param', required=True, default=0, type=openapi.TYPE_INTEGER)
    # limit       = openapi.Parameter('limit', openapi.IN_QUERY, description='limit param', required=True, default=10, type=openapi.TYPE_INTEGER)
    # trial_stage = openapi.Parameter('trial_stage', openapi.IN_QUERY, description='trial_stage param', required=False, type=openapi.TYPE_STRING)
    # department  = openapi.Parameter('department', openapi.IN_QUERY, description='department param', required=False, type=openapi.TYPE_STRING)
    # institute   = openapi.Parameter('institute', openapi.IN_QUERY, description='institute param', required=False, type=openapi.TYPE_STRING)
    # scope       = openapi.Parameter('scope', openapi.IN_QUERY, description='scope param', required=False, type=openapi.TYPE_STRING)
    # title       = openapi.Parameter('title', openapi.IN_QUERY, description='title param', required=False, type=openapi.TYPE_STRING)
    # type        = openapi.Parameter('type', openapi.IN_QUERY, description='type param', required=False, type=openapi.TYPE_STRING)

    # tags를 같은 값으로 사용하지 않으면, Swagger UI 상에 다른 API로 나타난다.
    # PATH 상에서 변수 받기 위해 2중(url, get(param) 설정 해줘야 하는 번거로움 있음, 아래 IN_QUERY 방식으로 사용
    # @swagger_auto_schema(tags=['LOGIN API by HRM SYSTEM'], operation_summary="IN_PATH TEST",
    #                      operation_description="SWAGGER 제공 PARAMETER 칸 에서 입력시 동작 안되는 문제 PATH TEST",
    #                      manual_parameters=[task_id_path], responses={200: 'Success'})
    # def get(self, request,taskId):
    #     print(f"LoginHRMAPIController get request.data ==> {request.data}")
    #     print(f"LoginHRMAPIController get taskId ==> {taskId}")
    #     inPathParam = request.GET.get('taskId')
    #     # getParams.append(task_id)
    #
    #     return Response({"mgs": "LoginHRMAPIController get", "get() PARAMS": taskId, "request.GET.get('taskId')": inPathParam},
    #                     status=200)

    @swagger_auto_schema(tags=['LOGIN API by HRM SYSTEM'], operation_summary="IN_QUERY TEST",
                         operation_description="SWAGGER 제공 PARAMETER 칸 에서 입력시 동작 안되는 문제 QUERY TEST",
                         manual_parameters=[task_id_query], responses={200: 'Success'})
    def get(self, request, *args, **kwargs):
        inQueryParam = request.GET.get('task_id')

        return Response({"mgs": "LoginHRMAPIController get", "inQueryParam": inQueryParam},
                        status=200)

    # Body 방식 : Serializer Class 방식 => 파라미터가 많을 때 사용, 파라미터 설정을 분리해 관리 하고 싶은 경우
    # query_serializer = Serializer Class [GET]방식,
    # request_body = Serializer Class [POST]방식,
    @swagger_auto_schema(tags=['LOGIN API by HRM SYSTEM'], request_body=PostRequestSerializer, )
    @inject
    def post(self, request, *args, **kwargs):
        print(f"LoginHRMAPI get request.data ==> {request.data}")

        container = BaseContainer()
        service: LoginHRMService = container.loginHRMServiceProvider()
        service.login_hrm(request.data)

        result = LoginHrmApiAdapter().login_hrm_api(path="/login/login/", method="POST", data=request.data)
        jResult = convert_json_to_obj(result)
        print(f"LoginHRMAPI get result ==> {result}")
        print(f"LoginHRMAPI get jResult ==> {jResult}")
        return Response(jResult)


if __name__ == '__login_hrm_api_controller__':
    containers = BaseContainer()
    containers.wire(modules=[sys.modules[__name__]])
