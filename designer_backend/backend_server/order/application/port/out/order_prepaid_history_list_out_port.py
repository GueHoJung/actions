from abc import ABC, abstractmethod

from ....adapter.out.order_prepaid_history_list_api_adapter import OrderPrepaidHistoryListApiAdapter


class OrderPrepaidHistoryListOutPort(ABC):
    """
    # CLASS : OrderPrepaidHistoryListOurPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/28 8:55 PM
    # DESCRIPTION
        - Prepaid history list Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/28          jung-gyuho          최초 생성
    """

    @abstractmethod
    def order_out_port(self, request):
        pass


class OrderPrepaidHistoryListOutCrmImpl(OrderPrepaidHistoryListOutPort):

    def __init__(self, orderPrepaidHistoryListApiAdapter: OrderPrepaidHistoryListApiAdapter):
        self.orderPrepaidHistoryListApiAdapter = orderPrepaidHistoryListApiAdapter

    def order_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} order_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : order_out_port get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : order_out_port get kwarg ==> {kwarg}")

        result = self.orderPrepaidHistoryListApiAdapter.order_prepaid_history_list_crm_api(api_host=args[1], path=args[2],
                                                                         method=args[3],
                                                                         data=args[4],
                                                                         accessToken=kwargs['accessToken'],
                                                                         refreshToken=kwargs['refreshToken'])

        return result
