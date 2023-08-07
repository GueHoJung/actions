from abc import ABC, abstractmethod

from ....adapter.out.stats_monthly_sales_user_sales_api_adapter import StatsMonthlySalesUserSalesApiAdapter


class StatsMonthlySalesUserSalesOutPort(ABC):
    """
    # CLASS : StatsMonthlySalesUserSalesOutPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/31 6:49 PM
    # DESCRIPTION
        - MonthlySalesUserSales Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/31          jung-gyuho          최초 생성
    """

    @abstractmethod
    def stats_out_port(self, request):
        pass


class StatsMonthlySalesUserSalesOutCrmImpl(StatsMonthlySalesUserSalesOutPort):

    def __init__(self, statsMonthlySalesUserSalesApiAdapter: StatsMonthlySalesUserSalesApiAdapter):
        self.statsMonthlySalesUserSalesApiAdapter = statsMonthlySalesUserSalesApiAdapter

    def stats_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} stats_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : stats_out_port get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : stats_out_port get kwarg ==> {kwarg}")

        result = self.statsMonthlySalesUserSalesApiAdapter.stats_monthly_sales_user_sales_crm_api(api_host=args[1],
                                                                                                  path=args[2],
                                                                                                  method=args[3],
                                                                                                  data=args[4],
                                                                                                  accessToken=kwargs[
                                                                                                      'accessToken'],
                                                                                                  refreshToken=kwargs[
                                                                                                      'refreshToken'])

        return result
