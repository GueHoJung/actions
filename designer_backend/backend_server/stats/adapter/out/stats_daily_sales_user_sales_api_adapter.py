import config.utils.common_utils as common_utils


class StatsDailySalesUserSalesApiAdapter:
    """
    # CLASS : StatsDailySalesUserSalesApiAdapter
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/31 6:59 PM
    # DESCRIPTION
        - daily_sales_user_sales
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/31          jung-gyuho          최초 생성
    """

    def stats_daily_sales_user_sales_crm_api(self, api_host, path, method, data, *args, **kwargs):
        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : stats_daily_sales_user_sales_crm_api get kwarg ==> {kwarg}")

        return common_utils.call_crm_api(self, self.__class__.__name__, api_host, path, method, data,
                                         accessToken=kwargs['accessToken'], refreshToken=kwargs['refreshToken'])
