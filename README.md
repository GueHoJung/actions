# Softstone Designer App
## Index
- [Softstone Designer App](#Softstone-Designer-App)
  - [Index](#index)
- [Overview](#overview)
  - [Mobile-&-CRM-중계-서버-구성](#Mobile-&-CRM-중계-서버-구성)
  - [새로운 API 중계 정책 추가 방법](#새로운-API-중계-정책-추가-방법)


# Overview
- Djangon Rest Framework Docker 구성
## Mobile & CRM 중계 서버 구성
- 프로젝트 구성 : docekr-compose
  - 아키텍처 패턴 : Hexagonal architecture 방식
  - 데이터베이스 : Mysql
  - 웹 앱 서버, 프레임워크 : nginx, gunicorn, Django, Django Rest Framework, Swagger
  - 개발 언어 : 파이썬


---

## 새로운 API 중계 정책 추가 방법

  <details>
        <summary>펼치기</summary>

    ### [신규 정책 추가 방법]
    - Hexagonal architecture 의 in/out

        진입점(web/app) - controller 
        - (interface/usecase) - service/domain - (interface/port) -
        adapter - 외부시스템, DB 등


    1. 진입점(web/app) : url 패턴 설정
        to) /ad_campaigns_app/urls.py
        ex) path("test/", views.new_policy)


    2. controller : request.method 함수 맵핑, 
        to) /ad_campaigns_app/adapter/in/web/ad_call_controller.py
        ex) @api_view(["GET"])
        def get_ad_campaigns(request, user_id):
            code ~~~
            return value


    3. (interface/usecase) : 추상화 클래스 작성, 
        to) /ad_campaigns_app/application/port/in/ad_call_usecase.py
        ex) def ad_call_policy_method(self, ad_call_infos: AdCallInfos):
                pass


    4. service/domain : 신규 정채 추가 등 핵심 로직 구현, servie = 연결, domain = 로직
                        : service는 usecase interface를 상속 받아 구현
                        : domain에 핵심 로직 구현
        to) ad_campaigns_app/application/service/ad_call_service.py
        ex) def ad_call_policy_method(self, ad_call_infos: AdCallInfos):
                code ~~~
                return value

        to) /ad_campaigns_app/domain/ad_campaigns.py
        ex) def serving_ads_by_pctr(self, ad_campaigns_list: list):
                code ~~~
                return value


    5. (interface/usecase) : 추상화 클래스 작성, 
        to) /ad_campaigns_app/application/port/out/ad_load_port.py
        ex) def ad_load(self, ad_call_info: AdCall):
                pass


    6. adapter : 데이터 베이스, Http 통신 등 외부 자원 처리
        to) /ad_campaigns_app/adapter/out/ad_load_adapter.py
        ex) def ad_load(self, ad_call):
                code ~~~
                query = ~~~ (
                    ~~~
                )
                return value


    7. 외부시스템, DB 등 : Http, db 등 연결
        to) /ad_campaigns_app/models.py 
        ex) class AdCampaigns(models.Model):
                id = models.IntegerField(primary_key=True, blank=True)
                name = models.TextField(blank=True, null=True)
                ~~~
                class Meta:
                    db_table = 'ad_campaigns'
    </details>
