from abc import ABC, abstractmethod


class EmployInPort(ABC):
    """
    # CLASS : EmployInPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/28 6:26 PM
    # DESCRIPTION

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/28          jung-gyuho          최초 생성
    """

    @abstractmethod
    def employ_in_port(self, request):
        pass


class EmployInHrmImpl(EmployInPort):

    def __init__(self):
        pass

    def employ_in_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} employ_in request ==> {args[0]}")
        result = args[0]

        return result
