from abc import ABC, abstractmethod


class CustomerInPort(ABC):
    """
    # CLASS : CustomerInPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/21 10:32 PM
    # DESCRIPTION
        - 고객 관련 In Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/21          jung-gyuho          최초 생성
    """

    @abstractmethod
    def customer_in_port(self, request):
        pass


class CustomerInCrmImpl(CustomerInPort):

    def __init__(self):
        pass

    def customer_in_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} customer_in request ==> {args[0]}")
        result = args[0]

        return result
