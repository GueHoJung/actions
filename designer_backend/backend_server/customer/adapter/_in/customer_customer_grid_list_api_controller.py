from dependency_injector.wiring import inject
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import APIView

from ...application.service.customer_customer_grid_list_service import CustomerCustomerGridListService
from ...serializers import PostRequestSerializer
import config.utils.common_utils as common_utils
from config.utils.decorator import check_token

from config.base_container import BaseContainer


class CustomerCustomerGridListApiController(APIView):
    """
    # CLASS : CustomerCustomerGridListApiController
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/09 2:10 PM
    # DESCRIPTION
        - CustomerCustomerGridListApiController
        - CustomerGridList API
        - CRM 디렉터리 : customer
        - CRM 서비스 설명 : 고객조회, 고객필터
        - CRM 서비스 호출 url : /customer/getCustomerGridList/
        - CRM 서비스 호출 method : POST
        - CRM 서비스 호출 body : json
        - CRM 서비스 호출 파라미터 :
            cpId (기업아이디)
            custParam (고객명 or 고객아이디)
            cpTelNo (휴대폰번호)
            carNo (차량번호)
            custMemo (고객메모)
            inActiveYn (휴면여부)
            chgUserId (담당디자이너아이디)
            fvrtsShopId (담당매장아이디)
            mbrGrdCd (멤버쉽등급)
            hasPrp (회원권보유여부)
            hasTkt (횟수권보유여부)
            smsRcptYn (문자수신여부)
            lstSalesUserId (최근담당디자이너아이디)
            lstVstShopId (최근방문매장아이디)
            bdayYyyy (생년)
            bdayMm (생월)
            searchTp (조회유형 => 최근방문기간조회 === 'lastVstDt' or '')
            searchStDt (조회시작일 => 최근방문기간조회 시)
            searchEdDt (조회종료일 => 최근방문기간조회 시)
            myShopTpCd (매장유형)
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/09          jung-gyuho          최초 생성
    """

    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(tags=['CRM SYSTEM - Customer API'], operation_summary="CRM Customer CustomerGridList API",
                         operation_description="# DESIGNER SEVER에서 CRM SYSTEM으로 CustomerGridList 요청 API\n"
                                               "\n"
                                               "|PARAM NAME|TYPE   |MAX LENGTH|REQUIRED|DESC|ETC     |\n"
                                               "|:--------:|:-----:|:--------:|:--:|:------:|:------:|\n"
                                               "|cpID      |varchar|20        |TRUE|기업아이디   |JN|\n"
                                               "|custParam      |varchar|20        |TRUE|고객명 or 고객아이디   ||\n"
                                               "|cpTelNo      |varchar|20        |TRUE|휴대폰번호   ||\n"
                                               "|carNo      |varchar|20        |TRUE|차량번호   ||\n"
                                               "|custMemo      |varchar|20        |TRUE|고객메모   ||\n"
                                               "|inActiveYn      |varchar|20        |TRUE|휴면여부   |false|\n"
                                               "|chgUserId      |varchar|20        |TRUE|담당디자이너아이디   |883|\n"
                                               "|fvrtsShopId      |varchar|20        |TRUE|담당매장아이디   |80|\n"
                                               "|mbrGrdCd      |varchar|20        |TRUE|멤버쉽등급   ||\n"
                                               "|hasPrp      |varchar|20        |TRUE|회원권보유여부   ||\n"
                                               "|hasTkt      |varchar|20        |TRUE|횟수권보유여부   ||\n"
                                               "|smsRcptYn      |varchar|20        |TRUE|문자수신여부   ||\n"
                                               "|lstSalesUserId      |varchar|20        |TRUE|최근담당디자이너아이디   ||\n"
                                               "|lstVstShopId      |varchar|20        |TRUE|최근방문매장아이디   ||\n"
                                               "|bdayYyyy      |varchar|20        |TRUE|생년   ||\n"
                                               "|bdayMm      |varchar|20        |TRUE|생월   ||\n"
                                               "|searchTp      |varchar|20        |TRUE|조회유형 => 최근방문기간조회 === 'lastVstDt' or ''   ||\n"
                                               "|searchStDt      |varchar|20        |TRUE|조회시작일 => 최근방문기간조회 시   |20210809|\n"
                                               "|searchEdDt      |varchar|20        |TRUE|조회종료일 => 최근방문기간조회 시   |20230809|\n"
                                               "|myShopTpCd      |varchar|20        |TRUE|매장유형   ||\n"
                                               "\n"
                                               "### Data type : json\n"
                                               "```\n"
                                               "{\n"
                                               "        \"cpId\": \"JN\",\n"
                                               "        \"custParam\": \"\",\n"
                                               "        \"cpTelNo\": \"\",\n"
                                               "        \"carNo\": \"\",\n"
                                               "        \"custMemo\": \"\",\n"
                                               "        \"inActiveYn\": false,\n"
                                               "        \"chgUserId\": \"883\",\n"
                                               "        \"fvrtsShopId\": \"80\",\n"
                                               "        \"mbrGrdCd\": \"\",\n"
                                               "        \"hasPrp\": \"\",\n"
                                               "        \"hasTkt\": \"\",\n"
                                               "        \"smsRcptYn\": \"\",\n"
                                               "        \"lstSalesUserId\": \"\",\n"
                                               "        \"lstVstShopId\": \"\",\n"
                                               "        \"bdayYyyy\": \"\",\n"
                                               "        \"bdayMm\": \"\",\n"
                                               "        \"searchTp\": \"\",\n"
                                               "        \"searchStDt\": \"20210809\",\n"
                                               "        \"searchEdDt\": \"20230809\",\n"
                                               "        \"myShopTpCd\": \"\"\n"
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
            - API NAME : CustomerGridList API
            - API DESC : CRM CustomerGridList 진입경로
                        ex) 분석 > 대시보드,비교분석,랭크 외 다른 메뉴로 진입 > 하단 비중분석에 항목 클릭 > 하단에 오더목록 > 고객명 클릭
            - API METHOD : POST
            - REQUEST PARAMS :
                (파라미터 이름, 타입, 최대길이, 설명, 필수여부, 비고)
                (ex/ cpId, varchar, 20, 조직ID, TRUE, 주노헤어=JN)
                |PARAM NAME|TYPE   |MAX LENGTH|REQUIRED|DESC|ETC     |
                |:--------:|:-----:|:--------:|:--:|:------:|:------:|
                |cpID      |varchar|20        |TRUE|기업아이디   |JN|
                |custParam      |varchar|20        |TRUE|고객명 or 고객아이디   ||
                |cpTelNo      |varchar|20        |TRUE|휴대폰번호   ||
                |carNo      |varchar|20        |TRUE|차량번호   ||
                |custMemo      |varchar|20        |TRUE|고객메모   ||
                |inActiveYn      |varchar|20        |TRUE|휴면여부   |false|
                |chgUserId      |varchar|20        |TRUE|담당디자이너아이디   |883|
                |fvrtsShopId      |varchar|20        |TRUE|담당매장아이디   |80|
                |mbrGrdCd      |varchar|20        |TRUE|멤버쉽등급   ||
                |hasPrp      |varchar|20        |TRUE|회원권보유여부   ||
                |hasTkt      |varchar|20        |TRUE|횟수권보유여부   ||
                |smsRcptYn      |varchar|20        |TRUE|문자수신여부   ||
                |lstSalesUserId      |varchar|20        |TRUE|최근담당디자이너아이디   ||
                |lstVstShopId      |varchar|20        |TRUE|최근방문매장아이디   ||
                |bdayYyyy      |varchar|20        |TRUE|생년   ||
                |bdayMm      |varchar|20        |TRUE|생월   ||
                |searchTp      |varchar|20        |TRUE|조회유형 => 최근방문기간조회 === 'lastVstDt' or ''   ||
                |searchStDt      |varchar|20        |TRUE|조회시작일 => 최근방문기간조회 시   |20210809|
                |searchEdDt      |varchar|20        |TRUE|조회종료일 => 최근방문기간조회 시   |20230809|
                |myShopTpCd      |varchar|20        |TRUE|매장유형   ||

                -SAMPLE JSON
                ```
                {
                    "cpId": "JN",
                    "custParam": "",
                    "cpTelNo": "",
                    "carNo": "",
                    "custMemo": "",
                    "inActiveYn": false,
                    "chgUserId": "883",
                    "fvrtsShopId": "80",
                    "mbrGrdCd": "",
                    "hasPrp": "",
                    "hasTkt": "",
                    "smsRcptYn": "",
                    "lstSalesUserId": "",
                    "lstVstShopId": "",
                    "bdayYyyy": "",
                    "bdayMm": "",
                    "searchTp": "",
                    "searchStDt": "20210809",
                    "searchEdDt": "20230809",
                    "myShopTpCd": ""
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
        service: CustomerCustomerGridListService = container.customerCustomerGridListCrmServiceProvider()

        try:
            result = service.customer_customer_grid_list_crm(request.data,
                                                             accessToken=kwargs.get('accessToken', 'None'),
                                                             refreshToken=kwargs.get('refreshToken', 'None'))
        except Exception as ex:
            print(f"{self.__class__.__name__} : Controller post error ==> {ex}")
            return Response(ex.__dict__, status=500)

        return Response(result, status=200)
        # return Response({"result": "CRM CONTROLLER GENERATE TEST"}, status=200)
