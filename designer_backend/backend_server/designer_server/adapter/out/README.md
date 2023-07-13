# Secondary Adapter/External
## Persistence/Adapter 영역
<br>

- Driven Adapter
- Driven out Port(Interface)를 implement 함
- Service에서 Port(를 implement 한 Adapter)를 호출
- 외부 Source(데이터, DB, Json 등) 와 통신 하는 Adapter(DAO, Data Access Object), Adapter의 데이터 객체를 담는 DTO(Data Transfer Object) 위치
  - userDao.dart : DAO
  - userDto.dart : Data, getter, setter
- DAO와 DTO 항상 붙어있도록 Naming