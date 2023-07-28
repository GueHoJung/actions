from dependency_injector.wiring import inject
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import APIView

from ...application.service.customer_modify_cust_info_service import CustomerModifyCustInfoService
from ...serializers import PostRequestSerializer
import config.utils.common_utils as common_utils
from config.utils.decorator import check_token

from config.base_container import BaseContainer


class CustomerModifyCustInfoApiController(APIView):
    """
    # CLASS : CustomerModifyCustInfoApiController
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/28 10:32 PM
    # DESCRIPTION
        - CustomerModifyCustInfoApiController
        - ModifyCustInfo API
        - CRM 디렉터리 : customer
        - CRM 서비스 호출 url : /customer/modifyCustInfo/
        - CRM 서비스 호출 method : POST
        - CRM 서비스 호출 body : json
        - CRM 서비스 호출 파라미터 :
            cpId (기업아이디)
            shopId (매장아이디)
            custId (고객아이디)
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/28          jung-gyuho          최초 생성
    """

    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(tags=['CRM SYSTEM - Customer API'], operation_summary="CRM Customer ModifyCustInfo API",
                         operation_description="# DESIGNER SEVER에서 CRM SYSTEM으로 ModifyCustInfo 요청 API\n"
                                               "\n"
                                               "|PARAM NAME|TYPE   |MAX LENGTH|DESC|REQUIRED|ETC     |\n"
                                               "|:--------:|:-----:|:--------:|:--:|:------:|:------:|\n"
                                               "|cpID      |varchar|20        |TRUE|기업아이디   |JN|\n"
                                               "|custId    |varchar|20        |TRUE|고객아이디   |1801141|\n"
                                               "|prpNo    |varchar|20        |TRUE|회원권번호   |PR000000001801141D001|\n"
                                               "|searchStDt    |varchar|20        |TRUE|조회시작일   |20200801|\n"
                                               "|searchEdDt    |varchar|20        |TRUE|조회종료일   |20220801|\n"
                                               "|prpHisDivCd    |varchar|20        |TRUE|회원권이력구분코드   |\"\"|\n"
                                               "|userId    |varchar|20        |TRUE|디자이너아이디   |\"\"|\n"
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
            - API NAME : ModifyCustInfo API
            - API DESC : CRM ModifyCustInfo 진입경로
                        ex) 분석 > 대시보드,비교분석,랭크 외 다른 메뉴로 진입 > 하단 비중분석에 항목 클릭 > 하단에 오더목록 > 고객명 클릭
            - API METHOD : POST
            - REQUEST PARAMS :
                (파라미터 이름, 타입, 최대길이, 설명, 필수여부, 비고)
                (ex/ cpId, varchar, 20, 조직ID, TRUE, 주노헤어=JN)
                |PARAM NAME|TYPE   |MAX LENGTH|DESC|REQUIRED|ETC     |
                |:--------:|:-----:|:--------:|:--:|:------:|:------:|
                |cpID      |varchar|20        |TRUE|기업아이디   |주노헤어=JN|
                |shopId    |varchar|20        |TRUE|매장아이디   |아무개=1234123|
                |custId    |varchar|20        |TRUE|고객아이디   |A매장=7|

                -SAMPLE JSON
                ```
                {
                    "cpId": "JN",
                    "shopId": "103",
                    "regUserId": "11273",
                    "custInfo": {
                        "custId": "1802104",
                        "custTpCd": "GNR",
                        "custNm": "김선희",
                        "mbrGrdCd": "BLK",
                        "mbrLineNo": "1",
                        "mbrGrdCdMode": "R",
                        "cpTelNo": "01088193669",
                        "maskingCpTelNo": "010****3669",
                        "gndrCd": "F",
                        "gndrCdNm": "여성",
                        "bdayDivCd": "S",
                        "bdayYyyy": "1900",
                        "bdayMm": "08",
                        "bdayDd": "19",
                        "bdayMmdd": "0819",
                        "telNo": "01011112222",
                        "smsRcptYn": "Y",
                        "chgUserId": "287",
                        "chgUserNm": "두설화",
                        "bfChgUserId": "287",
                        "warnYn": "N",
                        "emailAdr": "",
                        "custMemo": "염색 6NB\r\n",
                        "postNo": "",
                        "adr": "",
                        "adrDtl": "",
                        "extraAdr": "",
                        "joinTpCd": "99",
                        "joinShopId": "",
                        "fvrtsShopId": "103",
                        "fvrtsShopNm": "가든서현역점",
                        "annivTpCd": "",
                        "annivDt": "",
                        "carNo": ""
                    },
                    "custTstList": [
                        {
                            "idx": 0,
                            "tstLineNo": -1,
                            "tstTpCd": "02",
                            "tstTpCdNm": "음료",
                            "tstCntnt": "커피를 좋아하는 취향",
                            "readonly": true,
                            "modifyIcon": "M20.71,7.04C21.1,6.65 21.1,6 20.71,5.63L18.37,3.29C18,2.9 17.35,2.9 16.96,3.29L15.12,5.12L18.87,8.87M3,17.25V21H6.75L17.81,9.93L14.06,6.18L3,17.25Z",
                            "removeIcon": "M12,2C17.53,2 22,6.47 22,12C22,17.53 17.53,22 12,22C6.47,22 2,17.53 2,12C2,6.47 6.47,2 12,2M15.59,7L12,10.59L8.41,7L7,8.41L10.59,12L7,15.59L8.41,17L12,13.41L15.59,17L17,15.59L13.41,12L17,8.41L15.59,7Z",
                            "delYn": "N"
                        },
                        {
                            "idx": 1,
                            "tstLineNo": -1,
                            "tstTpCd": "03",
                            "tstTpCdNm": "샴푸",
                            "tstCntnt": "샴푸를 좋아하는 취향",
                            "readonly": true,
                            "modifyIcon": "M20.71,7.04C21.1,6.65 21.1,6 20.71,5.63L18.37,3.29C18,2.9 17.35,2.9 16.96,3.29L15.12,5.12L18.87,8.87M3,17.25V21H6.75L17.81,9.93L14.06,6.18L3,17.25Z",
                            "removeIcon": "M12,2C17.53,2 22,6.47 22,12C22,17.53 17.53,22 12,22C6.47,22 2,17.53 2,12C2,6.47 6.47,2 12,2M15.59,7L12,10.59L8.41,7L7,8.41L10.59,12L7,15.59L8.41,17L12,13.41L15.59,17L17,15.59L13.41,12L17,8.41L15.59,7Z",
                            "delYn": "N"
                        }
                    ],
                    "rsrvNo": "",
                    "ordNo": ""
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
        # service: CustomerModifyCustInfoService = container.customerModifyCustInfoCrmServiceProvider()

        # try:
        #     result = service.customer_modify_cust_info_crm(request.data, accessToken=kwargs.get('accessToken', 'None'),
        #                                              refreshToken=kwargs.get('refreshToken', 'None'))
        # except Exception as ex:
        #     print(f"{self.__class__.__name__} : Controller post error ==> {ex}")
        #     return Response(ex.__dict__, status=500)

        # return Response(result, status=200)
        return Response({"result": "CRM CONTROLLER GENERATE TEST"}, status=200)
