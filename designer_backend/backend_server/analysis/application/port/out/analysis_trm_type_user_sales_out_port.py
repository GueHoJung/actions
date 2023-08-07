from abc import ABC, abstractmethod

from ....adapter.out.analysis_trm_type_user_sales_api_adapter import AnalysisTrmTypeUserSalesApiAdapter


class AnalysisTrmTypeUserSalesOutPort(ABC):
    """
    # CLASS : AnalysisTrmTypeUserSalesOutPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/07 5:04 PM
    # DESCRIPTION
        - TrmTypeUserSales Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/07          jung-gyuho          최초 생성
    """

    @abstractmethod
    def analysis_out_port(self, request):
        pass


class AnalysisTrmTypeUserSalesOutCrmImpl(AnalysisTrmTypeUserSalesOutPort):

    def __init__(self, analysisTrmTypeUserSalesApiAdapter: AnalysisTrmTypeUserSalesApiAdapter):
        self.analysisTrmTypeUserSalesApiAdapter = analysisTrmTypeUserSalesApiAdapter

    def analysis_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} analysis_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : analysis_out_port get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : analysis_out_port get kwarg ==> {kwarg}")

        result = self.analysisTrmTypeUserSalesApiAdapter.analysis_trm_type_user_sales_crm_api(api_host=args[1],
                                                                                              path=args[2],
                                                                                              method=args[3],
                                                                                              data=args[4],
                                                                                              accessToken=kwargs[
                                                                                                  'accessToken'],
                                                                                              refreshToken=kwargs[
                                                                                                  'refreshToken'])

        return result
