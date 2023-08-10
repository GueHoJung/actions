from ..port._in.reservation_save_reservation_holiday_in_port import ReservationSaveReservationHolidayInPort
from ..port.out.reservation_save_reservation_holiday_out_port import ReservationSaveReservationHolidayOutPort
import config.utils.common_utils as common_utils
from django.conf import settings
import logging

logger = logging.getLogger("django.server")


class ReservationSaveReservationHolidayService:
    """
    # CLASS : ReservationSaveReservationHolidayService
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/08 10:29 PM
    # DESCRIPTION
        - SaveReservationHoliday Service

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/08          jung-gyuho          최초 생성
    """

    def __init__(self, portInImpl: ReservationSaveReservationHolidayInPort,
                 portOutImpl: ReservationSaveReservationHolidayOutPort):
        self.reservationIn = portInImpl
        self.reservationOut = portOutImpl

    def reservation_save_reservation_holiday_crm(self, *args, **kwargs):
        print(f"{self.__class__.__name__} reservation_save_reservation_holiday_crm *args ==> {args[0]}")

        data = self.reservationIn.reservation_in_port(self, args[0])

        for arg in args:
            print(f"{self.__class__.__name__} reservation_save_reservation_holiday_crm *args ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} reservation_save_reservation_holiday_crm **kwargs ==> {kwarg}")

        API_HOST = getattr(settings, "CRM_HOST_IP", None)
        API_PORT = getattr(settings, "CRM_HOST_PORT", None)
        API_ADR = API_HOST + ":" + API_PORT
        print(f"Api host ==> {API_HOST}")
        result = self.reservationOut.reservation_out_port(self, API_ADR, "/reservation/saveReservationHoliday/", "POST",
                                                          data,
                                                          accessToken=kwargs['accessToken'],
                                                          refreshToken=kwargs['refreshToken'])

        jtOResult = common_utils.convert_json_to_obj(result['data'])
        # print(f"{self.__class__.__name__} : analysis_trm_type_user_sales_crm get result ==> {result}")
        # print(f"{self.__class__.__name__} : analysis_trm_type_user_sales_crm get jResult ==> {jtOResult}")
        logger.info(f"{self.__class__.__name__} : analysis_trm_type_user_sales_crm get jResult ==> {jtOResult}")

        return jtOResult
