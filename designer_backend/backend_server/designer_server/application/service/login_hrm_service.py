from ..port._in.login_hrm_in_port import LoginInPort


class LoginHRMService:

    def __init__(self, portImpl: LoginInPort):
        self.LoginHRM = portImpl

    def login_hrm(self, *args, **kwargs):
        print(f"LoginHRMService login_hrm *args ==> {args}")
        return self.LoginHRM.login_in(self, *args, **kwargs)
