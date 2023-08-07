from abc import ABC, abstractmethod


class StatsDailyProductUserPerformanceInPort(ABC):
    """
    # CLASS : StatsDailyProductUserPerformanceInPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/04 3:31 PM
    # DESCRIPTION

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/04          jung-gyuho          최초 생성
    """

    @abstractmethod
    def stats_in_port(self, request):
        pass


class StatsDailyProductUserPerformanceInCrmImpl(StatsDailyProductUserPerformanceInPort):

    def __init__(self):
        pass

    def stats_in_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} stats_in request ==> {args[0]}")
        result = args[0]

        return result
