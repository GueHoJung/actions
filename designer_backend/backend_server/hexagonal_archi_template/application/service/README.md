# Service/Internal
## Orchestration 영역
<br>

- Service Orchestration
- 내부 비지니스 로직(Domain)과 외부 자원(Controller, Data Source 등) 연계
- In Port/Usecase 를 Implement
- In Adapter 에서 Interface Usecase/Port(를 Implement 한 Service)를 호출
- 비지니스 로직이 필요 없는 경우 Domain 거치지 않고 데이터 연계 가능
- Business Logic(Domain) 의 외부 Source(데이터, DB, Json 등) 에 대한 의존성 차단
- Adapter(외부) 변경에 Domain(내부) 영향 받지 않도록 Orchestration(연계 조정) 기능
  - loginService.dart : 비지니스 로직이 서비스에 반영 되는 실 구현부
- 직관적 Naming