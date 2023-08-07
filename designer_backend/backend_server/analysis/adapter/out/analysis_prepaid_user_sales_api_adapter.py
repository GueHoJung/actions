import config.utils.common_utils as common_utils


class AnalysisPrepaidUserSalesApiAdapter:
    """
    # CLASS : AnalysisPrepaidUserSalesApiAdapter
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/31 4:50 PM
    # DESCRIPTION
        - prepaid_user_sales
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/31          jung-gyuho          최초 생성
    """

    def analysis_prepaid_user_sales_crm_api(self, api_host, path, method, data, *args, **kwargs):
        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : analysis_prepaid_user_sales_crm_api get kwarg ==> {kwarg}")

        return common_utils.call_crm_api(self, self.__class__.__name__, api_host, path, method, data,
                                         accessToken=kwargs['accessToken'], refreshToken=kwargs['refreshToken'])
