from dependency_injector.wiring import inject
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import APIView

from ...application.service.order_prepaid_info_service import OrderPrepaidInfoService
from ...serializers import PostRequestSerializer
import config.utils.common_utils as common_utils
from config.utils.decorator import check_token

from config.base_container import BaseContainer


class OrderPrepaidInfoApiController(APIView):
    """
    # CLASS : OrderApiController
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/28 6:52 PM
    # DESCRIPTION
        - OrderApiController
        - PREPAID INFO API
        - CRM 디렉터리 :
        - CRM 서비스 호출 url :
        - CRM 서비스 호출 method : POST
        - CRM 서비스 호출 body : json
        - CRM 서비스 호출 파라미터 :
            cpId (기업아이디)
            shopId (매장아이디)
            custId (고객아이디)
            closeYn (폐쇄여부)
            prpTpCd (회원권유형코드)
            searchStDt (조회시작일)
            searchEdDt (조회종료일)

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/28          jung-gyuho          최초 생성
    """

    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(tags=['CRM SYSTEM - ORDER PrepaidInfo API'], operation_summary="CRM Order PREPAID INFO API",
                         operation_description="# DESIGNER SEVER에서 CRM SYSTEM으로 PREPAID INFO 요청 API\n"
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
            - API NAME : PREPAID INFO API
            - API DESC : CRM PREPAID INFO 진입경로
                        ex) 분석 > 대시보드,비교분석,랭크 외 다른 메뉴로 진입 > 하단 비중분석에 항목 클릭 > 하단에 오더목록 > 고객명 클릭
            - API METHOD : POST
            - REQUEST PARAMS :
                (파라미터 이름, 타입, 최대길이, 설명, 필수여부, 비고)
                (ex/ cpId, varchar, 20, 조직ID, TRUE, 주노헤어=JN)
                |PARAM NAME|TYPE   |MAX LENGTH|DESC|REQUIRED|ETC     |
                |:--------:|:-----:|:--------:|:--:|:------:|:------:|
                |cpID      |varchar|200        |TRUE|기업아이디   |주노헤어=JN|
                |shopId    |varchar|200        |TRUE|매장아이디   |A매장=1234123|
                |custId    |varchar|200        |TRUE|고객아이디   |아무개=7|
                |closeYn    |varchar|200        |TRUE|폐쇄여부   |Y,N,""|
                |prpTpCd    |varchar|200        |TRUE|회원권유형코드   |""|
                |searchStDt    |varchar|200        |TRUE|조회시작일   |20200101|
                |searchEdDt    |varchar|200        |TRUE|조회종료일   |20230731|

                -SAMPLE JSON
                ```
                {
                    "cpId": "JN",
                    "shopId": "103",
                    "custId": "2003929",
                    "closeYn": "",
                    "prpTpCd": "",
                    "searchStDt": "20200128",
                    "searchEdDt": "20230728"
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
                    {'data': [
                                    {'rowNum': 1, 'cpId': 'JN', 'prpNo': 'PR000000002003929D002', 'custId': '2003929', 'custNm': '강나라', 'cpTelNo': '01073444462', 'prpTpCd': 'DGN', 'prpTpCdNm': '선불권', 'prpOpenDivCd': 'MIG', 'prpOpenDivCdNm': None, 'mngShopId': '103', 'mngShopNm': '가든서현역점', 'mngUserId': '1959', 'mngUserNm': '조아람', 'openDt': '20220801', 'closeDt': '20220801', 'closeYn': 'Y', 'prpAmt': 0, 'ordNo': 'migration', 'itemCd': None, 'itemNm': None, 'itemDispNm': None, 'salesUserId': None, 'salesUserNm': None, 'totalRecordCnt': 2
                                    },
                                    {'rowNum': 2, 'cpId': 'JN', 'prpNo': 'PR000000002003929S001', 'custId': '2003929', 'custNm': '강나라', 'cpTelNo': '01073444462', 'prpTpCd': 'SHP', 'prpTpCdNm': '뉴선불권', 'prpOpenDivCd': 'MIG', 'prpOpenDivCdNm': None, 'mngShopId': '103', 'mngShopNm': '가든서현역점', 'mngUserId': '1959', 'mngUserNm': '조아람', 'openDt': '20220801', 'closeDt': '', 'closeYn': 'N', 'prpAmt': 33400, 'ordNo': 'migration', 'itemCd': None, 'itemNm': None, 'itemDispNm': None, 'salesUserId': None, 'salesUserNm': None, 'totalRecordCnt': 2
                                    }
                            ], 'summary': [
                                    {'custId': '2003929', 'prpTpCd': 'DGN', 'prpTpCdNm': '선불권', 'mngShopId': '103', 'mngShopNm': '가든서현역점', 'mngUserId': '1959', 'mngUserNm': '조아람', 'prpAmtTot': 0
                                    },
                                    {'custId': '2003929', 'prpTpCd': 'SHP', 'prpTpCdNm': '뉴선불권', 'mngShopId': '103', 'mngShopNm': '가든서현역점', 'mngUserId': '1959', 'mngUserNm': '조아람', 'prpAmtTot': 33400
                                    }
                            ]
                    }
                ```
        """

        # token 관리
        kwargs = common_utils.manage_tokens(self, kwargs=kwargs, request=request)

        print(f"{self.__class__.__name__} : Controller post get request.data ==> {request.data}")

        container = BaseContainer()
        service: OrderPrepaidInfoService = container.orderPrepaidInfoCrmServiceProvider()

        # try:
        result = service.order_prepaid_info_crm(request.data, accessToken=kwargs.get('accessToken', 'None'),
                                                refreshToken=kwargs.get('refreshToken', 'None'))
        # except Exception as ex:
        #     print(f"{self.__class__.__name__} : Controller post error ==> {ex}")
        #     return Response(ex.__dict__, status=500)

        return Response(result, status=200)
        # return Response({"result": "CRM CONTROLLER GENERATE TEST"}, status=200)
