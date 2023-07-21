from abc import ABC, abstractmethod

from ....adapter.out.reservation_api_adapter import ReservationApiAdapter


class ReservationOutPort(ABC):
    @abstractmethod
    def reservation_out_port(self, request):
        pass


class ReservationOutCrmAPI(ReservationOutPort):

    def __init__(self, reservationCrmApiAdapter: ReservationApiAdapter):
        self.reservationCrmApiAdapter = reservationCrmApiAdapter

    def reservation_out_port(self, *args, **kwargs):
        print(f"ReservationOutCrmAPI login_out_port args ==> {args[1]}")

        result = self.reservationCrmApiAdapter.reservation_crm_api(path="/reservation/getPopRsrvDetailInfo/", method="POST", data=args[1])

        return result
