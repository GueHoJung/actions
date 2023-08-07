from abc import ABC, abstractmethod

from ....adapter.out.analysis_dash_board_info_api_adapter import AnalysisDashBoardInfoApiAdapter


class AnalysisDashBoardInfoOutPort(ABC):
    """
    # CLASS : AnalysisDashBoardInfoOutPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/31 5:00 PM
    # DESCRIPTION
        - DashBoardInfo Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/31          jung-gyuho          최초 생성
    """

    @abstractmethod
    def analysis_out_port(self, request):
        pass


class AnalysisDashBoardInfoOutCrmImpl(AnalysisDashBoardInfoOutPort):

    def __init__(self, analysisDashBoardInfoApiAdapter: AnalysisDashBoardInfoApiAdapter):
        self.analysisDashBoardInfoApiAdapter = analysisDashBoardInfoApiAdapter

    def analysis_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} analysis_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : analysis_out_port get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : analysis_out_port get kwarg ==> {kwarg}")

        result = self.analysisDashBoardInfoApiAdapter.analysis_dash_board_info_crm_api(api_host=args[1], path=args[2],
                                                                                       method=args[3],
                                                                                       data=args[4],
                                                                                       accessToken=kwargs[
                                                                                           'accessToken'],
                                                                                       refreshToken=kwargs[
                                                                                           'refreshToken'])

        return result
