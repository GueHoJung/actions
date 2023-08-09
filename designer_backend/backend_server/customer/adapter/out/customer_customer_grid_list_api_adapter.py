import config.utils.common_utils as common_utils


class CustomerCustomerGridListApiAdapter:
    """
    # CLASS : CustomerCustomerGridListApiAdapter
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/09 2:18 PM
    # DESCRIPTION
        - customer_grid_list
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/09          jung-gyuho          최초 생성
    """

    def customer_customer_grid_list_crm_api(self, api_host, path, method, data, *args, **kwargs):
        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : customer_customer_grid_list_crm_api get kwarg ==> {kwarg}")

        return common_utils.call_crm_api(self, self.__class__.__name__, api_host, path, method, data,
                                         accessToken=kwargs['accessToken'], refreshToken=kwargs['refreshToken'])
