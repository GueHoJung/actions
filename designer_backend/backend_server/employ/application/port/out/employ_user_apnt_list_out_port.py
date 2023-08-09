from abc import ABC, abstractmethod

from ....adapter.out.employ_user_apnt_list_api_adapter import EmployUserApntListApiAdapter


class EmployUserApntListOutPort(ABC):
    """
    # CLASS : EmployUserApntListOutPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/09 3:39 PM
    # DESCRIPTION
        - UserApntList Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/09          jung-gyuho          최초 생성
    """

    @abstractmethod
    def employ_out_port(self, request):
        pass


class EmployUserApntListOutHrmImpl(EmployUserApntListOutPort):

    def __init__(self, employUserApntListApiAdapter: EmployUserApntListApiAdapter):
        self.employUserApntListApiAdapter = employUserApntListApiAdapter

    def employ_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} employ_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : employ_out_port get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : employ_out_port get kwarg ==> {kwarg}")

        result = self.employUserApntListApiAdapter.employ_user_apnt_list_hrm_api(api_host=args[1], path=args[2],
                                                                                 method=args[3],
                                                                                 data=args[4],
                                                                                 accessToken=kwargs['accessToken'],
                                                                                 refreshToken=kwargs['refreshToken'])

        return result
