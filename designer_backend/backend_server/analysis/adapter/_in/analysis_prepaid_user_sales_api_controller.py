from dependency_injector.wiring import inject
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import APIView

from ...application.service.analysis_prepaid_user_sales_service import AnalysisPrepaidUserSalesService
from ...serializers import PostRequestSerializer
import config.utils.common_utils as common_utils
from config.utils.decorator import check_token

from config.base_container import BaseContainer


class AnalysisPrepaidUserSalesApiController(APIView):
    """
    # CLASS : AnalysisPrepaidUserSalesApiController
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/31 4:44 PM
    # DESCRIPTION
        - AnalysisPrepaidUserSalesApiController
        - PrepaidUserSales API
        - CRM 디렉터리 : analysis
        - CRM 서비스 설명 : 분석 매출분석 회원권분석 (디자이너 별)
        - CRM 서비스 호출 url : /analysis/getPrepaidUserSales/
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
            prpTpCd (선불권유형코드)*
            userList (디자이너아이디목록)*
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/31          jung-gyuho          최초 생성
    """

    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(tags=['CRM SYSTEM - Analysis API'], operation_summary="CRM Analysis PrepaidUserSales API",
                         operation_description="# DESIGNER SEVER에서 CRM SYSTEM으로 PrepaidUserSales 요청 API\n"
                                               "\n"
                                               "|PARAM NAME|TYPE   |MAX LENGTH|DESC|REQUIRED|ETC     |\n"
                                               "|:--------:|:-----:|:--------:|:--:|:------:|:------:|\n"
                                               "|cpID      |varchar|20        |TRUE|기업아이디   |JN|\n"
                                               "|loginShopId    |varchar|20        |TRUE|로그인매장   |1801141|\n"
                                               "|loginId    |varchar|20        |TRUE|로그인아이디   |PR000000001801141D001|\n"
                                               "|path    |varchar|20        |TRUE|메뉴패스   |20200801|\n"
                                               "|name    |varchar|20        |TRUE|메뉴명   |20220801|\n"
                                               "|standard    |varchar|20        |TRUE|조회기준 => 매장/디자이너   |\"\"|\n"
                                               "|shopId    |varchar|20        |TRUE|매장아이디   |\"\"|\n"
                                               "|term    |varchar|20        |TRUE|월/주/일 => month/week/day   |\"\"|\n"
                                               "|searchStDt    |varchar|20        |TRUE|조회시작일   |\"\"|\n"
                                               "|searchEdDt    |varchar|20        |TRUE|조회종료일   |\"\"|\n"
                                               "|searchWeek    |varchar|20        |TRUE|조회주차   |\"\"|\n"
                                               "|prpTpCd    |varchar|20        |TRUE|선불권유형코드   |\"\"|\n"
                                               "|userList    |varchar|20        |TRUE|디자이너아이디목록   |\"\"|\n"
                                               "\n"
                                               "### Data type : json\n"
                                               "```\n"
                                               "{\n"
                                               "    \"cpId\": \"**\",\n"
                                               "    \"shopId\": \"***\",\n"
                                               "    \"custId\": \"juno*****\",\n"
                                               "}",
                         request_body=PostRequestSerializer, responses={200: 'Success'})
    @inject
    @check_token
    def post(self, request, *args, **kwargs):
        """
        # API : post
        # AUTHOR : jung-gyuho
        # TIME : 2023/07/27 6:02 PM
        # DESCRIPTION
            - API NAME : PrepaidUserSales API
            - API DESC : CRM PrepaidUserSales 진입경로
                        ex) 분석 > 대시보드,비교분석,랭크 외 다른 메뉴로 진입 > 하단 비중분석에 항목 클릭 > 하단에 오더목록 > 고객명 클릭
            - API METHOD : POST
            - REQUEST PARAMS :
                (파라미터 이름, 타입, 최대길이, 설명, 필수여부, 비고)
                (ex/ cpId, varchar, 20, 조직ID, TRUE, 주노헤어=JN)
                |PARAM NAME|TYPE   |MAX LENGTH|DESC|REQUIRED|ETC     |
                |:--------:|:-----:|:--------:|:--:|:------:|:------:|
                |cpID      |varchar|20        |TRUE|기업아이디   |주노헤어=JN|
                |loginShopId    |varchar|20        |TRUE|로그인매장   |아무개=1234123|
                |loginId    |varchar|20        |TRUE|로그인아이디   |A매장=7|
                |path    |varchar|20        |TRUE|메뉴패스   |A매장=7|
                |name    |varchar|20        |TRUE|메뉴명   |A매장=7|
                |standard    |varchar|20        |TRUE|조회기준 => 매장/디자이너   |A매장=7|
                |shopId    |varchar|20        |TRUE|매장아이디   |A매장=7|
                |term    |varchar|20        |TRUE|월/주/일 => month/week/day   |A매장=7|
                |searchStDt    |varchar|20        |TRUE|조회시작일   |A매장=7|
                |searchEdDt    |varchar|20        |TRUE|조회종료일   |A매장=7|
                |searchWeek    |varchar|20        |TRUE|조회주차   |A매장=7|
                |prpTpCd    |varchar|20        |TRUE|선불권유형코드   |A매장=7|
                |userList    |varchar|20        |TRUE|디자이너아이디목록   |A매장=7|

                -SAMPLE JSON
                ```
                {
                    "cpId": "JN",
                    "loginShopId": "149",
                    "loginId": "11273",
                    "path": "/crm/anlys/sales-anlys-prpd",
                    "name": "sales-anlys-prpd",
                    "standard": "DSGN",
                    "shopNm": "준오뷰티",
                    "shopId": "149",
                    "shopList": "'1','10','100','101','102','103','104','105','106','107','108','109','11','110','111','112','12','128','129','13','130','131','132','133','134','135','136','137','139','14','140','141','142','143','144','147','148','149','15','150','151','152','153','154','155','156','157','158','159','16','160','161','162','163','164','165','166','167','168','169','170','171','172','173','174','175','176','177','178','179','18','180','181','182','183','184','185','186','187','188','189','19','190','191','192','193','194','195','196','197','198','199','2','20','200','201','202','203','204','205','206','207','208','209','21','210','211','212','213','214','215','216','217','218','219','22','220','221','222','223','224','23','24','25','26','27','28','29','3','30','31','32','33','34','35','36','37','38','39','4','40','41','42','43','44','45','46','47','48','5','51','52','54','55','56','57','58','59','6','60','61','62','63','64','65','66','67','68','69','7','70','71','72','73','74','75','76','77','78','79','8','80','81','82','83','84','85','86','87','88','89','9','90','91','94','999'",
                    "shopCnt": 196,
                    "term": "month",
                    "searchStDt": "202306",
                    "searchEdDt": "202307",
                    "searchQrtr": "",
                    "searchWeek": "",
                    "empBuyYn": "",
                    "ordTpCd": "PRP",
                    "trmTpCd": "",
                    "payDivCd": "'DGN','SHP'",
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
                    "userList": "",
                    "userCnt": 0,
                    "isChart": true,
                    "chartTerm": "month",
                    "chart": "saleUse",
                    "subChart": "sale",
                    "isPrpOrder": true,
                    "ordTpCdList": "'PRP','TRM','PRD'"
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
        service: AnalysisPrepaidUserSalesService = container.analysisPrepaidUserSalesCrmServiceProvider()

        try:
            result = service.analysis_prepaid_user_sales_crm(request.data, accessToken=kwargs.get('accessToken', 'None'),
                                                     refreshToken=kwargs.get('refreshToken', 'None'))
        except Exception as ex:
            print(f"{self.__class__.__name__} : Controller post error ==> {ex}")
            return Response(ex.__dict__, status=500)

        return Response(result, status=200)
        # return Response({"result": "CRM CONTROLLER GENERATE TEST"}, status=200)
