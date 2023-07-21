from ..port._in.reservation_in_port import ReservationInPort
from ..port.out.reservation_out_port import ReservationOutPort
import config.utils.common_utils as CommonUtils


class ReservationService:

    def __init__(self, portInImpl: ReservationInPort, portOutImpl: ReservationOutPort):
        self.reservationIn = portInImpl
        self.reservationOut = portOutImpl

    def reservation_crm(self, *args, **kwargs):
        print(f"ReservationService reservation_crm *args ==> {args[0]}")

        request = self.reservationIn.reservation_in_port(self, args[0])
        result = self.reservationOut.reservation_out_port(self, request)

        jtOResult = CommonUtils.convert_json_to_obj(result)
        print(f"ReservationService : reservation_crm get result ==> {result}")
        print(f"ReservationService : reservation_crm get jResult ==> {jtOResult}")

        return jtOResult
