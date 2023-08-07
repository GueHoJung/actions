from abc import ABC, abstractmethod

from ....adapter.out.stats_daily_sales_user_sales_api_adapter import StatsDailySalesUserSalesApiAdapter


class StatsDailySalesUserSalesOutPort(ABC):
    """
    # CLASS : StatsDailySalesUserSalesOutPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/31 7:00 PM
    # DESCRIPTION
        - DailySalesUserSales Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/31          jung-gyuho          최초 생성
    """

    @abstractmethod
    def stats_out_port(self, request):
        pass


class StatsDailySalesUserSalesOutCrmImpl(StatsDailySalesUserSalesOutPort):

    def __init__(self, statsDailySalesUserSalesApiAdapter: StatsDailySalesUserSalesApiAdapter):
        self.statsDailySalesUserSalesApiAdapter = statsDailySalesUserSalesApiAdapter

    def stats_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} stats_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : stats_out_port get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : stats_out_port get kwarg ==> {kwarg}")

        result = self.statsDailySalesUserSalesApiAdapter.stats_daily_sales_user_sales_crm_api(api_host=args[1],
                                                                                              path=args[2],
                                                                                              method=args[3],
                                                                                              data=args[4],
                                                                                              accessToken=kwargs[
                                                                                                  'accessToken'],
                                                                                              refreshToken=kwargs[
                                                                                                  'refreshToken'])

        return result
