from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings


# 아래 test_view() 함수 주석을 풀면, LoginService의 crm login 함수가 실행되는 현상 발생, docker-compose up 또는 컨테이너 restart 시에도 발생
# Create your views here.
@api_view(['GET'])
def test_view(request):
    """
    # API : test_view
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/28 4:42 PM
    # DESCRIPTION
        - API NAME : TEST TEMPLATE API
        - API DESC : DJANGO APP START 용 TEAMPLATE API
        - API METHOD : GET
        - REQUEST PARAMS : 해당 없음
            (파라미터 이름, 타입, 최대길이, 설명, 필수여부, 비고)
            (ex/ cpId, varchar, 20, 조직ID, TRUE, 주노헤어=JN)
            |PARAM NAME|TYPE   |MAX LENGTH|DESC|REQUIRED|ETC     |
            |:--------:|:-----:|:--------:|:--:|:------:|:------:|
            |cpID      |varchar|20        |TRUE|조직ID   |주노헤어=JN|

            -SAMPLE JSON
            ```
            {
                "cpId": "JN",
                "system": "CRM",
                "userId": "juno***",
                "password": "***",
                "client": "PC"
            }

            ```
        - RESPONSE OBJECTS : TEST RESULT JSON
            (파라미터 이름, 타입, 최대길이, 설명, 필수여부, 비고)
            (ex/ code, varchar, 100, 결과 코드, TRUE, -)
            |PARAM NAME|TYPE|MAX LENGTH|DESC|REQUIRED|ETC|
            |:---:|:---:|:---:|:---:|:---:|:---:|
            |code|varchar|100|결과 코드|TRUE| - |
            - SAMPLE JSON :
            ```
                {"test": "테스트입니다.", "API_HOST": API_HOST, "API_PORT": API_PORT}
            ```
    """
    API_HOST = getattr(settings, "CRM_HOST_IP", None)
    API_PORT = getattr(settings, "CRM_HOST_PORT", None)

    return Response({"test": "테스트입니다.", "API_HOST": API_HOST, "API_PORT": API_PORT})
