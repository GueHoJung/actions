from abc import ABC, abstractmethod

from ....adapter.out.analysis_user_unit_price_compare_api_adapter import AnalysisUserUnitPriceCompareApiAdapter


class AnalysisUserUnitPriceCompareOutPort(ABC):
    """
    # CLASS : AnalysisUserUnitPriceCompareOutPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/08 6:50 PM
    # DESCRIPTION
        - UserUnitPriceCompare Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/08          jung-gyuho          최초 생성
    """

    @abstractmethod
    def analysis_out_port(self, request):
        pass


class AnalysisUserUnitPriceCompareOutCrmImpl(AnalysisUserUnitPriceCompareOutPort):

    def __init__(self, analysisUserUnitPriceCompareApiAdapter: AnalysisUserUnitPriceCompareApiAdapter):
        self.analysisUserUnitPriceCompareApiAdapter = analysisUserUnitPriceCompareApiAdapter

    def analysis_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} analysis_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : analysis_out_port get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : analysis_out_port get kwarg ==> {kwarg}")

        result = self.analysisUserUnitPriceCompareApiAdapter.analysis_user_unit_price_compare_crm_api(api_host=args[1],
                                                                                                      path=args[2],
                                                                                                      method=args[3],
                                                                                                      data=args[4],
                                                                                                      accessToken=
                                                                                                      kwargs[
                                                                                                          'accessToken'],
                                                                                                      refreshToken=
                                                                                                      kwargs[
                                                                                                          'refreshToken'])

        return result
