from abc import ABC, abstractmethod

from ....adapter.out.reservation_save_rsrv_holiday_schedule_api_adapter import \
    ReservationSaveRsrvHolidayScheduleApiAdapter


class ReservationSaveRsrvHolidayScheduleOutPort(ABC):
    """
    # CLASS : ReservationSaveRsrvHolidayScheduleOutPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/08 10:46 PM
    # DESCRIPTION
        - SaveRsrvHolidaySchedule Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/08          jung-gyuho          최초 생성
    """

    @abstractmethod
    def reservation_out_port(self, request):
        pass


class ReservationSaveRsrvHolidayScheduleOutCrmImpl(ReservationSaveRsrvHolidayScheduleOutPort):

    def __init__(self, reservationSaveRsrvHolidayScheduleApiAdapter: ReservationSaveRsrvHolidayScheduleApiAdapter):
        self.reservationSaveRsrvHolidayScheduleApiAdapter = reservationSaveRsrvHolidayScheduleApiAdapter

    def reservation_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} reservation_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : reservation_out_port get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : reservation_out_port get kwarg ==> {kwarg}")

        result = self.reservationSaveRsrvHolidayScheduleApiAdapter.reservation_save_rsrv_holiday_schedule_crm_api(
            api_host=args[1], path=args[2],
            method=args[3],
            data=args[4],
            accessToken=kwargs[
                'accessToken'],
            refreshToken=kwargs[
                'refreshToken'])

        return result
