import json
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
