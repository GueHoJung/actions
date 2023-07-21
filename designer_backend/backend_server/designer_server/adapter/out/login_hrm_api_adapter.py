import requests


class LoginHrmApiAdapter:
    """
    # CLASS : LoginHRMApiAdapter
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/21 1:59 PM
    # DESCRIPTION
        - LoginHRMApiAdapter
        - HRM Login API 호출
    """
    def login_hrm_api(self, path, method, data):
        """
        # login_hrm_api 설명

        # PARAMS
            path : BASE URL 이하 경로
            method : POST 사용, GET, POST 등
            data : Login Json Data
        # RETURN
            return response.text
        # DESCRIPTION
            HRM SYSTEM Login API 호출
            로그인 후 권한에 맞는 정보 리턴
            토큰 발행 X
        ==================================================
        AUTHOR              DATE                NOTE
        --------------------------------------------------
        jung-gyuho              2023/07/21 2:32 PM       최초 작성
        """
        API_HOST = "http://192.168.0.100:9001"
        url = API_HOST + path
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        # body = {
        #     "cpId": "JN",
        #     "system": "CRM",
        #     "userId": "juno11273",
        #     "password": "e4f3f6f18e26b69acc799adf12b75957ab18b699b613a277280b8dc6764be90aa2750ad616477880ade169b4b883bad5e97b22d3a59c15f21b629fcf769b023c",
        #     "client": "PC"
        # }
        is_verify = True
        print(f"LoginHrmApiAdapter : LoginHRMAPI get data ==> {data}")
        # response = None

        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers, verify=is_verify, timeout=8)
                # print("0. response status %r" % response.status_code)
                print("0. response text %r" % response.text)
                if response.ok:
                    # print("1. response status %r" % response.status_code)
                    # print("1. response text %r" % response.text)
                    return response.text

        except Exception as ex:
            print(ex)


