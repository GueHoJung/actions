from abc import ABC, abstractmethod


class OrderPrepaidInfoInPort(ABC):
    """
    # CLASS : OrderInPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/28 6:54 PM
    # DESCRIPTION

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/28          jung-gyuho          최초 생성
    """

    @abstractmethod
    def order_in_port(self, request):
        pass


class OrderPrepaidInfoInCrmImpl(OrderPrepaidInfoInPort):

    def __init__(self):
        pass

    def order_in_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} order_in request ==> {args[0]}")
        result = args[0]

        return result
