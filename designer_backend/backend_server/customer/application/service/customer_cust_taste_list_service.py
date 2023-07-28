from ..port._in.customer_cust_taste_list_in_port import CustomerCustTasteListInPort
from ..port.out.customer_cust_taste_list_out_port import CustomerCustTasteListOutPort
import config.utils.common_utils as common_utils
from django.conf import settings


class CustomerCustTasteListService:
    """
    # CLASS : CustomerCustTasteListServie
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/28 10:09 PM
    # DESCRIPTION
        - CustTasteList Service

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/28          jung-gyuho          최초 생성
    """

    def __init__(self, portInImpl: CustomerCustTasteListInPort, portOutImpl: CustomerCustTasteListOutPort):
        self.customerIn = portInImpl
        self.customerOut = portOutImpl

    def customer_cust_taste_list_crm(self, *args, **kwargs):
        print(f"{self.__class__.__name__} customer_cust_taste_list_crm *args ==> {args[0]}")

        data = self.customerIn.customer_in_port(self, args[0])

        for arg in args:
            print(f"{self.__class__.__name__} customer_cust_taste_list_crm *args ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} customer_cust_taste_list_crm **kwargs ==> {kwarg}")

        API_HOST = getattr(settings, "CRM_HOST_IP", None)
        API_PORT = getattr(settings, "CRM_HOST_PORT", None)
        API_ADR = API_HOST + ":" + API_PORT
        print(f"Api host ==> {API_HOST}")
        result = self.customerOut.customer_out_port(self, API_ADR, "/customer/getCustTasteList/", "POST", data,
                                                    accessToken=kwargs['accessToken'],
                                                    refreshToken=kwargs['refreshToken'])

        jtOResult = common_utils.convert_json_to_obj(result['data'])
        print(f"{self.__class__.__name__} : customer_cust_taste_list_crm get result ==> {result}")
        print(f"{self.__class__.__name__} : customer_cust_taste_list_crm get jResult ==> {jtOResult}")

        return jtOResult
