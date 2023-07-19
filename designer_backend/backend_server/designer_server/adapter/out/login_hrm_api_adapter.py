import json

import requests
import json


class LoginHrmApiAdapter:

    def login_hrm_api(self, path, method, data):
        API_HOST = "http://192.168.0.100:9001"
        url = API_HOST + path
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        body = {
            "cpId": "JN",
            "system": "CRM",
            "userId": "juno11273",
            "password": "e4f3f6f18e26b69acc799adf12b75957ab18b699b613a277280b8dc6764be90aa2750ad616477880ade169b4b883bad5e97b22d3a59c15f21b629fcf769b023c",
            "client": "PC"
        }
        is_verify = True
        print(f"LoginHRMAPI get data ==> {data}")
        # jBody = convert_json_to_obj(data.body)
        jBody = convert_dict_to_json(data)

        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                # response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))
                response = requests.post(url, json=jBody, headers=headers, verify=is_verify, timeout=8)
                print("response status %r" % response.status_code)
                print("response text %r" % response.text)
                if response.ok:
                    print("response status %r" % response.status_code)
                    print("response text %r" % response.text)
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
