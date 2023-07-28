import config.utils.common_utils as common_utils


class CustomerCustMemoListApiAdapter:
    """
    # CLASS : CustomerCustMemoListApiAdapter
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/28 9:46 PM
    # DESCRIPTION
        - cust_memo_list
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/28          jung-gyuho          최초 생성
    """

    def customer_cust_memo_list_crm_api(self, api_host, path, method, data, *args, **kwargs):
        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : customer_cust_memo_list_crm_api get kwarg ==> {kwarg}")

        return common_utils.call_crm_api(self, self.__class__.__name__, api_host, path, method, data,
                                         accessToken=kwargs['accessToken'], refreshToken=kwargs['refreshToken'])
