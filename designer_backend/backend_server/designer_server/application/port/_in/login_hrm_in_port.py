from abc import ABC, abstractmethod


class LoginInPort(ABC):
    @abstractmethod
    def login_in(self, request):
        pass


class LoginHRMInAPI(LoginInPort):

    def __init__(self):
        pass

    def login_in(self, request):
        print(f"LoginHRMInAPI login_in request ==> {request}")
        result = request

        return result
