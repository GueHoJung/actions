from abc import ABC, abstractmethod

from ....adapter.out.customer_modify_cust_info_api_adapter import CustomerModifyCustInfoApiAdapter


class CustomerModifyCustInfoOutPort(ABC):
    """
    # CLASS : CustomerModifyCustInfoOutPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/28 10:35 PM
    # DESCRIPTION
        - ModifyCustInfo Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/28          jung-gyuho          최초 생성
    """

    @abstractmethod
    def customer_out_port(self, request):
        pass


class CustomerModifyCustInfoOutCrmImpl(CustomerModifyCustInfoOutPort):

    def __init__(self, customerModifyCustInfoApiAdapter: CustomerModifyCustInfoApiAdapter):
        self.customerModifyCustInfoApiAdapter = customerModifyCustInfoApiAdapter

    def customer_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} customer_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : customer_out_port get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : customer_out_port get kwarg ==> {kwarg}")

        result = self.customerModifyCustInfoApiAdapter.customer_modify_cust_info_crm_api(api_host=args[1], path=args[2],
                                                                                         method=args[3],
                                                                                         data=args[4],
                                                                                         accessToken=kwargs[
                                                                                             'accessToken'],
                                                                                         refreshToken=kwargs[
                                                                                             'refreshToken'])

        return result
