import config.utils.common_utils as common_utils


class AnalysisUserProductSalesRankApiAdapter:
    """
    # CLASS : AnalysisUserProductSalesRankApiAdapter
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/07 5:48 PM
    # DESCRIPTION
        - user_product_sales_rank
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/07          jung-gyuho          최초 생성
    """

    def analysis_user_product_sales_rank_crm_api(self, api_host, path, method, data, *args, **kwargs):
        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : analysis_user_product_sales_rank_crm_api get kwarg ==> {kwarg}")

        return common_utils.call_crm_api(self, self.__class__.__name__, api_host, path, method, data,
                                         accessToken=kwargs['accessToken'], refreshToken=kwargs['refreshToken'])
