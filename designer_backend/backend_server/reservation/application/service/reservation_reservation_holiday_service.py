from ..port._in.reservation_reservation_holiday_in_port import ReservationReservationHolidayInPort
from ..port.out.reservation_reservation_holiday_out_port import ReservationReservationHolidayOutPort
import config.utils.common_utils as common_utils
from django.conf import settings
import logging

logger = logging.getLogger("django.server")


class ReservationReservationHolidayService:
    """
    # CLASS : ReservationReservationHolidayService
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/08 9:52 PM
    # DESCRIPTION
        - ReservationHoliday Service

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/08          jung-gyuho          최초 생성
    """

    def __init__(self, portInImpl: ReservationReservationHolidayInPort,
                 portOutImpl: ReservationReservationHolidayOutPort):
        self.reservationIn = portInImpl
        self.reservationOut = portOutImpl

    def reservation_reservation_holiday_crm(self, *args, **kwargs):
        print(f"{self.__class__.__name__} reservation_reservation_holiday_crm *args ==> {args[0]}")

        data = self.reservationIn.reservation_in_port(self, args[0])

        for arg in args:
            print(f"{self.__class__.__name__} reservation_reservation_holiday_crm *args ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} reservation_reservation_holiday_crm **kwargs ==> {kwarg}")

        API_HOST = getattr(settings, "CRM_HOST_IP", None)
        API_PORT = getattr(settings, "CRM_HOST_PORT", None)
        API_ADR = API_HOST + ":" + API_PORT
        print(f"Api host ==> {API_HOST}")
        result = self.reservationOut.reservation_out_port(self, API_ADR, "/reservation/getReservationHoliday/", "POST",
                                                          data,
                                                          accessToken=kwargs['accessToken'],
                                                          refreshToken=kwargs['refreshToken'])

        jtOResult = common_utils.convert_json_to_obj(result['data'])
        # print(f"{self.__class__.__name__} : analysis_trm_type_user_sales_crm get result ==> {result}")
        # print(f"{self.__class__.__name__} : analysis_trm_type_user_sales_crm get jResult ==> {jtOResult}")
        logger.info(f"{self.__class__.__name__} : analysis_trm_type_user_sales_crm get jResult ==> {jtOResult}")

        return jtOResult
