
---

## 쟝고를 활용한 미니프로젝트

---

# 인력사무소

중장년층 및 고령층 구직자들이 손쉽게 일자리를 찾고, 
인력사무소 운영자는 인력관리와 이들의 경력을 살려 채용할 수 있도록 연결해주는 인력 매칭 서비스입니다.

#### 👷 멤버 구성
---

- **박석번**
  - DB 구성
  - HTML 제작: `login.html`, `Members.html`, `Medetail.html`, `home.html`, `membersdetail.html`, `signup.html`
  - Django 구성, AJAX 구성
  - PPT 제작, 스토리보드 제작

- **장태영**
  - DB 구성
  - HTML 제작: `login.html`, `Members.html`, `Medetail.html`, `home.html`, `membersdetail.html`, `signup.html`
  - Django 구성, AJAX 구성
  - PPT 제작, 스토리보드 제작

- **전범하**
  - DB 구성
  - HTML 제작: `login.html`, `Members.html`, `Medetail.html`, `home.html`, `membersdetail.html`, `signup.html`
  - Django 구성, AJAX 구성
  - PPT 제작, 스토리보드 제작


## 🛠 개발환경

### 💻 Frontend
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=flat&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)

### ⚙️ Backend
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)

### 🗃 Database
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)](https://www.sqlite.org/)

### 🧰 Tool
[![VS Code](https://img.shields.io/badge/VSCode-007ACC?style=flat&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
[![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)](https://git-scm.com/)

### 📦 Others
[![AJAX](https://img.shields.io/badge/AJAX-005571?style=flat)]()
[![jQuery](https://img.shields.io/badge/jQuery-0769AD?style=flat&logo=jquery&logoColor=white)](https://jquery.com/)

## 프로젝트 구조(디렉터리 트리)
```
📂 inn_ryeock/
┣ 📂 HRapp/
┃ ┣ 📜 models.py
┃ ┣ 📜 views.py
┃ ┣ 📜 urls.py
┃ ┗ 📂 templates/
┃ ┣ 📜 home.html
┃ ┣ 📜 login.html
┃ ┣ 📜 signup.html
┃ ┣ 📜 medetail.html
┃ ┗ 📜 membersdetail.html
┣ 📜 manage.py
```

## 💻 코드 예시

<details>
<summary>🔽 views.py 코드 보기</summary>

```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
</details>
```
[위로 가기](#-💻-코드-예시)



