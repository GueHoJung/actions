import datetime

class LoginDomain:
    """
    # CLASS : LoginDomain
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/25 4:28 PM
    # DESCRIPTION
        - Login Domain TEST
        - 날짜 구하는 로직 테스트


    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/25          jung-gyuho          최초 생성
    """

    def getAllDate(self):
        currentDateTime = datetime.datetime.now().isocalendar()

        date = currentDateTime.date()
        year = date.strftime("%Y")
        print(f"Current Year -> {year}")
