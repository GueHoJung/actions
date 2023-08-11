from dependency_injector.wiring import inject
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import APIView

from ...application.service.analysis_weekly_synthesis_anlys_service import AnalysisWeeklySynthesisAnlysService
from ...serializers import PostRequestSerializer
import config.utils.common_utils as common_utils
from config.utils.decorator import check_token

from config.base_container import BaseContainer


class AnalysisWeeklySynthesisAnlysApiController(APIView):
    """
    # CLASS : AnalysisWeeklySynthesisAnlysApiController
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/07 7:41 PM
    # DESCRIPTION
        - AnalysisWeeklySynthesisAnlysApiController
        - WeeklySynthesisAnlys API
        - CRM 디렉터리 : analysis
        - CRM 서비스 설명 : 분석 고객분석 종합분석 - 주
        - CRM 서비스 호출 url : /analysis/getWeeklySynthesisAnlys/
        - CRM 서비스 호출 method : POST
        - CRM 서비스 호출 body : json
        - CRM 서비스 호출 파라미터 :
            cpId (기업아이디)
            loginShopId (로그인매장)
            loginId (로그인아이디)
            path (메뉴패스)
            name (메뉴명)
            standard (조회기준 => 매장/디자이너)
            shopId (매장아이디)
            term (월/주/일 => month/week/day)
            searchStDt (조회시작일)
            searchEdDt (조회종료일)
            searchWeek (조회주차)
            userList (디자이너아이디목록)*
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/07          jung-gyuho          최초 생성
    """

    # permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(tags=['CRM SYSTEM - Analysis API'], operation_summary="CRM Analysis WeeklySynthesisAnlys API",
                         operation_description="# DESIGNER SEVER에서 CRM SYSTEM으로 WeeklySynthesisAnlys 요청 API\n"
                                               "\n"
                                               "|PARAM NAME|TYPE   |MAX LENGTH|REQUIRED|DESC|ETC     |\n"
                                               "|:--------:|:-----:|:--------:|:--:|:------:|:------:|\n"
                                               "|cpID      |varchar|20        |TRUE|기업아이디   |JN|\n"
                                               "|loginShopId    |varchar|20        |TRUE|로그인매장   |149|\n"
                                               "|loginId    |varchar|20        |TRUE|로그인아이디   |11273|\n"
                                               "|path    |varchar|20        |TRUE|메뉴패스   |/crm/anlys/cust-anlys-synth|\n"
                                               "|name    |varchar|20        |TRUE|메뉴명   |cust-anlys-synth|\n"
                                               "|standard    |varchar|20        |TRUE|조회기준 => 매장/디자이너   |DSGN|\n"
                                               "|shopNm    |varchar|20        |TRUE|-   |준오뷰티|\n"
                                               "|shopId    |varchar|20        |TRUE|매장아이디   |149|\n"
                                               "|shopList    |varchar|20        |TRUE|-   |'10'|\n"
                                               "|shopCnt    |varchar|20        |TRUE|-   |1|\n"
                                               "|term    |varchar|20        |TRUE|월/주/일 => month/week/day |week|\n"
                                               "|searchStDt    |varchar|20        |TRUE|조회시작일   |202201|\n"
                                               "|searchEdDt    |varchar|20        |TRUE|조회종료일   |202203|\n"
                                               "|searchQrtr    |varchar|20        |TRUE|-   ||\n"
                                               "|searchWeek    |varchar|20        |TRUE|조회주차   ||\n"
                                               "|empBuyYn    |varchar|20        |TRUE|-   ||\n"
                                               "|ordTpCd    |varchar|20        |TRUE|-   ||\n"
                                               "|trmTpCd    |varchar|20        |TRUE|-   ||\n"
                                               "|payDivCd    |varchar|20        |TRUE|-   ||\n"
                                               "|custClsfcCd    |varchar|20        |TRUE|-   ||\n"
                                               "|mbrGrdCd    |varchar|20        |TRUE|-   ||\n"
                                               "|prpTpCd    |varchar|20        |TRUE|-   ||\n"
                                               "|tktTpCd    |varchar|20        |TRUE|횟수권유형코드   ||\n"
                                               "|prdcBrndCd    |varchar|20        |TRUE|-   |null|\n"
                                               "|gndrCd    |varchar|20        |TRUE|-   ||\n"
                                               "|joinTpCd    |varchar|20        |TRUE|-   ||\n"
                                               "|ageGrpCd    |varchar|20        |TRUE|-   ||\n"
                                               "|userNm    |varchar|20        |TRUE|-   ||\n"
                                               "|userId    |varchar|20        |TRUE|디자이너아이디   ||\n"
                                               "|userList    |varchar|20        |TRUE|디자이너아이디목록   |'9829','9827','6795','6019'|\n"
                                               "|userCnt    |varchar|20        |TRUE|-   |4|\n"
                                               "|custAnlysDiv    |varchar|20        |TRUE|-   |Synthesis|\n"
                                               "\n"
                                               "### Data type : json\n"
                                               "```\n"
                                               "{\n"
                                               "        \"cpId\": \"JN\",\n"
                                               "        \"loginShopId\": \"149\",\n"
                                               "        \"loginId\": \"11273\",\n"
                                               "        \"path\": \"/crm/anlys/cust-anlys-synth\",\n"
                                               "        \"name\": \"cust-anlys-synth\",\n"
                                               "        \"standard\": \"DSGN\",\n"
                                               "        \"shopNm\": \"준오뷰티\",\n"
                                               "        \"shopId\": \"149\",\n"
                                               "        \"shopList\": \"'10'\",\n"
                                               "        \"shopCnt\": 1,\n"
                                               "        \"term\": \"week\",\n"
                                               "        \"searchStDt\": \"202201\",\n"
                                               "        \"searchEdDt\": \"202203\",\n"
                                               "        \"searchQrtr\": \"\",\n"
                                               "        \"searchWeek\": \"\",\n"
                                               "        \"empBuyYn\": \"\",\n"
                                               "        \"ordTpCd\": \"\",\n"
                                               "        \"trmTpCd\": \"\",\n"
                                               "        \"payDivCd\": \"\",\n"
                                               "        \"custClsfcCd\": \"\",\n"
                                               "        \"mbrGrdCd\": \"\",\n"
                                               "        \"prpTpCd\": \"\",\n"
                                               "        \"tktTpCd\": \"\",\n"
                                               "        \"prdcBrndCd\": null,\n"
                                               "        \"gndrCd\": \"\",\n"
                                               "        \"joinTpCd\": \"\",\n"
                                               "        \"ageGrpCd\": \"\",\n"
                                               "        \"userNm\": \"\",\n"
                                               "        \"userId\": \"\",\n"
                                               "        \"userList\": \"'9829','9827','6795','6019'\",\n"
                                               "        \"userCnt\": 4,\n"
                                               "        \"custAnlysDiv\": \"Synthesis\"\n"
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
            - API NAME : WeeklySynthesisAnlys API
            - API DESC : CRM WeeklySynthesisAnlys 진입경로
                        ex) 분석 > 대시보드,비교분석,랭크 외 다른 메뉴로 진입 > 하단 비중분석에 항목 클릭 > 하단에 오더목록 > 고객명 클릭
            - API METHOD : POST
            - REQUEST PARAMS :
                (파라미터 이름, 타입, 최대길이, 설명, 필수여부, 비고)
                (ex/ cpId, varchar, 20, 조직ID, TRUE, 주노헤어=JN)
                |PARAM NAME|TYPE   |MAX LENGTH|REQUIRED|DESC|ETC     |
                |:--------:|:-----:|:--------:|:--:|:------:|:------:|
                |cpID      |varchar|20        |TRUE|기업아이디   |JN|
                |loginShopId    |varchar|20        |TRUE|로그인매장   |149|
                |loginId    |varchar|20        |TRUE|로그인아이디   |11273|
                |path    |varchar|20        |TRUE|메뉴패스   |/crm/anlys/cust-anlys-synth|
                |name    |varchar|20        |TRUE|메뉴명   |cust-anlys-synth|
                |standard    |varchar|20        |TRUE|조회기준 => 매장/디자이너   |DSGN|
                |shopNm    |varchar|20        |TRUE|-   |준오뷰티|
                |shopId    |varchar|20        |TRUE|매장아이디   |149|
                |shopList    |varchar|20        |TRUE|-   |'10'|
                |shopCnt    |varchar|20        |TRUE|-   |1|
                |term    |varchar|20        |TRUE|월/주/일 => month/week/day |week|
                |searchStDt    |varchar|20        |TRUE|조회시작일   |202201|
                |searchEdDt    |varchar|20        |TRUE|조회종료일   |202203|
                |searchQrtr    |varchar|20        |TRUE|-   ||
                |searchWeek    |varchar|20        |TRUE|조회주차   ||
                |empBuyYn    |varchar|20        |TRUE|-   ||
                |ordTpCd    |varchar|20        |TRUE|-   ||
                |trmTpCd    |varchar|20        |TRUE|-   ||
                |payDivCd    |varchar|20        |TRUE|-   ||
                |custClsfcCd    |varchar|20        |TRUE|-   ||
                |mbrGrdCd    |varchar|20        |TRUE|-   ||
                |prpTpCd    |varchar|20        |TRUE|-   ||
                |tktTpCd    |varchar|20        |TRUE|횟수권유형코드   ||
                |prdcBrndCd    |varchar|20        |TRUE|-   |null|
                |gndrCd    |varchar|20        |TRUE|-   ||
                |joinTpCd    |varchar|20        |TRUE|-   ||
                |ageGrpCd    |varchar|20        |TRUE|-   ||
                |userNm    |varchar|20        |TRUE|-   ||
                |userId    |varchar|20        |TRUE|디자이너아이디   ||
                |userList    |varchar|20        |TRUE|디자이너아이디목록   |'9829','9827','6795','6019'|
                |userCnt    |varchar|20        |TRUE|-   |4|
                |custAnlysDiv    |varchar|20        |TRUE|-   |Synthesis|

                -SAMPLE JSON
                ```
                {
                    "cpId": "JN",
                    "loginShopId": "149",
                    "loginId": "11273",
                    "path": "/crm/anlys/cust-anlys-synth",
                    "name": "cust-anlys-synth",
                    "standard": "DSGN",
                    "shopNm": "준오뷰티",
                    "shopId": "149",
                    "shopList": "'10'",
                    "shopCnt": 1,
                    "term": "week",
                    "searchStDt": "202201",
                    "searchEdDt": "202203",
                    "searchQrtr": "",
                    "searchWeek": "",
                    "empBuyYn": "",
                    "ordTpCd": "",
                    "trmTpCd": "",
                    "payDivCd": "",
                    "custClsfcCd": "",
                    "mbrGrdCd": "",
                    "prpTpCd": "",
                    "tktTpCd": "",
                    "prdcBrndCd": null,
                    "gndrCd": "",
                    "joinTpCd": "",
                    "ageGrpCd": "",
                    "userNm": "",
                    "userId": "",
                    "userList": "'9829','9827','6795','6019'",
                    "userCnt": 4,
                    "custAnlysDiv": "Synthesis"
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
        service: AnalysisWeeklySynthesisAnlysService = container.analysisWeeklySynthesisAnlysCrmServiceProvider()

        try:
            result = service.analysis_weekly_synthesis_anlys_crm(request.data,
                                                                 accessToken=kwargs.get('accessToken', 'None'),
                                                                 refreshToken=kwargs.get('refreshToken', 'None'))
        except Exception as ex:
            print(f"{self.__class__.__name__} : Controller post error ==> {ex}")
            return Response(ex.__dict__, status=500)

        return Response(result, status=200)
        # return Response({"result": "CRM CONTROLLER GENERATE TEST"}, status=200)
