from abc import ABC, abstractmethod

from ....adapter.out.reservation_reservation_holiday_api_adapter import ReservationReservationHolidayApiAdapter


class ReservationReservationHolidayOutPort(ABC):
    """
    # CLASS : ReservationReservationHolidayOutPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/08 9:51 PM
    # DESCRIPTION
        - ReservationHoliday Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/08          jung-gyuho          최초 생성
    """

    @abstractmethod
    def reservation_out_port(self, request):
        pass


class ReservationReservationHolidayOutCrmImpl(ReservationReservationHolidayOutPort):

    def __init__(self, reservationReservationHolidayApiAdapter: ReservationReservationHolidayApiAdapter):
        self.reservationReservationHolidayApiAdapter = reservationReservationHolidayApiAdapter

    def reservation_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} reservation_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : reservation_out_port get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : reservation_out_port get kwarg ==> {kwarg}")

        result = self.reservationReservationHolidayApiAdapter.reservation_reservation_holiday_crm_api(api_host=args[1],
                                                                                                      path=args[2],
                                                                                                      method=args[3],
                                                                                                      data=args[4],
                                                                                                      accessToken=
                                                                                                      kwargs[
                                                                                                          'accessToken'],
                                                                                                      refreshToken=
                                                                                                      kwargs[
                                                                                                          'refreshToken'])

        return result
