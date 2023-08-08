from abc import ABC, abstractmethod


class AnalysisWeeklyInflowAnlysInPort(ABC):
    """
    # CLASS : AnalysisWeeklyInflowAnlysInPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/08 3:12 PM
    # DESCRIPTION

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/08          jung-gyuho          최초 생성
    """

    @abstractmethod
    def analysis_in_port(self, request):
        pass


class AnalysisWeeklyInflowAnlysInCrmImpl(AnalysisWeeklyInflowAnlysInPort):

    def __init__(self):
        pass

    def analysis_in_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} analysis_in request ==> {args[0]}")
        result = args[0]

        return result
