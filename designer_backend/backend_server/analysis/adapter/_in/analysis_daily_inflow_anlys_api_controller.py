from dependency_injector.wiring import inject
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import APIView

from ...application.service.analysis_daily_inflow_anlys_service import AnalysisDailyInflowAnlysService
from ...serializers import PostRequestSerializer
import config.utils.common_utils as common_utils
from config.utils.decorator import check_token

from config.base_container import BaseContainer


class AnalysisDailyInflowAnlysApiController(APIView):
    """
    # CLASS : AnalysisDailyInflowAnlysApiController
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/08 3:17 PM
    # DESCRIPTION
        - AnalysisDailyInflowAnlysApiController
        - DailyInflowAnlys API
        - CRM 디렉터리 : analysis
        - CRM 서비스 설명 :
        - CRM 서비스 호출 url :
        - CRM 서비스 호출 method : POST
        - CRM 서비스 호출 body : json
        - CRM 서비스 호출 파라미터 :
            cpId (기업아이디)
            shopId (매장아이디)
            custId (고객아이디)
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/08          jung-gyuho          최초 생성
    """

    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(tags=['CRM SYSTEM - Analysis API'], operation_summary="CRM Analysis DailyInflowAnlys API",
                         operation_description="# DESIGNER SEVER에서 CRM SYSTEM으로 DailyInflowAnlys 요청 API\n"
                                               "\n"
                                               "|PARAM NAME|TYPE   |MAX LENGTH|REQUIRED|DESC|ETC     |\n"
                                               "|:--------:|:-----:|:--------:|:--:|:------:|:------:|\n"
                                               "|cpID      |varchar|20        |TRUE|기업아이디   |JN|\n"
                                               "|loginShopId    |varchar|20        |TRUE|로그인매장   |149|\n"
                                               "|loginId    |varchar|20        |TRUE|로그인아이디   |11273|\n"
                                               "|path    |varchar|20        |TRUE|메뉴패스   |/crm/anlys/cust-anlys-inflw|\n"
                                               "|name    |varchar|20        |TRUE|메뉴명   |cust-anlys-inflw|\n"
                                               "|standard    |varchar|20        |TRUE|조회기준 => 매장/디자이너   |DSGN|\n"
                                               "|shopNm    |varchar|20        |TRUE|-   |가든서현역점|\n"
                                               "|shopId    |varchar|20        |TRUE|매장아이디   |103|\n"
                                               "|shopList    |varchar|20        |TRUE|-   |'10'|\n"
                                               "|shopCnt    |varchar|20        |TRUE|-   |1|\n"
                                               "|term    |varchar|20        |TRUE|월/주/일 => month/week/day  |day|\n"
                                               "|searchStDt    |varchar|20        |TRUE|조회시작일   |20221201|\n"
                                               "|searchEdDt    |varchar|20        |TRUE|조회종료일   |20221231|\n"
                                               "|searchQrtr    |varchar|20        |TRUE|-   ||\n"
                                               "|searchWeek    |varchar|20        |TRUE|조회주차   |3|\n"
                                               "|empBuyYn    |varchar|20        |TRUE|-   ||\n"
                                               "|ordTpCd    |varchar|20        |TRUE|-   ||\n"
                                               "|trmTpCd    |varchar|20        |TRUE|-   ||\n"
                                               "|payDivCd    |varchar|20        |TRUE|-   ||\n"
                                               "|custClsfcCd    |varchar|20        |TRUE|-   ||\n"
                                               "|mbrGrdCd    |varchar|20        |TRUE|-   ||\n"
                                               "|prpTpCd    |varchar|20        |TRUE|-   ||\n"
                                               "|tktTpCd    |varchar|20        |TRUE|횟수권유형코드   ||\n"
                                               "|prdcBrndCd    |varchar|20        |TRUE|-   |null|\n"
                                               "|gndrCd    |varchar|20        |TRUE|성별코드   |'F','M'|\n"
                                               "|joinTpCd    |varchar|20        |TRUE|유입경로코드   |'01','07','08','09','10','11','99','06','03','04','02'|\n"
                                               "|ageGrpCd    |varchar|20        |TRUE|연령대코드   ||\n"
                                               "|userNm    |varchar|20        |TRUE|-   ||\n"
                                               "|userId    |varchar|20        |TRUE|디자이너아이디   ||\n"
                                               "|userList    |varchar|20        |TRUE|디자이너아이디목록   ||\n"
                                               "|userCnt    |varchar|20        |TRUE|-   |0|\n"
                                               "|realAgeGrpCd    |varchar|20        |TRUE|-   ||\n"
                                               "|custAnlysDiv    |varchar|20        |TRUE|-   |Inflow|\n"
                                               "\n"
                                               "### Data type : json\n"
                                               "```\n"
                                               "{\n"
                                               "        \"cpId\": \"JN\",\n"
                                               "        \"loginShopId\": \"103\",\n"
                                               "        \"loginId\": \"11273\",\n"
                                               "        \"path\": \"/crm/anlys/cust-anlys-inflw\",\n"
                                               "        \"name\": \"cust-anlys-inflw\",\n"
                                               "        \"standard\": \"DSGN\",\n"
                                               "        \"shopNm\": \"가든서현역점\",\n"
                                               "        \"shopId\": \"103\",\n"
                                               "        \"shopList\": \"'10'\",\n"
                                               "        \"shopCnt\": 1,\n"
                                               "        \"term\": \"day\",\n"
                                               "        \"searchStDt\": \"20221201\",\n"
                                               "        \"searchEdDt\": \"20221231\",\n"
                                               "        \"searchQrtr\": \"\",\n"
                                               "        \"searchWeek\": \"3\",\n"
                                               "        \"empBuyYn\": \"\",\n"
                                               "        \"ordTpCd\": \"\",\n"
                                               "        \"trmTpCd\": \"\",\n"
                                               "        \"payDivCd\": \"\",\n"
                                               "        \"custClsfcCd\": \"\",\n"
                                               "        \"mbrGrdCd\": \"\",\n"
                                               "        \"prpTpCd\": \"\",\n"
                                               "        \"tktTpCd\": \"\",\n"
                                               "        \"prdcBrndCd\": null,\n"
                                               "        \"gndrCd\": \"'F','M'\",\n"
                                               "        \"joinTpCd\": \"'01','07','08','09','10','11','99','06','03','04','02'\",\n"
                                               "        \"ageGrpCd\": \"\",\n"
                                               "        \"userNm\": \"\",\n"
                                               "        \"userId\": \"\",\n"
                                               "        \"userList\": \"\",\n"
                                               "        \"userCnt\": 0,\n"
                                               "        \"realAgeGrpCd\": \"\",\n"
                                               "        \"custAnlysDiv\": \"Inflow\"\n"
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
            - API NAME : DailyInflowAnlys API
            - API DESC : CRM DailyInflowAnlys 진입경로
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
                |path    |varchar|20        |TRUE|메뉴패스   |/crm/anlys/cust-anlys-inflw|
                |name    |varchar|20        |TRUE|메뉴명   |cust-anlys-inflw|
                |standard    |varchar|20        |TRUE|조회기준 => 매장/디자이너   |DSGN|
                |shopNm    |varchar|20        |TRUE|-   |가든서현역점|
                |shopId    |varchar|20        |TRUE|매장아이디   |103|
                |shopList    |varchar|20        |TRUE|-   |'10'|
                |shopCnt    |varchar|20        |TRUE|-   |1|
                |term    |varchar|20        |TRUE|월/주/일 => month/week/day  |day|
                |searchStDt    |varchar|20        |TRUE|조회시작일   |20221201|
                |searchEdDt    |varchar|20        |TRUE|조회종료일   |20221231|
                |searchQrtr    |varchar|20        |TRUE|-   ||
                |searchWeek    |varchar|20        |TRUE|조회주차   |3|
                |empBuyYn    |varchar|20        |TRUE|-   ||
                |ordTpCd    |varchar|20        |TRUE|-   ||
                |trmTpCd    |varchar|20        |TRUE|-   ||
                |payDivCd    |varchar|20        |TRUE|-   ||
                |custClsfcCd    |varchar|20        |TRUE|-   ||
                |mbrGrdCd    |varchar|20        |TRUE|-   ||
                |prpTpCd    |varchar|20        |TRUE|-   ||
                |tktTpCd    |varchar|20        |TRUE|횟수권유형코드   ||
                |prdcBrndCd    |varchar|20        |TRUE|-   |null|
                |gndrCd    |varchar|20        |TRUE|성별코드   |'F','M'|
                |joinTpCd    |varchar|20        |TRUE|유입경로코드   |'01','07','08','09','10','11','99','06','03','04','02'|
                |ageGrpCd    |varchar|20        |TRUE|연령대코드   ||
                |userNm    |varchar|20        |TRUE|-   ||
                |userId    |varchar|20        |TRUE|디자이너아이디   ||
                |userList    |varchar|20        |TRUE|디자이너아이디목록   ||
                |userCnt    |varchar|20        |TRUE|-   |0|
                |realAgeGrpCd    |varchar|20        |TRUE|-   ||
                |custAnlysDiv    |varchar|20        |TRUE|-   |Inflow|

                -SAMPLE JSON
                ```
                {
                    "cpId": "JN",
                    "loginShopId": "103",
                    "loginId": "11273",
                    "path": "/crm/anlys/cust-anlys-inflw",
                    "name": "cust-anlys-inflw",
                    "standard": "DSGN",
                    "shopNm": "가든서현역점",
                    "shopId": "103",
                    "shopList": "'10'",
                    "shopCnt": 1,
                    "term": "day",
                    "searchStDt": "20221201",
                    "searchEdDt": "20221231",
                    "searchQrtr": "",
                    "searchWeek": "3",
                    "empBuyYn": "",
                    "ordTpCd": "",
                    "trmTpCd": "",
                    "payDivCd": "",
                    "custClsfcCd": "",
                    "mbrGrdCd": "",
                    "prpTpCd": "",
                    "tktTpCd": "",
                    "prdcBrndCd": null,
                    "gndrCd": "'F','M'",
                    "joinTpCd": "'01','07','08','09','10','11','99','06','03','04','02'",
                    "ageGrpCd": "",
                    "userNm": "",
                    "userId": "",
                    "userList": "",
                    "userCnt": 0,
                    "realAgeGrpCd": "",
                    "custAnlysDiv": "Inflow"
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
        service: AnalysisDailyInflowAnlysService = container.analysisDailyInflowAnlysCrmServiceProvider()

        try:
            result = service.analysis_daily_inflow_anlys_crm(request.data,
                                                             accessToken=kwargs.get('accessToken', 'None'),
                                                             refreshToken=kwargs.get('refreshToken', 'None'))
        except Exception as ex:
            print(f"{self.__class__.__name__} : Controller post error ==> {ex}")
            return Response(ex.__dict__, status=500)

        return Response(result, status=200)
        # return Response({"result": "CRM CONTROLLER GENERATE TEST"}, status=200)
