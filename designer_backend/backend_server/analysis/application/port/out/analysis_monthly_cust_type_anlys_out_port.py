from abc import ABC, abstractmethod

from ....adapter.out.analysis_monthly_cust_type_anlys_api_adapter import AnalysisMonthlyCustTypeAnlysApiAdapter


class AnalysisMonthlyCustTypeAnlysOutPort(ABC):
    """
    # CLASS : AnalysisMonthlyCustTypeAnlysOutPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/07 6:10 PM
    # DESCRIPTION
        - MonthlyCustTypeAnlys Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/07          jung-gyuho          최초 생성
    """

    @abstractmethod
    def analysis_out_port(self, request):
        pass


class AnalysisMonthlyCustTypeAnlysOutCrmImpl(AnalysisMonthlyCustTypeAnlysOutPort):

    def __init__(self, analysisMonthlyCustTypeAnlysApiAdapter: AnalysisMonthlyCustTypeAnlysApiAdapter):
        self.analysisMonthlyCustTypeAnlysApiAdapter = analysisMonthlyCustTypeAnlysApiAdapter

    def analysis_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} analysis_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : analysis_out_port get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : analysis_out_port get kwarg ==> {kwarg}")

        result = self.analysisMonthlyCustTypeAnlysApiAdapter.analysis_monthly_cust_type_anlys_crm_api(api_host=args[1],
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
