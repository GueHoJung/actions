from abc import ABC, abstractmethod

from ....adapter.out.stats_yearly_sales_user_order_type_sales_api_adapter import \
    StatsYearlySalesUserOrderTypeSalesApiAdapter


class StatsYearlySalesUserOrderTypeSalesOutPort(ABC):
    """
    # CLASS : StatsYearlySalesUserOrderTypeSalesOutPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/04 1:36 PM
    # DESCRIPTION
        - YearlySalesUserOrderTypeSales Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/04          jung-gyuho          최초 생성
    """

    @abstractmethod
    def stats_out_port(self, request):
        pass


class StatsYearlySalesUserOrderTypeSalesOutCrmImpl(StatsYearlySalesUserOrderTypeSalesOutPort):

    def __init__(self, statsYearlySalesUserOrderTypeSalesApiAdapter: StatsYearlySalesUserOrderTypeSalesApiAdapter):
        self.statsYearlySalesUserOrderTypeSalesApiAdapter = statsYearlySalesUserOrderTypeSalesApiAdapter

    def stats_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} stats_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : stats_out_port get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : stats_out_port get kwarg ==> {kwarg}")

        result = self.statsYearlySalesUserOrderTypeSalesApiAdapter.stats_yearly_sales_user_order_type_sales_crm_api(
            api_host=args[1], path=args[2],
            method=args[3],
            data=args[4],
            accessToken=kwargs['accessToken'],
            refreshToken=kwargs['refreshToken'])

        return result
