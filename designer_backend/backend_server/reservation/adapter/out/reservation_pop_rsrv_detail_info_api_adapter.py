import config.utils.common_utils as common_utils


class ReservationPopRsrvDetailInfoApiAdapter:
    """
    # CLASS : ReservationPopRsrvDetailInfoApiAdapter
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/09 2:04 PM
    # DESCRIPTION
        - pop_rsrv_detail_info
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/09          jung-gyuho          최초 생성
    """

    def reservation_pop_rsrv_detail_info_crm_api(self, api_host, path, method, data, *args, **kwargs):
        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : reservation_pop_rsrv_detail_info_crm_api get kwarg ==> {kwarg}")

        return common_utils.call_crm_api(self, self.__class__.__name__, api_host, path, method, data,
                                         accessToken=kwargs['accessToken'], refreshToken=kwargs['refreshToken'])
