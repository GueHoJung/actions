import config.utils.common_utils as common_utils


class ItsrSaveSrInfoApiAdapter:
    """
    # CLASS : ItsrSaveSrInfoApiAdapter
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/09 2:42 PM
    # DESCRIPTION
        - save_sr_info
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/09          jung-gyuho          최초 생성
    """

    def itsr_save_sr_info_crm_api(self, api_host, path, method, data, *args, **kwargs):
        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : itsr_save_sr_info_crm_api get kwarg ==> {kwarg}")

        return common_utils.call_crm_api(self, self.__class__.__name__, api_host, path, method, data,
                                         accessToken=kwargs['accessToken'], refreshToken=kwargs['refreshToken'])
