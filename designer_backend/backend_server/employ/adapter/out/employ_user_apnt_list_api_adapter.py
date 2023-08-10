import config.utils.common_utils as common_utils


class EmployUserApntListApiAdapter:
    """
    # CLASS : EmployUserApntListApiAdapter
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/09 3:38 PM
    # DESCRIPTION
        - user_apnt_list
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/09          jung-gyuho          최초 생성
    """

    def employ_user_apnt_list_hrm_api(self, api_host, path, method, data, *args, **kwargs):
        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : employ_user_apnt_list_hrm_api get kwarg ==> {kwarg}")

        return common_utils.call_hrm_api(self, self.__class__.__name__, api_host, path, method, data,
                                         accessToken=kwargs['accessToken'], refreshToken=kwargs['refreshToken'])
