import config.utils.common_utils as common_utils


class ReservationModReservationHolidayApiAdapter:
    """
    # CLASS : ReservationModReservationHolidayApiAdapter
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/08 10:36 PM
    # DESCRIPTION
        - mod_reservation_holiday
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/08          jung-gyuho          최초 생성
    """

    def reservation_mod_reservation_holiday_crm_api(self, api_host, path, method, data, *args, **kwargs):
        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : reservation_mod_reservation_holiday_crm_api get kwarg ==> {kwarg}")

        return common_utils.call_crm_api(self, self.__class__.__name__, api_host, path, method, data,
                                         accessToken=kwargs['accessToken'], refreshToken=kwargs['refreshToken'])
