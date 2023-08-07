import config.utils.common_utils as common_utils


class StatsYearlySalesUserOrderTypeSalesApiAdapter:
    """
    # CLASS : StatsYearlySalesUserOrderTypeSalesApiAdapter
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/04 1:44 PM
    # DESCRIPTION
        - yearly_sales_user_order_type_sales
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/04          jung-gyuho          최초 생성
    """

    def stats_yearly_sales_user_order_type_sales_crm_api(self, api_host, path, method, data, *args, **kwargs):
        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : stats_yearly_sales_user_order_type_sales_crm_api get kwarg ==> {kwarg}")

        return common_utils.call_crm_api(self, self.__class__.__name__, api_host, path, method, data,
                                         accessToken=kwargs['accessToken'], refreshToken=kwargs['refreshToken'])
