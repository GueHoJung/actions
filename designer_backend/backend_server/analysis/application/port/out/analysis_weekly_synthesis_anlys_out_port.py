from abc import ABC, abstractmethod

from ....adapter.out.analysis_weekly_synthesis_anlys_api_adapter import AnalysisWeeklySynthesisAnlysApiAdapter


class AnalysisWeeklySynthesisAnlysOutPort(ABC):
    """
    # CLASS : AnalysisWeeklySynthesisAnlysOutPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/07 7:55 PM
    # DESCRIPTION
        - WeeklySynthesisAnlys Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/07          jung-gyuho          최초 생성
    """

    @abstractmethod
    def analysis_out_port(self, request):
        pass


class AnalysisWeeklySynthesisAnlysOutCrmImpl(AnalysisWeeklySynthesisAnlysOutPort):

    def __init__(self, analysisWeeklySynthesisAnlysApiAdapter: AnalysisWeeklySynthesisAnlysApiAdapter):
        self.analysisWeeklySynthesisAnlysApiAdapter = analysisWeeklySynthesisAnlysApiAdapter

    def analysis_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} analysis_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : analysis_out_port get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : analysis_out_port get kwarg ==> {kwarg}")

        result = self.analysisWeeklySynthesisAnlysApiAdapter.analysis_weekly_synthesis_anlys_crm_api(api_host=args[1],
                                                                                                     path=args[2],
                                                                                                     method=args[3],
                                                                                                     data=args[4],
                                                                                                     accessToken=kwargs[
                                                                                                         'accessToken'],
                                                                                                     refreshToken=
                                                                                                     kwargs[
                                                                                                         'refreshToken'])

        return result
