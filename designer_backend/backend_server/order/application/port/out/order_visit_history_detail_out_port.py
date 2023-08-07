from abc import ABC, abstractmethod

from ....adapter.out.order_visit_history_detail_api_adapter import OrderVisitHistoryDetailApiAdapter


class OrderVisitHistoryDetailOutPort(ABC):
    """
    # CLASS : OrderVisitHistoryDetailOutPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/31 4:19 PM
    # DESCRIPTION
        - VisitHistoryDetail Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/31          jung-gyuho          최초 생성
    """

    @abstractmethod
    def order_out_port(self, request):
        pass


class OrderVisitHistoryDetailOutCrmImpl(OrderVisitHistoryDetailOutPort):

    def __init__(self, orderVisitHistoryDetailApiAdapter: OrderVisitHistoryDetailApiAdapter):
        self.orderVisitHistoryDetailApiAdapter = orderVisitHistoryDetailApiAdapter

    def order_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} order_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : order_out_port get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : order_out_port get kwarg ==> {kwarg}")

        result = self.orderVisitHistoryDetailApiAdapter.order_visit_history_detail_crm_api(api_host=args[1],
                                                                                           path=args[2],
                                                                                           method=args[3],
                                                                                           data=args[4],
                                                                                           accessToken=kwargs[
                                                                                               'accessToken'],
                                                                                           refreshToken=kwargs[
                                                                                               'refreshToken'])

        return result
