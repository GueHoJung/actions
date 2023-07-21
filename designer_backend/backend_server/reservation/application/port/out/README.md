# Driven Port/Interface
## Port Interface 영역
<br>

- Driven Port/Interface
- Out Adapter가 Driven Port를 Implement
- Service에서 Interface Port(를 Implement 한 Adapter)를 호출
- Repository 구성 가능
- Business Logic(Service, Domain) 과 외부 Source(데이터, DB, Json 등) 간에 느슨한 연결 고리
- Adapter(외부) 변경에 Service/Domain(내부) 영향 받지 않도록 하는 추상 클래스
  - loginPort.dart : 추상 클래스로 method 등 강제
- 직관적 Naming