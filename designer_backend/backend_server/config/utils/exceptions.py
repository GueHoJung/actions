from rest_framework.views import exception_handler
from rest_framework import exceptions


def custom_exception_handler(exc, context):
    """
    # custom_exception_handler 설명

    # PARAMS :
        exc : exception
        context : context
    # RETURN :
        response : response에 exception 해결 위한 정보 추가
    # DESCRIPTION
        Mobile 서버에서 API 호출 시, 기본적으로 cookie와 token 정보를 가지고 있는지 검사
    ==================================================
    AUTHOR              DATE                NOTE
    --------------------------------------------------
    jung-gyuho              2023/07/27 5:37 PM       최초 작성
    """

    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    print(f"custom_exception_handler exc ==> {exc}")
    print(f"custom_exception_handler context ==> {context}")

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code

        # exception 종류에 따라 다른 info 메세지 전달
        if isinstance(exc, exceptions.PermissionDenied):
            response.data['info'] = 'no available tokens'

    return response
