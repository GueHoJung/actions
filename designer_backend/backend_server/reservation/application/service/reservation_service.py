from ..port._in.reservation_in_port import ReservationInPort
from ..port.out.reservation_out_port import ReservationOutPort
import config.utils.common_utils as CommonUtils
from django.conf import settings

class ReservationService:

    def __init__(self, portInImpl: ReservationInPort, portOutImpl: ReservationOutPort):
        self.reservationIn = portInImpl
        self.reservationOut = portOutImpl

    def reservation_crm(self, *args, **kwargs):
        print(f"{self.__class__.__name__} reservation_crm *args ==> {args[0]}")

        request = self.reservationIn.reservation_in_port(self, args[0])

        API_HOST = getattr(settings, "CRM_HOST_IP", None)
        API_PORT = getattr(settings, "CRM_HOST_PORT", None)
        API_ADR = API_HOST + ":" + API_PORT
        print(f"Api host ==> {API_HOST}")
        print(f"Api port ==> {API_PORT}")
        print(f"Api adr ==> {API_ADR}")

        for arg in args:
            print(f"{self.__class__.__name__} : reservation_crm get arg ==> {arg}")

        result = self.reservationOut.reservation_out_port(self, API_ADR, "/reservation/getPopRsrvDetailInfo/", "POST", request)

        jtOResult = CommonUtils.convert_json_to_obj(result)
        print(f"{self.__class__.__name__} : reservation_crm get result ==> {result}")
        print(f"{self.__class__.__name__} : reservation_crm get jResult ==> {jtOResult}")

        return jtOResult
