from abc import ABC, abstractmethod


class ReservationInPort(ABC):
    @abstractmethod
    def reservation_in_port(self, request):
        pass


class ReservationInCrmImpl(ReservationInPort):

    def __init__(self):
        pass

    def reservation_in_port(self, *args, **kwargs):
        print(f"LoginCrmInAPI login_in request ==> {args[0]}")
        result = args[0]

        return result
