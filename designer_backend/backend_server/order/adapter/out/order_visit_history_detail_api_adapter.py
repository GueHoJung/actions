import config.utils.common_utils as common_utils


class OrderVisitHistoryDetailApiAdapter:
    """
    # CLASS : OrderVisitHistoryDetailApiAdapter
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/31 4:18 PM
    # DESCRIPTION
        - visit_history_detail
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/31          jung-gyuho          최초 생성
    """

    def order_visit_history_detail_crm_api(self, api_host, path, method, data, *args, **kwargs):
        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : order_visit_history_detail_crm_api get kwarg ==> {kwarg}")

        return common_utils.call_crm_api(self, self.__class__.__name__, api_host, path, method, data,
                                         accessToken=kwargs['accessToken'], refreshToken=kwargs['refreshToken'])
