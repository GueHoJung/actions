# Domain/Internal
## Business Logic 영역
<br>

- Business Logic/Core, Entity : 서비스가 제공하는 실질적인 서비스/기능
- 외부에 대한 의존성이 전혀 없음, 단독으로 존재하는 비지니스의 로직/가치
- Service에서 Domain 호출하여 어플리케이션에 비지니스 로직 적용
- VO(Virtual Object) 또는 Model(Entity) 구성 가능
- Business Logic(Service, Domain) 구현부
  - loginDomain.dart : 로그인과 관련된 서비스의 결과/가치 구현
- 직관적 Naming