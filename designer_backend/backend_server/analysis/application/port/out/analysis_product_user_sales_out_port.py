from abc import ABC, abstractmethod

from ....adapter.out.analysis_product_user_sales_api_adapter import AnalysisProductUserSalesApiAdapter


class AnalysisProductUserSalesOutPort(ABC):
    """
    # CLASS : AnalysisProductUserSalesOutPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/31 4:36 PM
    # DESCRIPTION
        - ProductUserSales Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/31          jung-gyuho          최초 생성
    """

    @abstractmethod
    def analysis_out_port(self, request):
        pass


class AnalysisProductUserSalesOutCrmImpl(AnalysisProductUserSalesOutPort):

    def __init__(self, analysisProductUserSalesApiAdapter: AnalysisProductUserSalesApiAdapter):
        self.analysisProductUserSalesApiAdapter = analysisProductUserSalesApiAdapter

    def analysis_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} analysis_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : analysis_out_port get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : analysis_out_port get kwarg ==> {kwarg}")

        result = self.analysisProductUserSalesApiAdapter.analysis_product_user_sales_crm_api(api_host=args[1],
                                                                                             path=args[2],
                                                                                             method=args[3],
                                                                                             data=args[4],
                                                                                             accessToken=kwargs[
                                                                                                 'accessToken'],
                                                                                             refreshToken=kwargs[
                                                                                                 'refreshToken'])

        return result
