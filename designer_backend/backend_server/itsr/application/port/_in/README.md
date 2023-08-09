# Driving Port/Interface
## Usecase Interface 영역
<br>

- Driving Usecase/Port/Interface
- Service가 Driving Port를 Implement
- Controller 에서 Usecase(를 Implement 한 Service) 호
- Usecase 정의,
- 외부 Controller(사용자, API 호출 등) 와 Business Logic(Service, Domain) 느슨한 연결 고리
- Adapter(외부) 변경에 Service/Domain(내부) 영향 받지 않도록 하는 추상 클래스 
  - loginUsecase.dart : 로그인 하고자 하려는 사용자의 행위 사례 정의
    - ex/ 로그인 사용자 사례
      - 아이디 및 패스워드 입력
      - 입력 값 유효성 검증
      - 로그인 프로세스
      - 권한 부여
      - etc
- 직관적 Naming