from ..port._in.order_prepaid_history_list_in_port import OrderPrepaidHistoryListInCrmImpl
from ..port.out.order_prepaid_history_list_out_port import OrderPrepaidHistoryListOutCrmImpl
import config.utils.common_utils as common_utils
from django.conf import settings


class OrderPrepaidHistoryListService:
    """
    # CLASS : OrderPrepaidHistoryListService
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/28 8:58 PM
    # DESCRIPTION
        - 분석 관련 Service

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/28          jung-gyuho          최초 생성
    """

    def __init__(self, portInImpl: OrderPrepaidHistoryListInCrmImpl, portOutImpl: OrderPrepaidHistoryListOutCrmImpl):
        self.orderIn = portInImpl
        self.orderOut = portOutImpl

    def order_prepaid_history_list_crm(self, *args, **kwargs):
        print(f"{self.__class__.__name__} order_prepaid_history_list_crm *args ==> {args[0]}")

        data = self.orderIn.order_in_port(self, args[0])

        for arg in args:
            print(f"{self.__class__.__name__} order_prepaid_history_list_crm *args ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} order_prepaid_history_list_crm **kwargs ==> {kwarg}")

        API_HOST = getattr(settings, "CRM_HOST_IP", None)
        API_PORT = getattr(settings, "CRM_HOST_PORT", None)
        API_ADR = API_HOST + ":" + API_PORT
        print(f"Api host ==> {API_HOST}")
        result = self.orderOut.order_out_port(self, API_ADR, "/order/getPrpHisGridList/", "POST", data,
                                              accessToken=kwargs['accessToken'],
                                              refreshToken=kwargs['refreshToken'])

        jtOResult = common_utils.convert_json_to_obj(result['data'])
        print(f"{self.__class__.__name__} : order_prepaid_history_list_crm get result ==> {result}")
        print(f"{self.__class__.__name__} : order_prepaid_history_list_crm get jResult ==> {jtOResult}")

        return jtOResult
