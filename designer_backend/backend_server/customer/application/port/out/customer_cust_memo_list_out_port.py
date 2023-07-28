from abc import ABC, abstractmethod

from ....adapter.out.customer_cust_memo_list_api_adapter import CustomerCustMemoListApiAdapter


class CustomerCustMemoListOutPort(ABC):
    """
    # CLASS : CustomerCustMemoListOutPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/28 9:47 PM
    # DESCRIPTION
        - CustMemoList Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/28          jung-gyuho          최초 생성
    """

    @abstractmethod
    def customer_out_port(self, request):
        pass


class CustomerCustMemoListOutCrmImpl(CustomerCustMemoListOutPort):

    def __init__(self, customerCustMemoListApiAdapter: CustomerCustMemoListApiAdapter):
        self.customerCustMemoListApiAdapter = customerCustMemoListApiAdapter

    def customer_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} customer_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : customer_out_port get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : customer_out_port get kwarg ==> {kwarg}")

        result = self.customerCustMemoListApiAdapter.customer_cust_memo_list_crm_api(api_host=args[1], path=args[2],
                                                                                     method=args[3],
                                                                                     data=args[4],
                                                                                     accessToken=kwargs['accessToken'],
                                                                                     refreshToken=kwargs[
                                                                                         'refreshToken'])

        return result
