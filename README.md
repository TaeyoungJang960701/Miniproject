프로젝트소개(스토리보드)
● 중장년층 및 고령층 구직자들이 손쉽게 일자리를 찾고, 
  인력사무소 운영자는 인력관리와 이들의 경력을 살려 채용할 수 있도록 연결해주는 인력 매칭 서비스입니다.


프로젝트 구조(디렉터리 트리)
📂inn_ryeock
 ┣ 📂HRapp
 ┃ ┣ 📜models.py
 ┃ ┣ 📜views.py
 ┃ ┣ 📜urls.py
 ┃ ┗ 📂templates/
 ┃    ┣ 📜home.html
 ┃    ┣ 📜login.html
 ┃    ┣ 📜signup.html
 ┃    ┣ 📜medetail.html
 ┃    ┗ 📜membersdetail.html
 ┣ 📜manage.py


개발기간
● 25.07.14 - 25.07.25


멤버구성(선택형)
● 박선번: DB구성, login.html제작, Members.html제작, Medetail.html제작, home.html제작, membersdetail.html제작, signup.html제작
, PPT제작, django 구성, ajax구성, 스토리보드제작
● 정태영: DB구성, login.html제작, Members.html제작, Medetail.html제작, home.html제작, membersdetail.html제작, signup.html제작
, PPT제작, django 구성, ajax구성, 스토리보드제작
● 전범하: DB구성, login.html제작, Members.html제작, Medetail.html제작, home.html제작, membersdetail.html제작, signup.html제작
, PPT제작, django 구성, ajax구성, 스토리보드제작


개발환경
● Frontend: HTML, CSS, JavaScript, Bootstrap
● Backend: Python 3.12.10, Django 5.2.4
● Database: SQLite3
● Tool: Visual Studio Code, Git
● Others: AJAX, jQuery


주요기능
홈 화면(home.html)
● 로그인으로 들어가기전 화면 
● 어떠한 내용인지를 간략하게 소개하는 화면


회원가입(signup.html)
● ID 중복 체크
● 개인정보(이름,생년월일,주소...)를 기입하여 DB에 저장


로그인(login.html)
● 입력한 내용과 회원가입에 저장된 DB내용이 일치하는지를 확인하는 화면
● 로그인 불일치 이메일 또는 비밀번호의 오류에 대해서 알림기능
● 아이디가 없을 시 화면 하단의 회원가입버튼을 통해 회원가입 가능


User의 상세정보(Medetail.html)
● User정보페이지
● DB에 저장된 로그인 한 인원의 개인정보(이름,생년월일,주소...)를 출력
● DB에 저장된 기본이미지가 출력되며 C드라이버를 통해 이미지 변환이 가능
● 편집기능으로 개인정보수정가능
● 뒤로 가기 버튼을 통해 인원정보페이지로 화면이동


인원정보페이지(Members.html)
● 등록된 인원들을 확인하는 화면
● 상세정보를 통해 인원들의 상세정보(이름,나이,주소,전화번호)를 확인가능
● 로그아웃 버튼을 누르면 로그인 화면으로 화면이동
● 내 정보조회를통해 user의 정보를 확인가능
● 검색란에 이름을 입력하여 인원 검색가능


인원상세정보(membersdetail.html)
● DB에 저장된 기본이미지가 출력
● 뒤로 가기 버튼을 통해 인원정보페이지로 화면이동
● DB에 저장된 인원의 상세정보(이름,나이,주소,전화번호)를 출력

