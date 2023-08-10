from dependency_injector.wiring import inject
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import APIView

from ...application.service.analysis_user_trm_type_compare_service import AnalysisUserTrmTypeCompareService
from ...serializers import PostRequestSerializer
import config.utils.common_utils as common_utils
from config.utils.decorator import check_token

from config.base_container import BaseContainer


class AnalysisUserTrmTypeCompareApiController(APIView):
    """
    # CLASS : AnalysisUserTrmTypeCompareApiController
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/08 9:08 PM
    # DESCRIPTION
        - AnalysisUserTrmTypeCompareApiController
        - UserTrmTypeCompare API
        - CRM 디렉터리 : analysis
        - CRM 서비스 설명 : 분석 비교분석 시술유형비교분석
        - CRM 서비스 호출 url : /analysis/getUserTrmTypeCompare/
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
            term (월/분기/연도 => month/qrtr/year)
            searchStDt (조회시작일)
            searchEdDt (조회종료일)
            userId (디자이너아이디)
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/08          jung-gyuho          최초 생성
    """

    # permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(tags=['CRM SYSTEM - Analysis API'], operation_summary="CRM Analysis UserTrmTypeCompare API",
                         operation_description="# DESIGNER SEVER에서 CRM SYSTEM으로 UserTrmTypeCompare 요청 API\n"
                                               "\n"
                                               "|PARAM NAME|TYPE   |MAX LENGTH|REQUIRED|DESC|ETC     |\n"
                                               "|:--------:|:-----:|:--------:|:--:|:------:|:------:|\n"
                                               "|cpID      |varchar|20        |TRUE|기업아이디   |JN|\n"
                                               "|loginShopId      |varchar|20        |TRUE|로그인매장   |103|\n"
                                               "|loginId      |varchar|20        |TRUE|로그인아이디   |11273|\n"
                                               "|path      |varchar|20        |TRUE|메뉴패스   |/crm/anlys/cmpr-anlys-trm-type|\n"
                                               "|name      |varchar|20        |TRUE|메뉴명   |cmpr-anlys-trm-type|\n"
                                               "|standard      |varchar|20        |TRUE|조회기준=>매장/디자이너   |DSGN|\n"
                                               "|shopNm      |varchar|20        |TRUE|매장이름   |가든서현역점|\n"
                                               "|shopId      |varchar|20        |TRUE|매장아이디   |103|\n"
                                               "|shopList      |varchar|20        |TRUE|매장아이디목록   ||\n"
                                               "|shopCnt      |varchar|20        |TRUE|매장수   |0|\n"
                                               "|term      |varchar|20        |TRUE|월/분기/연도 => month/qrtr/year   |year|\n"
                                               "|searchStDt      |varchar|20        |TRUE|조회시작일   |2022|\n"
                                               "|searchEdDt      |varchar|20        |TRUE|조회종료일   |2022|\n"
                                               "|searchQrtr      |varchar|20        |TRUE|조회분기   |1|\n"
                                               "|searchWeek      |varchar|20        |TRUE|조회주차   ||\n"
                                               "|empBuyYn      |varchar|20        |TRUE|직원오더여부   ||\n"
                                               "|ordTpCd      |varchar|20        |TRUE|오더유형코드   ||\n"
                                               "|trmTpCd      |varchar|20        |TRUE|시술유형코드   ||\n"
                                               "|payDivCd      |varchar|20        |TRUE|결제유형코드   ||\n"
                                               "|custClsfcCdID      |varchar|20        |TRUE|고객유형코드   ||\n"
                                               "|mbrGrdCd      |varchar|20        |TRUE|멤버십등급코드   ||\n"
                                               "|prpTpCd      |varchar|20        |TRUE|회원권유형코드   ||\n"
                                               "|tktTpCd      |varchar|20        |TRUE|횟수권유형코드   ||\n"
                                               "|prdcBrndCd      |varchar|20        |TRUE|점판브랜드코드   |null|\n"
                                               "|gndrCd      |varchar|20        |TRUE|성별코드   ||\n"
                                               "|joinTpCd      |varchar|20        |TRUE|유입경로코드   ||\n"
                                               "|ageGrpCd      |varchar|20        |TRUE|-   ||\n"
                                               "|userNm      |varchar|20        |TRUE|디자이너이름   |김조한|\n"
                                               "|userId      |varchar|20        |TRUE|디자이너아이디   |1956|\n"
                                               "|userList      |varchar|20        |TRUE|디자이너아이디목록   ||\n"
                                               "|userCnt      |varchar|20        |TRUE|디자이너수   |0|\n"
                                               "|searchStDtOrg      |varchar|20        |TRUE|-   |2022|\n"
                                               "|searchEdDtOrg      |varchar|20        |TRUE|-   |2022|\n"
                                               "|isChart      |varchar|20        |TRUE|-   |true|\n"
                                               "|chartTerm      |varchar|20        |TRUE|-   |year|\n"
                                               "|chart      |varchar|20        |TRUE|-   |rgn|\n"
                                               "|dvsn      |varchar|20        |TRUE|-   |rgn|\n"
                                               "|seaitemGrpCdrchDiv      |varchar|20        |TRUE|-   |PRM|\n"
                                               "\n"
                                               "### Data type : json\n"
                                               "```\n"
                                               "{\n"
                                               "        \"cpId\": \"JN\",\n"
                                               "        \"loginShopId\": \"103\",\n"
                                               "        \"loginId\": \"11273\",\n"
                                               "        \"path\": \"/crm/anlys/cmpr-anlys-trm-type\",\n"
                                               "        \"name\": \"cmpr-anlys-trm-type\",\n"
                                               "        \"standard\": \"DSGN\",\n"
                                               "        \"shopNm\": \"가든서현역점\",\n"
                                               "        \"shopId\": \"103\",\n"
                                               "        \"shopList\": \"\",\n"
                                               "        \"shopCnt\": 0,\n"
                                               "        \"term\": \"year\",\n"
                                               "        \"searchStDt\": \"2022\",\n"
                                               "        \"searchEdDt\": \"2022\",\n"
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
                                               "        \"userNm\": \"김조한\",\n"
                                               "        \"userId\": \"1956\",\n"
                                               "        \"userList\": \"\",\n"
                                               "        \"userCnt\": 0,\n"
                                               "        \"searchStDtOrg\": \"2022\",\n"
                                               "        \"searchEdDtOrg\": \"2022\",\n"
                                               "        \"isChart\": true,\n"
                                               "        \"chartTerm\": \"year\",\n"
                                               "        \"chart\": \"rgn\",\n"
                                               "        \"dvsn\": \"rgn\",\n"
                                               "        \"itemGrpCd\": \"PRM\"\n"
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
            - API NAME : UserTrmTypeCompare API
            - API DESC : CRM UserTrmTypeCompare 진입경로
                        ex) 분석 > 대시보드,비교분석,랭크 외 다른 메뉴로 진입 > 하단 비중분석에 항목 클릭 > 하단에 오더목록 > 고객명 클릭
            - API METHOD : POST
            - REQUEST PARAMS :
                (파라미터 이름, 타입, 최대길이, 설명, 필수여부, 비고)
                (ex/ cpId, varchar, 20, 조직ID, TRUE, 주노헤어=JN)
                |PARAM NAME|TYPE   |MAX LENGTH|REQUIRED|DESC|ETC     |
                |:--------:|:-----:|:--------:|:--:|:------:|:------:|
                |cpID      |varchar|20        |TRUE|기업아이디   |JN|
                |loginShopId      |varchar|20        |TRUE|로그인매장   |103|
                |loginId      |varchar|20        |TRUE|로그인아이디   |11273|
                |path      |varchar|20        |TRUE|메뉴패스   |/crm/anlys/cmpr-anlys-trm-type|
                |name      |varchar|20        |TRUE|메뉴명   |cmpr-anlys-trm-type|
                |standard      |varchar|20        |TRUE|조회기준=>매장/디자이너   |DSGN|
                |shopNm      |varchar|20        |TRUE|매장이름   |가든서현역점|
                |shopId      |varchar|20        |TRUE|매장아이디   |103|
                |shopList      |varchar|20        |TRUE|매장아이디목록   ||
                |shopCnt      |varchar|20        |TRUE|매장수   |0|
                |term      |varchar|20        |TRUE|월/분기/연도 => month/qrtr/year   |year|
                |searchStDt      |varchar|20        |TRUE|조회시작일   |2022|
                |searchEdDt      |varchar|20        |TRUE|조회종료일   |2022|
                |searchQrtr      |varchar|20        |TRUE|조회분기   |1|
                |searchWeek      |varchar|20        |TRUE|조회주차   ||
                |empBuyYn      |varchar|20        |TRUE|직원오더여부   ||
                |ordTpCd      |varchar|20        |TRUE|오더유형코드   ||
                |trmTpCd      |varchar|20        |TRUE|시술유형코드   ||
                |payDivCd      |varchar|20        |TRUE|결제유형코드   ||
                |custClsfcCdID      |varchar|20        |TRUE|고객유형코드   ||
                |mbrGrdCd      |varchar|20        |TRUE|멤버십등급코드   ||
                |prpTpCd      |varchar|20        |TRUE|회원권유형코드   ||
                |tktTpCd      |varchar|20        |TRUE|횟수권유형코드   ||
                |prdcBrndCd      |varchar|20        |TRUE|점판브랜드코드   |null|
                |gndrCd      |varchar|20        |TRUE|성별코드   ||
                |joinTpCd      |varchar|20        |TRUE|유입경로코드   ||
                |ageGrpCd      |varchar|20        |TRUE|-   ||
                |userNm      |varchar|20        |TRUE|디자이너이름   |김조한|
                |userId      |varchar|20        |TRUE|디자이너아이디   |1956|
                |userList      |varchar|20        |TRUE|디자이너아이디목록   ||
                |userCnt      |varchar|20        |TRUE|디자이너수   |0|
                |searchStDtOrg      |varchar|20        |TRUE|-   |2022|
                |searchEdDtOrg      |varchar|20        |TRUE|-   |2022|
                |isChart      |varchar|20        |TRUE|-   |true|
                |chartTerm      |varchar|20        |TRUE|-   |year|
                |chart      |varchar|20        |TRUE|-   |rgn|
                |dvsn      |varchar|20        |TRUE|-   |rgn|
                |seaitemGrpCdrchDiv      |varchar|20        |TRUE|-   |PRM|

                -SAMPLE JSON
                ```
                {
                    "cpId": "JN",
                    "loginShopId": "103",
                    "loginId": "11273",
                    "path": "/crm/anlys/cmpr-anlys-trm-type",
                    "name": "cmpr-anlys-trm-type",
                    "standard": "DSGN",
                    "shopNm": "가든서현역점",
                    "shopId": "103",
                    "shopList": "",
                    "shopCnt": 0,
                    "term": "year",
                    "searchStDt": "2022",
                    "searchEdDt": "2022",
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
                    "userNm": "김조한",
                    "userId": "1956",
                    "userList": "",
                    "userCnt": 0,
                    "searchStDtOrg": "2022",
                    "searchEdDtOrg": "2022",
                    "isChart": true,
                    "chartTerm": "year",
                    "chart": "rgn",
                    "dvsn": "rgn",
                    "itemGrpCd": "PRM"
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
        service: AnalysisUserTrmTypeCompareService = container.analysisUserTrmTypeCompareCrmServiceProvider()

        try:
            result = service.analysis_user_trm_type_compare_crm(request.data,
                                                                accessToken=kwargs.get('accessToken', 'None'),
                                                                refreshToken=kwargs.get('refreshToken', 'None'))
        except Exception as ex:
            print(f"{self.__class__.__name__} : Controller post error ==> {ex}")
            return Response(ex.__dict__, status=500)

        return Response(result, status=200)
        # return Response({"result": "CRM CONTROLLER GENERATE TEST"}, status=200)
