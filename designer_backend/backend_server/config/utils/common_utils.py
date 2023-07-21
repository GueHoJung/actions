import requests
import json


def call_crm_api(self, className, path, method, data):
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
    API_HOST = "http://192.168.0.247:8000"

    url = API_HOST + path
    headers = {'Content-Type': 'application/json; charset=utf-8',
               'Origin': 'http://192.168.0.247:8000'}

    is_verify = True
    print(f"{className} : LoginCrmAPI get data ==> {data}")

    try:
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':

            response = requests.post(url, json=data, headers=headers, verify=is_verify, timeout=8)

            print("0. response status %r" % response.status_code)
            print("0. response text %r" % response.text)
            print(f"0. {className} : call_crm_api response.cookies ==> {response.cookies}")
            if response.ok:
                # print("1. response status %r" % response.status_code)
                # print("1. response text %r" % response.text)
                # requests.cookies = response.cookies
                # csrftoken = response.cookies['csrftoken']
                print(f"1. {className} : call_crm_api response.cookies ==> {response.cookies}")
                return response.text

    except Exception as ex:
        print(ex)


# convert json to object
def convert_json_to_obj(data):
    """
    json string 을 object 로 변환
    :param data: request data 혹은 interface response data
    :return: object
    """
    if isinstance(data, str):
        return json.loads(data)
    else:
        return json.loads(data.body.decode('utf-8'))


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
