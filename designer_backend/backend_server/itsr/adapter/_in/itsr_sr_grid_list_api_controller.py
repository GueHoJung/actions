from dependency_injector.wiring import inject
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import APIView

from ...application.service.itsr_sr_grid_list_service import ItsrSrGridListService
from ...serializers import PostRequestSerializer
import config.utils.common_utils as common_utils
from config.utils.decorator import check_token

from config.base_container import BaseContainer


class ItsrSrGridListApiController(APIView):
    """
    # CLASS : ItsrSrGridListApiController
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/09 2:49 PM
    # DESCRIPTION
        - ItsrSrGridListApiController
        - SrGridList API
        - CRM 디렉터리 : itsr
        - CRM 서비스 설명 : 문의내역
        - CRM 서비스 호출 url : /itsr/getSrGridList/
        - CRM 서비스 호출 method : POST
        - CRM 서비스 호출 body : json
        - CRM 서비스 호출 파라미터 :
            cpId (기업아이디)
            shopId (매장아이디)
            year (요청연도)
            systmTpCd (시스템유형)
            reqClsfcCd (요청분류)
            reqPrcStateCd (처리상태)
            reqCon (요청내용)
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/09          jung-gyuho          최초 생성
    """

    # permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(tags=['CRM SYSTEM - Itsr API'], operation_summary="CRM Itsr SrGridList API",
                         operation_description="# DESIGNER SEVER에서 CRM SYSTEM으로 SrGridList 요청 API\n"
                                               "\n"
                                               "|PARAM NAME|TYPE   |MAX LENGTH|REQUIRED|DESC|ETC     |\n"
                                               "|:--------:|:-----:|:--------:|:--:|:------:|:------:|\n"
                                               "|cpID      |varchar|20        |TRUE|기업아이디   |JN|\n"
                                               "|shopId      |varchar|20        |TRUE|매장아이디   |80|\n"
                                               "|year      |varchar|20        |TRUE|요청연도   |2023|\n"
                                               "|systmTpCd      |varchar|20        |TRUE|시스템유형   ||\n"
                                               "|reqClsfcCd      |varchar|20        |TRUE|요청분류   ||\n"
                                               "|reqPrcStateCd      |varchar|20        |TRUE|처리상태   ||\n"
                                               "|reqCon      |varchar|20        |TRUE|요청내용   ||\n"
                                               "\n"
                                               "### Data type : json\n"
                                               "```\n"
                                               "{\n"
                                               "        \"cpId\": \"JN\",\n"
                                               "        \"shopId\": \"80\",\n"
                                               "        \"year\": \"2023\",\n"
                                               "        \"systmTpCd\": \"\",\n"
                                               "        \"reqClsfcCd\": \"\",\n"
                                               "        \"reqPrcStateCd\": \"\",\n"
                                               "        \"reqCon\": \"\"\n"
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
            - API NAME : SrGridList API
            - API DESC : CRM SrGridList 진입경로
                        ex) 분석 > 대시보드,비교분석,랭크 외 다른 메뉴로 진입 > 하단 비중분석에 항목 클릭 > 하단에 오더목록 > 고객명 클릭
            - API METHOD : POST
            - REQUEST PARAMS :
                (파라미터 이름, 타입, 최대길이, 설명, 필수여부, 비고)
                (ex/ cpId, varchar, 20, 조직ID, TRUE, 주노헤어=JN)
                |PARAM NAME|TYPE   |MAX LENGTH|REQUIRED|DESC|ETC     |
                |:--------:|:-----:|:--------:|:--:|:------:|:------:|
                |cpID      |varchar|20        |TRUE|기업아이디   |JN|
                |shopId      |varchar|20        |TRUE|매장아이디   |80|
                |year      |varchar|20        |TRUE|요청연도   |2023|
                |systmTpCd      |varchar|20        |TRUE|시스템유형   ||
                |reqClsfcCd      |varchar|20        |TRUE|요청분류   ||
                |reqPrcStateCd      |varchar|20        |TRUE|처리상태   ||
                |reqCon      |varchar|20        |TRUE|요청내용   |SR 등록 테스트|

                -SAMPLE JSON
                ```
                {
                    "cpId": "JN",
                    "shopId": "80",
                    "year": "2023",
                    "systmTpCd": "",
                    "reqClsfcCd": "",
                    "reqPrcStateCd": "",
                    "reqCon": ""
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
        service: ItsrSrGridListService = container.itsrSrGridListCrmServiceProvider()

        try:
            result = service.itsr_sr_grid_list_crm(request.data, accessToken=kwargs.get('accessToken', 'None'),
                                                   refreshToken=kwargs.get('refreshToken', 'None'))
        except Exception as ex:
            print(f"{self.__class__.__name__} : Controller post error ==> {ex}")
            return Response(ex.__dict__, status=500)

        return Response(result, status=200)
        # return Response({"result": "CRM CONTROLLER GENERATE TEST"}, status=200)
