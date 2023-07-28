from abc import ABC, abstractmethod


class OrderPrepaidHistoryListInPort(ABC):
    """
    # CLASS : OrderPrepaidHistoryListInPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/28 8:55 PM
    # DESCRIPTION

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/28          jung-gyuho          최초 생성
    """

    @abstractmethod
    def order_in_port(self, request):
        pass


class OrderPrepaidHistoryListInCrmImpl(OrderPrepaidHistoryListInPort):

    def __init__(self):
        pass

    def order_in_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} order_in request ==> {args[0]}")
        result = args[0]

        return result
