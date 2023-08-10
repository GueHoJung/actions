from abc import ABC, abstractmethod

from ....adapter.out.analysis_monthly_dprtr_anlys_api_adapter import AnalysisMonthlyDprtrAnlysApiAdapter


class AnalysisMonthlyDprtrAnlysOutPort(ABC):
    """
    # CLASS : AnalysisMonthlyDprtrAnlysOutPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/08 4:12 PM
    # DESCRIPTION
        - MonthlyDprtrAnlys Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/08          jung-gyuho          최초 생성
    """

    @abstractmethod
    def analysis_out_port(self, request):
        pass


class AnalysisMonthlyDprtrAnlysOutCrmImpl(AnalysisMonthlyDprtrAnlysOutPort):

    def __init__(self, analysisMonthlyDprtrAnlysApiAdapter: AnalysisMonthlyDprtrAnlysApiAdapter):
        self.analysisMonthlyDprtrAnlysApiAdapter = analysisMonthlyDprtrAnlysApiAdapter

    def analysis_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} analysis_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : analysis_out_port get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : analysis_out_port get kwarg ==> {kwarg}")

        result = self.analysisMonthlyDprtrAnlysApiAdapter.analysis_monthly_dprtr_anlys_crm_api(api_host=args[1],
                                                                                               path=args[2],
                                                                                               method=args[3],
                                                                                               data=args[4],
                                                                                               accessToken=kwargs[
                                                                                                   'accessToken'],
                                                                                               refreshToken=kwargs[
                                                                                                   'refreshToken'])

        return result
