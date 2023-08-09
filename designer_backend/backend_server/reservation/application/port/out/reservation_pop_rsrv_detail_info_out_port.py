from abc import ABC, abstractmethod

from ....adapter.out.reservation_pop_rsrv_detail_info_api_adapter import ReservationPopRsrvDetailInfoApiAdapter


class ReservationPopRsrvDetailInfoOutPort(ABC):
    """
    # CLASS : ReservationPopRsrvDetailInfoOutPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/09 2:04 PM
    # DESCRIPTION
        - PopRsrvDetailInfo Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/09          jung-gyuho          최초 생성
    """

    @abstractmethod
    def reservation_out_port(self, request):
        pass


class ReservationPopRsrvDetailInfoOutCrmImpl(ReservationPopRsrvDetailInfoOutPort):

    def __init__(self, reservationPopRsrvDetailInfoApiAdapter: ReservationPopRsrvDetailInfoApiAdapter):
        self.reservationPopRsrvDetailInfoApiAdapter = reservationPopRsrvDetailInfoApiAdapter

    def reservation_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} reservation_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : reservation_out_port get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : reservation_out_port get kwarg ==> {kwarg}")

        result = self.reservationPopRsrvDetailInfoApiAdapter.reservation_pop_rsrv_detail_info_crm_api(api_host=args[1],
                                                                                                      path=args[2],
                                                                                                      method=args[3],
                                                                                                      data=args[4],
                                                                                                      accessToken=
                                                                                                      kwargs[
                                                                                                          'accessToken'],
                                                                                                      refreshToken=
                                                                                                      kwargs[
                                                                                                          'refreshToken'])

        return result
