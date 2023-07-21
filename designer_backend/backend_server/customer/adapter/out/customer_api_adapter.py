import config.utils.common_utils as CommonUtils


class CustomerApiAdapter:
    """
    # CLASS : CustomerApiAdapter
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/21 10:06 PM
    # DESCRIPTION
        - 고객 관련 API Adapter
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/21          jung-gyuho          최초 생성
    """

    def customer_info_crm_api(self, path, method, data):
        return CommonUtils.call_crm_api(self, self.__class__.__name__, path, method, data)
