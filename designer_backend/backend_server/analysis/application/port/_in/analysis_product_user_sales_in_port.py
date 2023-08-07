from abc import ABC, abstractmethod


class AnalysisProductUserSalesInPort(ABC):
    """
    # CLASS : AnalysisProductUserSalesInPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/31 4:36 PM
    # DESCRIPTION

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/31          jung-gyuho          최초 생성
    """

    @abstractmethod
    def analysis_in_port(self, request):
        pass


class AnalysisProductUserSalesInCrmImpl(AnalysisProductUserSalesInPort):

    def __init__(self):
        pass

    def analysis_in_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} analysis_in request ==> {args[0]}")
        result = args[0]

        return result
