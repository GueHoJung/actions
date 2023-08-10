import config.utils.common_utils as common_utils


class AnalysisWeeklyRetentionAnlysApiAdapter:
    """
    # CLASS : AnalysisWeeklyRetentionAnlysApiAdapter
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/08 3:45 PM
    # DESCRIPTION
        - weekly_retention_anlys
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/08          jung-gyuho          최초 생성
    """

    def analysis_weekly_retention_anlys_crm_api(self, api_host, path, method, data, *args, **kwargs):
        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : analysis_weekly_retention_anlys_crm_api get kwarg ==> {kwarg}")

        return common_utils.call_crm_api(self, self.__class__.__name__, api_host, path, method, data,
                                         accessToken=kwargs['accessToken'], refreshToken=kwargs['refreshToken'])
