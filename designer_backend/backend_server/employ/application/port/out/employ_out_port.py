from abc import ABC, abstractmethod

from ....adapter.out.employ_api_adapter import EmployApiAdapter


class EmployOutPort(ABC):
    """
    # CLASS : EmployOutPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/28 5:45 PM
    # DESCRIPTION
        -  Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/28          jung-gyuho          최초 생성
    """

    @abstractmethod
    def employ_out_port(self, request):
        pass


class EmployOutHrmImpl(EmployOutPort):

    def __init__(self, employApiAdapter: EmployApiAdapter):
        self.employApiAdapter = employApiAdapter

    def employ_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} employ_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : employ_out_port get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : employ_out_port get kwarg ==> {kwarg}")

        result = self.employApiAdapter.employ_apnt_list_hrm_api(api_host=args[1], path=args[2],
                                                                method=args[3],
                                                                data=args[4], accessToken=kwargs['accessToken'],
                                                                refreshToken=kwargs['refreshToken'])

        return result
