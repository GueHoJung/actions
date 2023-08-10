from dependency_injector.wiring import inject
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import APIView

from ...application.service.analysis_user_cust_count_compare_service import AnalysisUserCustCountCompareService
from ...serializers import PostRequestSerializer
import config.utils.common_utils as common_utils
from config.utils.decorator import check_token

from config.base_container import BaseContainer


class AnalysisUserCustCountCompareApiController(APIView):
    """
    # CLASS : AnalysisUserCustCountCompareApiController
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/08 8:48 PM
    # DESCRIPTION
        - AnalysisUserCustCountCompareApiController
        - UserCustCountCompare API
        - CRM 디렉터리 : analysis
        - CRM 서비스 설명 : 분석 비교분석 고객수비교분석
        - CRM 서비스 호출 url : /analysis/getUserCustCountCompare/
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

    @swagger_auto_schema(tags=['CRM SYSTEM - Analysis API'], operation_summary="CRM Analysis UserCustCountCompare API",
                         operation_description="# DESIGNER SEVER에서 CRM SYSTEM으로 UserCustCountCompare 요청 API\n"
                                               "\n"
                                               "|PARAM NAME|TYPE   |MAX LENGTH|REQUIRED|DESC|ETC     |\n"
                                               "|:--------:|:-----:|:--------:|:--:|:------:|:------:|\n"
                                               "|cpID      |varchar|20        |TRUE|기업아이디   |JN|\n"
                                               "|loginShopId      |varchar|20        |TRUE|로그인매장   |103|\n"
                                               "|loginId      |varchar|20        |TRUE|로그인아이디   |11273|\n"
                                               "|path      |varchar|20        |TRUE|메뉴패스   |/crm/anlys/cmpr-anlys-cust-count|\n"
                                               "|name      |varchar|20        |TRUE|메뉴명   |cmpr-anlys-cust-count|\n"
                                               "|standard      |varchar|20        |TRUE|조회기준=>매장/디자이너   |DSGN|\n"
                                               "|shopNm      |varchar|20        |TRUE|매장이름   |안산중앙2호점|\n"
                                               "|shopId      |varchar|20        |TRUE|매장아이디   |100|\n"
                                               "|shopList      |varchar|20        |TRUE|매장아이디목록   ||\n"
                                               "|shopCnt      |varchar|20        |TRUE|매장수   |0|\n"
                                               "|term      |varchar|20        |TRUE|월/분기/연도 => month/qrtr/year   |qrtr|\n"
                                               "|searchStDt      |varchar|20        |TRUE|조회시작일   |202210|\n"
                                               "|searchEdDt      |varchar|20        |TRUE|조회종료일   |202303|\n"
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
                                               "|userNm      |varchar|20        |TRUE|디자이너이름   |민영|\n"
                                               "|userId      |varchar|20        |TRUE|디자이너아이디   |9354|\n"
                                               "|userList      |varchar|20        |TRUE|디자이너아이디목록   ||\n"
                                               "|userCnt      |varchar|20        |TRUE|디자이너수   |0|\n"
                                               "|searchStDtOrg      |varchar|20        |TRUE|-   |202301|\n"
                                               "|searchEdDtOrg      |varchar|20        |TRUE|-   |202303|\n"
                                               "|isChart      |varchar|20        |TRUE|-   |true|\n"
                                               "|chartTerm      |varchar|20        |TRUE|-   |qrtr|\n"
                                               "|chart      |varchar|20        |TRUE|-   |rgn|\n"
                                               "|searchDiv      |varchar|20        |TRUE|-   |custCnt|\n"
                                               "\n"
                                               "### Data type : json\n"
                                               "```\n"
                                               "{\n"
                                               "        \"cpId\": \"JN\",\n"
                                               "        \"loginShopId\": \"103\",\n"
                                               "        \"loginId\": \"11273\",\n"
                                               "        \"path\": \"/crm/anlys/cmpr-anlys-cust-count\",\n"
                                               "        \"name\": \"cmpr-anlys-cust-count\",\n"
                                               "        \"standard\": \"DSGN\",\n"
                                               "        \"shopNm\": \"안산중앙2호점\",\n"
                                               "        \"shopId\": \"100\",\n"
                                               "        \"shopList\": \"\",\n"
                                               "        \"shopCnt\": 0,\n"
                                               "        \"term\": \"qrtr\",\n"
                                               "        \"searchStDt\": \"202210\",\n"
                                               "        \"searchEdDt\": \"202303\",\n"
                                               "        \"searchQrtr\": \"1\",\n"
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
                                               "        \"userNm\": \"민영\",\n"
                                               "        \"userId\": \"9354\",\n"
                                               "        \"userList\": \"\",\n"
                                               "        \"userCnt\": 0,\n"
                                               "        \"searchStDtOrg\": \"202301\",\n"
                                               "        \"searchEdDtOrg\": \"202303\",\n"
                                               "        \"isChart\": true,\n"
                                               "        \"chartTerm\": \"qrtr\",\n"
                                               "        \"chart\": \"rgn\",\n"
                                               "        \"searchDiv\": \"custCnt\"\n"
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
            - API NAME : UserCustCountCompare API
            - API DESC : CRM UserCustCountCompare 진입경로
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
                |path      |varchar|20        |TRUE|메뉴패스   |/crm/anlys/cmpr-anlys-cust-count|
                |name      |varchar|20        |TRUE|메뉴명   |cmpr-anlys-cust-count|
                |standard      |varchar|20        |TRUE|조회기준=>매장/디자이너   |DSGN|
                |shopNm      |varchar|20        |TRUE|매장이름   |안산중앙2호점|
                |shopId      |varchar|20        |TRUE|매장아이디   |100|
                |shopList      |varchar|20        |TRUE|매장아이디목록   ||
                |shopCnt      |varchar|20        |TRUE|매장수   |0|
                |term      |varchar|20        |TRUE|월/분기/연도 => month/qrtr/year   |qrtr|
                |searchStDt      |varchar|20        |TRUE|조회시작일   |202210|
                |searchEdDt      |varchar|20        |TRUE|조회종료일   |202303|
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
                |userNm      |varchar|20        |TRUE|디자이너이름   |민영|
                |userId      |varchar|20        |TRUE|디자이너아이디   |9354|
                |userList      |varchar|20        |TRUE|디자이너아이디목록   ||
                |userCnt      |varchar|20        |TRUE|디자이너수   |0|
                |searchStDtOrg      |varchar|20        |TRUE|-   |202301|
                |searchEdDtOrg      |varchar|20        |TRUE|-   |202303|
                |isChart      |varchar|20        |TRUE|-   |true|
                |chartTerm      |varchar|20        |TRUE|-   |qrtr|
                |chart      |varchar|20        |TRUE|-   |rgn|
                |searchDiv      |varchar|20        |TRUE|-   |custCnt|

                -SAMPLE JSON
                ```
                {
                    "cpId": "JN",
                    "loginShopId": "103",
                    "loginId": "11273",
                    "path": "/crm/anlys/cmpr-anlys-cust-count",
                    "name": "cmpr-anlys-cust-count",
                    "standard": "DSGN",
                    "shopNm": "안산중앙2호점",
                    "shopId": "100",
                    "shopList": "",
                    "shopCnt": 0,
                    "term": "qrtr",
                    "searchStDt": "202210",
                    "searchEdDt": "202303",
                    "searchQrtr": "1",
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
                    "userNm": "민영",
                    "userId": "9354",
                    "userList": "",
                    "userCnt": 0,
                    "searchStDtOrg": "202301",
                    "searchEdDtOrg": "202303",
                    "isChart": true,
                    "chartTerm": "qrtr",
                    "chart": "rgn",
                    "searchDiv": "custCnt"
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
        service: AnalysisUserCustCountCompareService = container.analysisUserCustCountCompareCrmServiceProvider()

        try:
            result = service.analysis_user_cust_count_compare_crm(request.data,
                                                                  accessToken=kwargs.get('accessToken', 'None'),
                                                                  refreshToken=kwargs.get('refreshToken', 'None'))
        except Exception as ex:
            print(f"{self.__class__.__name__} : Controller post error ==> {ex}")
            return Response(ex.__dict__, status=500)

        return Response(result, status=200)
        # return Response({"result": "CRM CONTROLLER GENERATE TEST"}, status=200)
