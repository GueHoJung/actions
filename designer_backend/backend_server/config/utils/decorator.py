# from functools import wraps

from django.core.exceptions import PermissionDenied


def check_token(func):
    # @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        print(f"decorator : Controller post get request.headers ==> {request.headers}")
        print(f"decorator : Controller post get request.COOKIES ==> {request.COOKIES}")
        # accessToken, refreshToken 있는지 체크
        if request.COOKIES.get('accessToken') and request.COOKIES.get('refreshToken') :
            print(
                f"decorator token YES : Controller post get request.COOKIES['accessToken'] ==> {request.COOKIES['accessToken']}")
            print(
                f"decorator token YES : Controller post get request.COOKIES['refreshToken'] ==> {request.COOKIES['refreshToken']}")
            return func(self, request, *args, **kwargs)
        else:
            print(
                f"decorator token NO : Controller post get request.COOKIES['accessToken'] ==> {request.COOKIES.get('accessToken','None')}")
            print(
                f"decorator token NO : Controller post get request.COOKIES['refreshToken'] ==> {request.COOKIES.get('refreshToken','None')}")
            raise PermissionDenied

    return wrapper
