from abc import ABC, abstractmethod

from ....adapter.out.reservation_mod_rsrv_holiday_schedule_api_adapter import \
    ReservationModRsrvHolidayScheduleApiAdapter


class ReservationModRsrvHolidayScheduleOutPort(ABC):
    """
    # CLASS : ReservationModRsrvHolidayScheduleOutPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/08 10:18 PM
    # DESCRIPTION
        - ModRsrvHolidaySchedule Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/08          jung-gyuho          최초 생성
    """

    @abstractmethod
    def reservation_out_port(self, request):
        pass


class ReservationModRsrvHolidayScheduleOutCrmImpl(ReservationModRsrvHolidayScheduleOutPort):

    def __init__(self, reservationModRsrvHolidayScheduleApiAdapter: ReservationModRsrvHolidayScheduleApiAdapter):
        self.reservationModRsrvHolidayScheduleApiAdapter = reservationModRsrvHolidayScheduleApiAdapter

    def reservation_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} reservation_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : reservation_out_port get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : reservation_out_port get kwarg ==> {kwarg}")

        result = self.reservationModRsrvHolidayScheduleApiAdapter.reservation_mod_rsrv_holiday_schedule_crm_api(
            api_host=args[1], path=args[2],
            method=args[3],
            data=args[4],
            accessToken=kwargs[
                'accessToken'],
            refreshToken=kwargs[
                'refreshToken'])

        return result
