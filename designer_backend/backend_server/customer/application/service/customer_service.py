from ..port._in.customer_in_port import CustomerInPort
from ..port.out.customer_out_port import CustomerOutPort
import config.utils.common_utils as CommontUtils
from django.conf import settings

class CustomerService:
    """
    # CLASS : CustomerService
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/21 10:40 PM
    # DESCRIPTION
        - 고객 관련 Service
    """
    def __init__(self, portInImpl: CustomerInPort, portOutImpl: CustomerOutPort):
        self.customerIn = portInImpl
        self.customerOut = portOutImpl

    def customer_info_crm(self, *args, **kwargs):
        print(f"{self.__class__.__name__} customer_info_crm *args ==> {args[0]}")

        request = self.customerIn.customer_in_port(self, args[0])

        API_HOST = getattr(settings, "CRM_HOST_IP", None)
        API_PORT = getattr(settings, "CRM_HOST_PORT", None)
        API_ADR = API_HOST+":"+API_PORT
        print(f"Api host ==> {API_HOST}")
        result = self.customerOut.customer_out_port(self, API_ADR, "/customer/getCustInfoWithAgr/", "POST", request)

        jtOResult = CommontUtils.convert_json_to_obj(result)
        print(f"{self.__class__.__name__} : customer_info_crm get result ==> {result}")
        print(f"{self.__class__.__name__} : customer_info_crm get jResult ==> {jtOResult}")

        return jtOResult
