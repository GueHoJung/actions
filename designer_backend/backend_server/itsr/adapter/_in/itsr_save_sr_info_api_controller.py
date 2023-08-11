from dependency_injector.wiring import inject
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.views import APIView

from ...application.service.itsr_save_sr_info_service import ItsrSaveSrInfoService
from ...serializers import PostRequestSerializer
import config.utils.common_utils as common_utils
from config.utils.decorator import check_token

from config.base_container import BaseContainer


class ItsrSaveSrInfoApiController(APIView):
    """
    # CLASS : ItsrSaveSrInfoApiController
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/09 2:32 PM
    # DESCRIPTION
        - ItsrSaveSrInfoApiController
        - SaveSrInfo API
        - CRM 디렉터리 : itsr
        - CRM 서비스 설명 : 문의등록
        - CRM 서비스 호출 url : /itsr/saveSrInfo/
        - CRM 서비스 호출 method : POST
        - CRM 서비스 호출 body : json
        - CRM 서비스 호출 파라미터 :
            cpId (기업아이디)
            shopId (매장아이디)
            reqClsfcCd (요청분류)
            reqClsfcDtlCd (요청분류상세)
            reqPrcStateCd (요청처리상태)
            reqUserId (요청자)
            ordNo (오더번호)
            rsrvNo (예약번호)
            custId (고객아이디)
            custNm (고객명)
            salesUserId (판매자디자이너아이디)
            reqCon (요청내용)
            regUserId (등록자아이디)
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/09          jung-gyuho          최초 생성
    """

    # permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(tags=['CRM SYSTEM - Itsr API'], operation_summary="CRM Itsr SaveSrInfo API",
                         operation_description="# DESIGNER SEVER에서 CRM SYSTEM으로 SaveSrInfo 요청 API\n"
                                               "\n"
                                               "|PARAM NAME|TYPE   |MAX LENGTH|REQUIRED|DESC|ETC     |\n"
                                               "|:--------:|:-----:|:--------:|:--:|:------:|:------:|\n"
                                               "|cpID      |varchar|20        |TRUE|기업아이디   |JN|\n"
                                               "|srNo      |varchar|20        |TRUE|-   ||\n"
                                               "|shopId      |varchar|20        |TRUE|매장아이디   |80|\n"
                                               "|shopNm      |varchar|20        |TRUE|매장이름   |가든강남구청역점|\n"
                                               "|reqUserId      |varchar|20        |TRUE|요청자아이디   |11273|\n"
                                               "|reqUserNm      |varchar|20        |TRUE|요청자이름   |안준|\n"
                                               "|systmTpCd      |varchar|20        |TRUE|시스템유형   |POS|\n"
                                               "|reqTpCd      |varchar|20        |TRUE|요청유형코드   |INQR|\n"
                                               "|reqClsfcCd      |varchar|20        |TRUE|요청분류   |P02|\n"
                                               "|reqClsfcDtlCd      |varchar|20        |TRUE|요청분류상세   |P0201|\n"
                                               "|reqPrcStateCd      |varchar|20        |TRUE|요청처리상태   |REQ|\n"
                                               "|ordNo      |varchar|20        |TRUE|오더번호   |JN|\n"
                                               "|rsrvNo      |varchar|20        |TRUE|예약번호   |JN|\n"
                                               "|custId      |varchar|20        |TRUE|고객아이디   |J202110300298|\n"
                                               "|custNm      |varchar|20        |TRUE|고객명   |강은|\n"
                                               "|fvrtsShopNm      |varchar|20        |TRUE|즐겨찾는매장명   |가든강남구청역점|\n"
                                               "|salesUserId      |varchar|20        |TRUE|판매자디자이너아이디   ||\n"
                                               "|salesUserNm      |varchar|20        |TRUE|판매자디자이너이름   ||\n"
                                               "|salesUserOfdtyNm      |varchar|20        |TRUE|-   ||\n"
                                               "|reqCon      |varchar|20        |TRUE|요청내용   |SR 등록 테스트|\n"
                                               "|regUserId      |varchar|20        |TRUE|등록자아이디   |11273|\n"
                                               "|updUserId      |varchar|20        |TRUE|편집자아이디   |11273|\n"
                                               "\n"
                                               "### Data type : json\n"
                                               "```\n"
                                               "{\n"
                                               "        \"cpId\": \"JN\",\n"
                                               "        \"srNo\": \"\",\n"
                                               "        \"shopId\": \"80\",\n"
                                               "        \"shopNm\": \"가든강남구청역점\",\n"
                                               "        \"reqUserId\": \"11273\",\n"
                                               "        \"reqUserNm\": \"안준\",\n"
                                               "        \"systmTpCd\": \"POS\",\n"
                                               "        \"reqTpCd\": \"INQR\",\n"
                                               "        \"reqClsfcCd\": \"P02\",\n"
                                               "        \"reqClsfcDtlCd\": \"P0201\",\n"
                                               "        \"reqPrcStateCd\": \"REQ\",\n"
                                               "        \"ordNo\": \"\",\n"
                                               "        \"rsrvNo\": \"\",\n"
                                               "        \"custId\": \"J202110300298\",\n"
                                               "        \"custNm\": \"강은\",\n"
                                               "        \"fvrtsShopNm\": \"가든강남구청역점\",\n"
                                               "        \"salesUserId\": \"\",\n"
                                               "        \"salesUserNm\": \"\",\n"
                                               "        \"salesUserOfdtyNm\": \"\",\n"
                                               "        \"reqCon\": \"SR 등록 테스트\",\n"
                                               "        \"regUserId\": \"11273\",\n"
                                               "        \"updUserId\": \"11273\"\n"
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
            - API NAME : SaveSrInfo API
            - API DESC : CRM SaveSrInfo 진입경로
                        ex) 분석 > 대시보드,비교분석,랭크 외 다른 메뉴로 진입 > 하단 비중분석에 항목 클릭 > 하단에 오더목록 > 고객명 클릭
            - API METHOD : POST
            - REQUEST PARAMS :
                (파라미터 이름, 타입, 최대길이, 설명, 필수여부, 비고)
                (ex/ cpId, varchar, 20, 조직ID, TRUE, 주노헤어=JN)
                |PARAM NAME|TYPE   |MAX LENGTH|REQUIRED|DESC|ETC     |
                |:--------:|:-----:|:--------:|:--:|:------:|:------:|
                |cpID      |varchar|20        |TRUE|기업아이디   |JN|
                |srNo      |varchar|20        |TRUE|-   ||
                |shopId      |varchar|20        |TRUE|매장아이디   |80|
                |shopNm      |varchar|20        |TRUE|매장이름   |가든강남구청역점|
                |reqUserId      |varchar|20        |TRUE|요청자아이디   |11273|
                |reqUserNm      |varchar|20        |TRUE|요청자이름   |안준|
                |systmTpCd      |varchar|20        |TRUE|시스템유형   |POS|
                |reqTpCd      |varchar|20        |TRUE|요청유형코드   |INQR|
                |reqClsfcCd      |varchar|20        |TRUE|요청분류   |P02|
                |reqClsfcDtlCd      |varchar|20        |TRUE|요청분류상세   |P0201|
                |reqPrcStateCd      |varchar|20        |TRUE|요청처리상태   |REQ|
                |ordNo      |varchar|20        |TRUE|오더번호   |JN|
                |rsrvNo      |varchar|20        |TRUE|예약번호   |JN|
                |custId      |varchar|20        |TRUE|고객아이디   |J202110300298|
                |custNm      |varchar|20        |TRUE|고객명   |강은|
                |fvrtsShopNm      |varchar|20        |TRUE|즐겨찾는매장명   |가든강남구청역점|
                |salesUserId      |varchar|20        |TRUE|판매자디자이너아이디   ||
                |salesUserNm      |varchar|20        |TRUE|판매자디자이너이름   ||
                |salesUserOfdtyNm      |varchar|20        |TRUE|-   ||
                |reqCon      |varchar|20        |TRUE|요청내용   |SR 등록 테스트|
                |regUserId      |varchar|20        |TRUE|등록자아이디   |11273|
                |updUserId      |varchar|20        |TRUE|편집자아이디   |11273|

                -SAMPLE JSON
                ```
                {
                    "cpId": "JN",
                    "srNo": "",
                    "shopId": "80",
                    "shopNm": "가든강남구청역점",
                    "reqUserId": "11273",
                    "reqUserNm": "안준",
                    "systmTpCd": "POS",
                    "reqTpCd": "INQR",
                    "reqClsfcCd": "P02",
                    "reqClsfcDtlCd": "P0201",
                    "reqPrcStateCd": "REQ",
                    "ordNo": "",
                    "rsrvNo": "",
                    "custId": "J202110300298",
                    "custNm": "강은",
                    "fvrtsShopNm": "가든강남구청역점",
                    "salesUserId": "",
                    "salesUserNm": "",
                    "salesUserOfdtyNm": "",
                    "reqCon": "SR 등록 테스트",
                    "regUserId": "11273",
                    "updUserId": "11273"
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
        service: ItsrSaveSrInfoService = container.itsrSaveSrInfoCrmServiceProvider()

        try:
            result = service.itsr_save_sr_info_crm(request.data, accessToken=kwargs.get('accessToken', 'None'),
                                                   refreshToken=kwargs.get('refreshToken', 'None'))
        except Exception as ex:
            print(f"{self.__class__.__name__} : Controller post error ==> {ex}")
            return Response(ex.__dict__, status=500)

        return Response(result, status=200)
        # return Response({"result": "CRM CONTROLLER GENERATE TEST"}, status=200)
