from abc import ABC, abstractmethod


class AnalysisDailyCustPrepaidAnlysInPort(ABC):
    """
    # CLASS : AnalysisDailyCustPrepaidAnlysInPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/07 9:57 PM
    # DESCRIPTION

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/07          jung-gyuho          최초 생성
    """

    @abstractmethod
    def analysis_in_port(self, request):
        pass


class AnalysisDailyCustPrepaidAnlysInCrmImpl(AnalysisDailyCustPrepaidAnlysInPort):

    def __init__(self):
        pass

    def analysis_in_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} analysis_in request ==> {args[0]}")
        result = args[0]

        return result
