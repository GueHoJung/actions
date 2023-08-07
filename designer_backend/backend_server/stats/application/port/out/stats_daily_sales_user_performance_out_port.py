from abc import ABC, abstractmethod

from ....adapter.out.stats_daily_sales_user_performance_api_adapter import StatsDailySalesUserPerformanceApiAdapter


class StatsDailySalesUserPerformanceOutPort(ABC):
    """
    # CLASS : StatsDailySalesUserPerformanceOutPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/31 6:04 PM
    # DESCRIPTION
        - DailySalesUserPerformance Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/31          jung-gyuho          최초 생성
    """

    @abstractmethod
    def stats_out_port(self, request):
        pass


class StatsDailySalesUserPerformanceOutCrmImpl(StatsDailySalesUserPerformanceOutPort):

    def __init__(self, statsDailySalesUserPerformanceApiAdapter: StatsDailySalesUserPerformanceApiAdapter):
        self.statsDailySalesUserPerformanceApiAdapter = statsDailySalesUserPerformanceApiAdapter

    def stats_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} stats_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : stats_out_port get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : stats_out_port get kwarg ==> {kwarg}")

        result = self.statsDailySalesUserPerformanceApiAdapter.stats_daily_sales_user_performance_crm_api(
            api_host=args[1], path=args[2],
            method=args[3],
            data=args[4],
            accessToken=kwargs['accessToken'],
            refreshToken=kwargs['refreshToken'])

        return result
