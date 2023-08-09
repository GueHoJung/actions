from abc import ABC, abstractmethod

from ....adapter.out.reservation_mod_reservation_holiday_api_adapter import ReservationModReservationHolidayApiAdapter


class ReservationModReservationHolidayOutPort(ABC):
    """
    # CLASS : ReservationModReservationHolidayOutPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/08 10:37 PM
    # DESCRIPTION
        - ModReservationHoliday Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/08          jung-gyuho          최초 생성
    """

    @abstractmethod
    def reservation_out_port(self, request):
        pass


class ReservationModReservationHolidayOutCrmImpl(ReservationModReservationHolidayOutPort):

    def __init__(self, reservationModReservationHolidayApiAdapter: ReservationModReservationHolidayApiAdapter):
        self.reservationModReservationHolidayApiAdapter = reservationModReservationHolidayApiAdapter

    def reservation_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} reservation_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : reservation_out_port get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : reservation_out_port get kwarg ==> {kwarg}")

        result = self.reservationModReservationHolidayApiAdapter.reservation_mod_reservation_holiday_crm_api(
            api_host=args[1], path=args[2],
            method=args[3],
            data=args[4], accessToken=kwargs[
                'accessToken'],
            refreshToken=kwargs[
                'refreshToken'])

        return result
