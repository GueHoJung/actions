from ..port._in.customer_customer_grid_list_in_port import CustomerCustomerGridListInPort
from ..port.out.customer_customer_grid_list_out_port import CustomerCustomerGridListOutPort
import config.utils.common_utils as common_utils
from django.conf import settings
import logging

logger = logging.getLogger("django.server")


class CustomerCustomerGridListService:
    """
    # CLASS : CustomerCustomerGridListService
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/09 2:19 PM
    # DESCRIPTION
        - CustomerGridList Service

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/09          jung-gyuho          최초 생성
    """

    def __init__(self, portInImpl: CustomerCustomerGridListInPort, portOutImpl: CustomerCustomerGridListOutPort):
        self.customerIn = portInImpl
        self.customerOut = portOutImpl

    def customer_customer_grid_list_crm(self, *args, **kwargs):
        print(f"{self.__class__.__name__} customer_customer_grid_list_crm *args ==> {args[0]}")

        data = self.customerIn.customer_in_port(self, args[0])

        for arg in args:
            print(f"{self.__class__.__name__} customer_customer_grid_list_crm *args ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} customer_customer_grid_list_crm **kwargs ==> {kwarg}")

        API_HOST = getattr(settings, "CRM_HOST_IP", None)
        API_PORT = getattr(settings, "CRM_HOST_PORT", None)
        API_ADR = API_HOST + ":" + API_PORT
        print(f"Api host ==> {API_HOST}")
        result = self.customerOut.customer_out_port(self, API_ADR, "/customer/getCustomerGridList/", "POST", data,
                                                    accessToken=kwargs['accessToken'],
                                                    refreshToken=kwargs['refreshToken'])

        jtOResult = common_utils.convert_json_to_obj(result['data'])
        # print(f"{self.__class__.__name__} : analysis_trm_type_user_sales_crm get result ==> {result}")
        # print(f"{self.__class__.__name__} : analysis_trm_type_user_sales_crm get jResult ==> {jtOResult}")
        logger.info(f"{self.__class__.__name__} : analysis_trm_type_user_sales_crm get jResult ==> {jtOResult}")

        return jtOResult
