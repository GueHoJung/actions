from abc import ABC, abstractmethod


class ReservationModReservationHolidayInPort(ABC):
    """
    # CLASS : ReservationModReservationHolidayInPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/08 10:36 PM
    # DESCRIPTION

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/08          jung-gyuho          최초 생성
    """

    @abstractmethod
    def reservation_in_port(self, request):
        pass


class ReservationModReservationHolidayInCrmImpl(ReservationModReservationHolidayInPort):

    def __init__(self):
        pass

    def reservation_in_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} reservation_in request ==> {args[0]}")
        result = args[0]

        return result
