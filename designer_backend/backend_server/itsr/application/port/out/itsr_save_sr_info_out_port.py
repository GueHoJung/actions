from abc import ABC, abstractmethod

from ....adapter.out.itsr_save_sr_info_api_adapter import ItsrSaveSrInfoApiAdapter


class ItsrSaveSrInfoOutPort(ABC):
    """
    # CLASS : ItsrSaveSrInfoOutPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/09 2:43 PM
    # DESCRIPTION
        - SaveSrInfo Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/09          jung-gyuho          최초 생성
    """

    @abstractmethod
    def itsr_out_port(self, request):
        pass


class ItsrSaveSrInfoOutCrmImpl(ItsrSaveSrInfoOutPort):

    def __init__(self, itsrSaveSrInfoApiAdapter: ItsrSaveSrInfoApiAdapter):
        self.itsrSaveSrInfoApiAdapter = itsrSaveSrInfoApiAdapter

    def itsr_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} itsr_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : itsr_out_port get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : itsr_out_port get kwarg ==> {kwarg}")

        result = self.itsrSaveSrInfoApiAdapter.itsr_save_sr_info_crm_api(api_host=args[1], path=args[2],
                                                                         method=args[3],
                                                                         data=args[4],
                                                                         accessToken=kwargs['accessToken'],
                                                                         refreshToken=kwargs['refreshToken'])

        return result
