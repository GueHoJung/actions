from abc import ABC, abstractmethod


class LoginInPort(ABC):
    @abstractmethod
    def login_in_port(self, request):
        pass


class LoginInHrmAPI(LoginInPort):

    def __init__(self):
        pass

    def login_in_port(self, *args, **kwargs):
        print(f"LoginHRMInAPI login_in request ==> {args[0]}")
        result = args[0]

        return result


class LoginInCrmAPI(LoginInPort):

    def __init__(self):
        pass

    def login_in_port(self, *args, **kwargs):
        print(f"LoginCrmInAPI login_in request ==> {args[0]}")
        result = args[0]

        return result
