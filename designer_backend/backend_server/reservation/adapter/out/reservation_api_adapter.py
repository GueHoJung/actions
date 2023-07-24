import config.utils.common_utils as CommonUtils

class ReservationApiAdapter:
    """
    # CLASS : ReservationApiAdapter
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/21 6:54 PM
    # DESCRIPTION
        - ReservationApiAdapter
        - 예약 API 호출

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/21          jung-gyuho          최초 생성
    """

    def reservation_crm_api(self, api_host, path, method, data):
        """
        # login_hrm_api 설명

        # PARAMS
            path : BASE URL 이하 경로
            method : POST 사용, GET, POST 등
            data : Login Json Data
        # RETURN
            return response.text
        # DESCRIPTION
            CRM SYSTEM Login API 호출
            로그인 후 권한에 맞는 정보 리턴
            토큰 발행 X
        ==================================================
        AUTHOR              DATE                NOTE
        --------------------------------------------------
        jung-gyuho              2023/07/21 2:32 PM       최초 작성
        """


        return CommonUtils.call_crm_api(self, self.__class__.__name__, api_host, path, method, data)
