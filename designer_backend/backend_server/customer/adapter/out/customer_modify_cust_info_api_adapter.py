import config.utils.common_utils as common_utils


class CustomerModifyCustInfoApiAdapter:
    """
    # CLASS : CustomerModifyCustInfoApiAdapter
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/28 10:34 PM
    # DESCRIPTION
        - modify_cust_info
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/28          jung-gyuho          최초 생성
    """

    def customer_modify_cust_info_crm_api(self, api_host, path, method, data, *args, **kwargs):
        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : customer_modify_cust_info_crm_api get kwarg ==> {kwarg}")

        return common_utils.call_crm_api(self, self.__class__.__name__, api_host, path, method, data,
                                         accessToken=kwargs['accessToken'], refreshToken=kwargs['refreshToken'])
