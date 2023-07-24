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
        print(f"{self.__class__.__name__} login_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : login_out_port get arg ==> {arg}")

        result = self.reservationCrmApiAdapter.reservation_crm_api(api_host=args[1], path=args[2], method=args[3], data=args[4])

        return result
