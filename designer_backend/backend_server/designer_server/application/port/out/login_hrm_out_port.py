from abc import ABCMeta, abstractmethod


class LoginHRMOutPort(metaclass=ABCMeta):
    @abstractmethod
    def login_hrm_api(self, path, method):
        pass
