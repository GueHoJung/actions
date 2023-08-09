from abc import ABC, abstractmethod


class CustomerCustomerGridListInPort(ABC):
    """
    # CLASS : CustomerCustomerGridListInPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/09 2:18 PM
    # DESCRIPTION

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/09          jung-gyuho          최초 생성
    """

    @abstractmethod
    def customer_in_port(self, request):
        pass


class CustomerCustomerGridListInCrmImpl(CustomerCustomerGridListInPort):

    def __init__(self):
        pass

    def customer_in_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} customer_in request ==> {args[0]}")
        result = args[0]

        return result
