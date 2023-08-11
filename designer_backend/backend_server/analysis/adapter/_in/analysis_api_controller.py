from dependency_injector.wiring import inject
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import APIView

from ...serializers import PostRequestSerializer
from ...application.service.analysis_service import AnalysisService
import config.utils.common_utils as common_utils
from config.utils.decorator import check_token

from config.base_container import BaseContainer


class AnalysisApiController(APIView):
    """
    # CLASS : AnalysisApiController
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/27 5:58 PM
    # DESCRIPTION
        - Analysis Controller
        - 고객 상세 분석 API
        - CRM 디렉터리 : analysis
        - CRM 서비스 호출 url : /analysis/getCustDetailAnlys/
        - CRM 서비스 호출 method : POST
        - CRM 서비스 호출 body : json
        - CRM 서비스 호출 파라미터 :
            cpId (기업아이디)
            shopId (매장아이디)
            custId (고객아이디)
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/27          jung-gyuho          최초 생성
    """

    # permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(tags=['CRM SYSTEM - ANALYSIS API'], operation_summary="CRM ANALYSIS INFO API",
                         operation_description="# DESIGNER SEVER에서 CRM SYSTEM으로 고객 정보 요청 API\n"
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
            - API NAME : 고객상세분석 API
            - API DESC : CRM 고객상세분석 진입경로
                        분석 > 대시보드,비교분석,랭크 외 다른 메뉴로 진입 > 하단 비중분석에 항목 클릭 > 하단에 오더목록 > 고객명 클릭
            - API METHOD : POST
            - REQUEST PARAMS :
                (파라미터 이름, 타입, 최대길이, 설명, 필수여부, 비고)
                (ex/ cpId, varchar, 20, 조직ID, TRUE, 주노헤어=JN)
                |PARAM NAME|TYPE   |MAX LENGTH|DESC|REQUIRED|ETC     |
                |:--------:|:-----:|:--------:|:--:|:------:|:------:|
                |cpID      |varchar|20        |TRUE|기업아이디   |주노헤어=JN|
                |shopId    |varchar|20        |TRUE|매장아이디   |아무개=1234123|
                |custId    |varchar|20        |TRUE|고객아이디   |A매장=7|

                -SAMPLE JSON (** searchShop 같이 보내지 않아도 Return 함)
                ```
                {
                    "cpId": "JN",
                    "custId": "1916685",
                    "shopId": "1",
                    "searchShop": "order"
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
                    {
                        "custInfo": {
                            "cpId": "JN",
                            "custId": "1916685",
                            "custNm": "\uc774\uc815\uc740",
                            "mbrGrdCd": "BLK",
                            "mbrGrdNm": "Black",
                            "cpTelNo": "01073382890",
                            "bdayDate": "740302",
                            "chgUserId": "",
                            "chgUserNm": "",
                            "fvrtsShopId": "1",
                            "frstVstDt": "20190129",
                            "lastVstDt": "20230513",
                            "vstTotCnt": "52",
                            "visitCycleDay": "22",
                            "smsRcptYn": "Y",
                            "prpShpAmt": "0",
                            "prpDgnAmt": "0",
                            "custMemo": ""
                        },
                        "ticketList": [],
                        "custPayAmt": [
                            {
                                "cpId": "JN",
                                "ordDt": "20230501",
                                "chartLabel": "2023.05.01",
                                "shopId": "1",
                                "payAmt": "88000"
                            },
                            {
                                "cpId": "JN",
                                "ordDt": "20230307",
                                "chartLabel": "2023.03.07",
                                "shopId": "1",
                                "payAmt": "28000"
                            },
                            {
                                "cpId": "JN",
                                "ordDt": "20230207",
                                "chartLabel": "2023.02.07",
                                "shopId": "1",
                                "payAmt": "216000"
                            },
                            {
                                "cpId": "JN",
                                "ordDt": "20230207",
                                "chartLabel": "2023.02.07",
                                "shopId": "1",
                                "payAmt": "300000"
                            }
                        ],
                        "custPayInfo": {
                            "cpId": "JN",
                            "custId": "1916685",
                            "unitPrice": "158000",
                            "prpPrice": "0"
                        },
                        "mmbrsPayInfo": {
                            "cpId": "JN",
                            "stdYear": "2023",
                            "mbmGrdCd": "BLK",
                            "untprAmt": "92778",
                            "avgPrpAmt": "762848",
                            "custCnt": "278671",
                            "payAmt": "25854658721"
                        },
                        "custPayDiv": [
                            {
                                "payDivCd": "TOTAL",
                                "payDivNm": "\ud569\uacc4",
                                "totPayAmt": "673000"
                            },
                            {
                                "payDivCd": "CRD",
                                "payDivNm": "\uc2e0\uc6a9\uce74\ub4dc",
                                "totPayAmt": "373000"
                            },
                            {
                                "payDivCd": "CSH",
                                "payDivNm": "\ud604\uae08",
                                "totPayAmt": "300000"
                            }
                        ],
                        "custTrmType": [
                            {
                                "custId": "1916685",
                                "itemGrpCd": "TOTAL",
                                "itemGrpNm": "\ud569\uacc4",
                                "totPayAmt": "632000"
                            },
                            {
                                "custId": "1916685",
                                "itemGrpCd": "PRM",
                                "itemGrpNm": "\ud38c",
                                "totPayAmt": "536000"
                            },
                            {
                                "custId": "1916685",
                                "itemGrpCd": "CUT",
                                "itemGrpNm": "\ucef7",
                                "totPayAmt": "56000"
                            },
                            {
                                "custId": "1916685",
                                "itemGrpCd": "CLI",
                                "itemGrpNm": "\ud074\ub9ac\ub2c9",
                                "totPayAmt": "40000"
                            }
                        ]
                    }
                ```
        """

        # token 관리
        kwargs = common_utils.manage_tokens(self, kwargs=kwargs, request=request)

        print(f"{self.__class__.__name__} : Controller post get request.data ==> {request.data}")

        container = BaseContainer()
        service: AnalysisService = container.analysisCrmServiceProvider()

        # try:
        result = service.analysis_cust_detail_crm(request.data, accessToken=kwargs.get('accessToken', 'None'),
                                                      refreshToken=kwargs.get('refreshToken', 'None'))
        # except Exception as ex:
        #     print(f"{self.__class__.__name__} : Controller post error ==> {ex}")
        #     return Response(ex.__dict__, status=500)

        return Response(result, status=200)
