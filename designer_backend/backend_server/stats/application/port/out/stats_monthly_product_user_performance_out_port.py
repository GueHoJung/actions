from abc import ABC, abstractmethod

from ....adapter.out.stats_monthly_product_user_performance_api_adapter import \
    StatsMonthlyProductUserPerformanceApiAdapter


class StatsMonthlyProductUserPerformanceOutPort(ABC):
    """
    # CLASS : StatsMonthlyProductUserPerformanceOutPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/07 11:59 AM
    # DESCRIPTION
        - MonthlyProductUserPerformance Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/07          jung-gyuho          최초 생성
    """

    @abstractmethod
    def stats_out_port(self, request):
        pass


class StatsMonthlyProductUserPerformanceOutCrmImpl(StatsMonthlyProductUserPerformanceOutPort):

    def __init__(self, statsMonthlyProductUserPerformanceApiAdapter: StatsMonthlyProductUserPerformanceApiAdapter):
        self.statsMonthlyProductUserPerformanceApiAdapter = statsMonthlyProductUserPerformanceApiAdapter

    def stats_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} stats_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : stats_out_port get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : stats_out_port get kwarg ==> {kwarg}")

        result = self.statsMonthlyProductUserPerformanceApiAdapter.stats_monthly_product_user_performance_crm_api(
            api_host=args[1], path=args[2],
            method=args[3],
            data=args[4],
            accessToken=kwargs['accessToken'],
            refreshToken=kwargs['refreshToken'])

        return result
