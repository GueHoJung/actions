from abc import ABC, abstractmethod

from ....adapter.out.customer_api_adapter import CustomerApiAdapter


class CustomerOutPort(ABC):
    """
    # CLASS : CustomerOutPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/21 10:32 PM
    # DESCRIPTION
        - 고객 관련 Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/21          jung-gyuho          최초 생성
    """

    @abstractmethod
    def customer_out_port(self, request):
        pass


class CustomerOutCrmImpl(CustomerOutPort):

    def __init__(self, customerApiAdapter: CustomerApiAdapter):
        self.customerApiAdapter = customerApiAdapter

    def customer_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} customer_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : customer_out_port get arg ==> {arg}")

        result = self.customerApiAdapter.customer_info_crm_api(api_host=args[1], path=args[2], method=args[3],
                                                               data=args[4])

        return result
