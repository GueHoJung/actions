from abc import ABCMeta, abstractmethod


class LoginHRMInPort(metaclass=ABCMeta):
    @abstractmethod
    def login_hrm(self, request):
        pass
