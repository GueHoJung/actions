import requests
import re
import json


def call_crm_api(self, className, api_host, path, method, data, *args, **kwargs):
    """
    # call_crm_api 설명

    # PARAMS :
        className : 클래스 명
        path : API BASEURL 이하 경로
        method : POST 사용, GET, POST 등
        data : json data
    # RETURN :
        json
        - response.text
        - accessToken, refreshToken
    # DESCRIPTION

    ==================================================
    AUTHOR              DATE                NOTE
    --------------------------------------------------
    jung-gyuho              2023/07/21 10:13 PM       최초 작성
    """
    # API_HOST = "http://192.168.0.247:8000"
    API_HOST = api_host

    url = API_HOST + path

    for key in kwargs.keys():
        print(f"{className} : call_crm_api get arg ==> {key} : {kwargs[key]}")

    headers = {'Content-Type': 'application/json; charset=utf-8',
               'Origin': 'http://192.168.0.247:8000'}
    # accessToken은 헤더 'Authorization'에 담아서 보낸다.
    if kwargs.get('accessToken') is not None:
        headers['Authorization'] = 'Bearer ' + kwargs['accessToken']

    # accessToken, refreshToken은 COOKIE 에 담아서 보낸다.
    if kwargs.get('refreshToken') is not None:
        requests.cookies = {'accessToken': kwargs['accessToken'], 'refreshToken': kwargs['refreshToken']}

    result = {}
    # is_verify = True
    is_verify = False
    print(f"{className} : call_crm_api ==> {data}")

    try:
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':

            response = requests.post(url, json=data, headers=headers, verify=is_verify, timeout=20)

            print("0. response status %r" % response.status_code)
            print("0. response text %r" % response.text)
            print(f"0. {className} : call_crm_api response.cookies ==> {response.cookies}")
            if response.ok:
                # print("1. response status %r" % response.status_code)
                # print("1. response text %r" % response.text)
                # requests.cookies = response.cookies
                # csrftoken = response.cookies['csrftoken']
                print(f"1. {className} : call_crm_api response.cookies ==> {response.cookies}")

                # response.cookies 에 accessToken, refreshToken 값 있는 경우 result 에 저장
                for res in response.cookies:
                    if res.name == 'accessToken':
                        result['accessToken'] = res.value
                        print(
                            f"2. {className} : call_crm_api response.cookie.name : value  ==> {res.name} : {res.value}")
                    if res.name == 'refreshToken':
                        result['refreshToken'] = res.value
                        print(
                            f"2. {className} : call_crm_api response.cookie.name : value  ==> {res.name} : {res.value}")

                result['data'] = response.text
                print(f"3. {className} : call_crm_api result ==> {result}")
                return result

    except Exception as ex:
        print(f"{className} : call_crm_api Exception ==> {ex}")
        return {"Exception": str(ex)}


def call_hrm_api(self, className, api_host, path, method, data, *args, **kwargs):
    """
    # call_hrm_api 설명

    # PARAMS :
        className : 클래스 명
        path : API BASEURL 이하 경로
        method : POST 사용, GET, POST 등
        data : json data
    # RETURN :
        json
        - response.text
        - accessToken, refreshToken
    # DESCRIPTION

    ==================================================
    AUTHOR              DATE                NOTE
    --------------------------------------------------
    jung-gyuho              2023/07/21 10:13 PM       최초 작성
    """
    # API_HOST = "http://192.168.0.247:8000"
    API_HOST = api_host

    url = API_HOST + path

    for key in kwargs.keys():
        print(f"{className} : call_hrm_api get arg ==> {key} : {kwargs[key]}")

    headers = {'Content-Type': 'application/json; charset=utf-8',
               'Origin': 'http://192.168.0.247:8000'}
    # # accessToken은 헤더 'Authorization'에 담아서 보낸다.
    # if kwargs.get('accessToken') is not None:
    #     headers['Authorization'] = 'Bearer ' + kwargs['accessToken']
    #
    # # accessToken, refreshToken은 COOKIE 에 담아서 보낸다.
    # if kwargs.get('refreshToken') is not None:
    #     requests.cookies = {'accessToken': kwargs['accessToken'], 'refreshToken': kwargs['refreshToken']}

    result = {}
    # is_verify = True
    is_verify = False
    print(f"{className} : call_hrm_api ==> {data}")

    try:
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':

            response = requests.post(url, json=data, headers=headers, verify=is_verify, timeout=8)

            print("0. response status %r" % response.status_code)
            print("0. response text %r" % response.text)
            print(f"0. {className} : call_hrm_api response.cookies ==> {response.cookies}")
            if response.ok:
                # print("1. response status %r" % response.status_code)
                # print("1. response text %r" % response.text)
                # requests.cookies = response.cookies
                # csrftoken = response.cookies['csrftoken']
                print(f"1. {className} : call_hrm_api response.cookies ==> {response.cookies}")

                # response.cookies 에 accessToken, refreshToken 값 있는 경우 result 에 저장
                # for res in response.cookies:
                #     if res.name == 'accessToken':
                #         result['accessToken'] = res.value
                #         print(
                #             f"2. {className} : call_hrm_api response.cookie.name : value  ==> {res.name} : {res.value}")
                #     if res.name == 'refreshToken':
                #         result['refreshToken'] = res.value
                #         print(
                #             f"2. {className} : call_hrm_api response.cookie.name : value  ==> {res.name} : {res.value}")

                result['data'] = response.text
                return result

    except Exception as ex:
        print(f"{className} : call_hrm_api Exception ==> {ex}")
        return {"Exception": str(ex)}


# convert json to object
def convert_json_to_obj(data):
    """
    json string 을 object 로 변환
    :param data: request data 혹은 interface response data
    :return: object
    """
    try:
        if isinstance(data, str):
            return json.loads(data)
        else:
            return json.loads(data.body.decode('utf-8'))
    except Exception as ex:
        print(f"convert_json_to_obj Exception ==> {ex}")
        return {"Exception": str(ex)}


def convert_dict_to_json(data):
    """
    dictionary data 를 json 형식으로 변환
    :param data: dictionary type data
    :return: object
    """
    if isinstance(data, dict):
        return json.dumps(data, ensure_ascii=False)
    else:
        return data


def manage_tokens(self, kwargs, request):
    """
    # manage_tokens 설명

    # PARAMS :
        kwargs : accessToken, refreshToken 을 담을 dynamic parameter
        request : accessToken, refreshToken 을 담고 있는 request 요청
    # RETURN :
        kwargs
    # DESCRIPTION

    ==================================================
    AUTHOR              DATE                NOTE
    --------------------------------------------------
    jung-gyuho              2023/07/27 4:24 PM       최초 작성
    """
    # accessToekn, refreshToken 을 request 에서 가져온다.
    # accessToken 은 쿠키로 관리
    if request.COOKIES.get('accessToken'):
        print(
            f"{self.__class__.__name__} : Controller post get request.COOKIES['accessToken'] ==> {request.COOKIES['accessToken']}")
        kwargs['accessToken'] = request.COOKIES['accessToken']
    # refreshToken 은 쿠키로 관리
    if request.COOKIES.get('refreshToken'):
        print(
            f"{self.__class__.__name__} : Controller post get request.COOKIES['refreshToken'] ==> {request.COOKIES['refreshToken']}")
        kwargs['refreshToken'] = request.COOKIES['refreshToken']

    return kwargs
