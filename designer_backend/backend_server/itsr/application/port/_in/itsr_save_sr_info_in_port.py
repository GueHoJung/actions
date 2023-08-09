from abc import ABC, abstractmethod


class ItsrSaveSrInfoInPort(ABC):
    """
    # CLASS : ItsrSaveSrInfoInPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/09 2:43 PM
    # DESCRIPTION

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/09          jung-gyuho          최초 생성
    """

    @abstractmethod
    def itsr_in_port(self, request):
        pass


class ItsrSaveSrInfoInCrmImpl(ItsrSaveSrInfoInPort):

    def __init__(self):
        pass

    def itsr_in_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} itsr_in request ==> {args[0]}")
        result = args[0]

        return result
