from abc import ABC, abstractmethod


class StatsMonthlyProductUserPerformanceInPort(ABC):
    """
    # CLASS : StatsMonthlyProductUserPerformanceInPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/07 11:58 AM
    # DESCRIPTION

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/07          jung-gyuho          최초 생성
    """

    @abstractmethod
    def stats_in_port(self, request):
        pass


class StatsMonthlyProductUserPerformanceInCrmImpl(StatsMonthlyProductUserPerformanceInPort):

    def __init__(self):
        pass

    def stats_in_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} stats_in request ==> {args[0]}")
        result = args[0]

        return result
