from abc import ABC, abstractmethod

from ....adapter.out.itsr_sr_grid_list_api_adapter import ItsrSrGridListApiAdapter


class ItsrSrGridListOutPort(ABC):
    """
    # CLASS : ItsrSrGridListOutPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/09 2:55 PM
    # DESCRIPTION
        - SrGridList Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/09          jung-gyuho          최초 생성
    """

    @abstractmethod
    def itsr_out_port(self, request):
        pass


class ItsrSrGridListOutCrmImpl(ItsrSrGridListOutPort):

    def __init__(self, itsrSrGridListApiAdapter: ItsrSrGridListApiAdapter):
        self.itsrSrGridListApiAdapter = itsrSrGridListApiAdapter

    def itsr_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} itsr_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : itsr_out_port get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : itsr_out_port get kwarg ==> {kwarg}")

        result = self.itsrSrGridListApiAdapter.itsr_sr_grid_list_crm_api(api_host=args[1], path=args[2],
                                                                         method=args[3],
                                                                         data=args[4],
                                                                         accessToken=kwargs['accessToken'],
                                                                         refreshToken=kwargs['refreshToken'])

        return result
