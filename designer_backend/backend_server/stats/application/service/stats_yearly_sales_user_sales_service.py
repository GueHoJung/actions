from ..port._in.stats_yearly_sales_user_sales_in_port import StatsYearlySalesUserSalesInPort
from ..port.out.stats_yearly_sales_user_sales_out_port import StatsYearlySalesUserSalesOutPort
import config.utils.common_utils as common_utils
from django.conf import settings


class StatsYearlySalesUserSalesService:
    """
    # CLASS : StatsYearlySalesUserSalesService
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/31 6:22 PM
    # DESCRIPTION
        - YearlySalesUserSales Service

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/31          jung-gyuho          최초 생성
    """

    def __init__(self, portInImpl: StatsYearlySalesUserSalesInPort, portOutImpl: StatsYearlySalesUserSalesOutPort):
        self.statsIn = portInImpl
        self.statsOut = portOutImpl

    def stats_yearly_sales_user_sales_crm(self, *args, **kwargs):
        print(f"{self.__class__.__name__} stats_yearly_sales_user_sales_crm *args ==> {args[0]}")

        data = self.statsIn.stats_in_port(self, args[0])

        for arg in args:
            print(f"{self.__class__.__name__} stats_yearly_sales_user_sales_crm *args ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} stats_yearly_sales_user_sales_crm **kwargs ==> {kwarg}")

        API_HOST = getattr(settings, "CRM_HOST_IP", None)
        API_PORT = getattr(settings, "CRM_HOST_PORT", None)
        API_ADR = API_HOST + ":" + API_PORT
        print(f"Api host ==> {API_HOST}")
        result = self.statsOut.stats_out_port(self, API_ADR, "/stats/getYearlySalesUserSales/", "POST", data,
                                              accessToken=kwargs['accessToken'],
                                              refreshToken=kwargs['refreshToken'])

        jtOResult = common_utils.convert_json_to_obj(result['data'])
        print(f"{self.__class__.__name__} : stats_yearly_sales_user_sales_crm get result ==> {result}")
        print(f"{self.__class__.__name__} : stats_yearly_sales_user_sales_crm get jResult ==> {jtOResult}")

        return jtOResult
