from abc import ABC, abstractmethod

from ....adapter.out.customer_customer_grid_list_api_adapter import CustomerCustomerGridListApiAdapter


class CustomerCustomerGridListOutPort(ABC):
    """
    # CLASS : CustomerCustomerGridListOutPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/09 2:18 PM
    # DESCRIPTION
        - CustomerGridList Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/09          jung-gyuho          최초 생성
    """

    @abstractmethod
    def customer_out_port(self, request):
        pass


class CustomerCustomerGridListOutCrmImpl(CustomerCustomerGridListOutPort):

    def __init__(self, customerCustomerGridListApiAdapter: CustomerCustomerGridListApiAdapter):
        self.customerCustomerGridListApiAdapter = customerCustomerGridListApiAdapter

    def customer_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} customer_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : customer_out_port get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : customer_out_port get kwarg ==> {kwarg}")

        result = self.customerCustomerGridListApiAdapter.customer_customer_grid_list_crm_api(api_host=args[1],
                                                                                             path=args[2],
                                                                                             method=args[3],
                                                                                             data=args[4],
                                                                                             accessToken=kwargs[
                                                                                                 'accessToken'],
                                                                                             refreshToken=kwargs[
                                                                                                 'refreshToken'])

        return result
