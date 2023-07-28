from abc import ABC, abstractmethod


class CustomerCustTasteListInPort(ABC):
    """
    # CLASS : CustomerCustTasteListInPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/28 10:08 PM
    # DESCRIPTION

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/28          jung-gyuho          최초 생성
    """

    @abstractmethod
    def customer_in_port(self, request):
        pass


class CustomerCustTasteListInCrmImpl(CustomerCustTasteListInPort):

    def __init__(self):
        pass

    def customer_in_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} customer_in request ==> {args[0]}")
        result = args[0]

        return result
