
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

## 💻 BACK 코드 예시

<details>
<summary>🔽 views.py 코드 보기</summary>

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import date

def HomeView(request):
    return render(request, 'home.html')

def LoginView(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        user_email = request.POST.get('user_email', None)
        user_password = request.POST.get('user_password', None)
        
        res_data = {}
        
        if not (user_email and user_password):
            res_data['error'] = "이메일과 비밀번호를 입력해주세요."
            return render(request, 'login.html', res_data)
        
        try:
            user = User.objects.get(user_email=user_email)
            if check_password(user_password, user.user_password):
                request.session['user'] = user.id
                return redirect('members') 
            else:
                res_data['error'] = "비밀번호가 일치하지 않습니다."
                return render(request, 'login.html', res_data)
        except User.DoesNotExist:
            res_data['error'] = "해당 이메일의 사용자가 없습니다."
            return render(request, 'login.html', res_data)

def LogoutView(request):
    request.session.flush()
    return redirect('login.html')

def SignupView(request):
    if request.method =='GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        user_name = request.POST.get('user_name', None)
        user_email = request.POST.get('user_email', None)
        user_password = request.POST.get('user_password', None)
        password_check = request.POST.get('password_check', None)
        user_address = request.POST.get('user_address', None)
        user_phone = request.POST.get('user_phone', None)
        user_birthdate = request.POST.get('user_birthdate', None)
        
        res_data = {}
        
        if not(user_name and user_password and password_check and user_address and user_phone and user_birthdate and user_email):
            res_data['error'] = "모든 값을 입력해주세요."
            return render(request, 'signup.html', res_data)
        elif user_password != password_check:
            res_data['error'] = "비밀번호가 일치하지 않습니다."
            return render(request, 'signup.html', res_data)
        elif len(user_phone) != 11:
            res_data['error'] = "전화번호는 11자리로 입력해주세요."
            return render(request, 'signup.html', res_data)
        elif len(user_birthdate) != 10 or not user_birthdate.replace('-', '').isdigit():
            res_data['error'] = "생년월일은 YYYY-MM-DD 형식으로 입력해주세요."
            return render(request, 'signup.html', res_data)
        else:
            user= User(
                user_name=user_name,
                user_email=user_email,
                user_password=make_password(user_password),
                user_address=user_address,
                user_phone=user_phone,
                user_birthdate=user_birthdate
            )
            
            user.save()
            # res_data['success'] = "회원가입이 완료되었습니다."
        
        # return render(request, 'signup.html', res_data)
        return redirect('login')


def MembersView(request):
    query = request.GET.get('search', '')
    if query:
        users = User.objects.filter(user_name__icontains=query)
    else:
        users = User.objects.all()
    if not users:
        return render(request, 'members.html', {'error': '등록된 회원이 없습니다.'}) 
    today = date.today()
    user_data = []
    for user in users:
        birthdate = user.user_birthdate
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        user_data.append({
            'id': user.id,
            'name': user.user_name,
            'email': user.user_email,
            'age': age,
        })

    return render(request, 'members.html', {'users': user_data})


def MembersDetailView(request, user_id):
    user = get_object_or_404(User, id=user_id) 
    return render(request, 'membersdetail.html', {'user': user})

def MeView(request):
    user_id = request.session.get('user')
    my_user = User.objects.get(id=user_id)
    my_user.refresh_from_db()

    return render(request, 'medetail.html', {'user': my_user})

@csrf_exempt   
def MeEditView(request):
    user_id = request.session.get('user')
    user = get_object_or_404(User, id=user_id)

    new_email = request.POST.get('user_email')

    # 다른 유저가 이 이메일을 쓰고 있는지 확인
    if User.objects.filter(user_email=new_email).exclude(id=user.id).exists():
        return JsonResponse({'error': '이미 사용 중인 이메일입니다.'}, status=400)

    user.user_name = request.POST.get('user_name')
    user.user_email = new_email
    user.user_phone = request.POST.get('user_phone')
    user.user_address = request.POST.get('user_address')
    user.save()

    return JsonResponse({
        'user_name': user.user_name,
        'user_email': user.user_email,
        'user_phone': user.user_phone,
        'user_address': user.user_address,
    })

def MeImageView(request):
    user_id = request.session.get('user')
    user = get_object_or_404(User, id=user_id)

    if 'profile_image' in request.FILES:
        user.profile_image = request.FILES['profile_image']
        user.save(update_fields=['profile_image', 'updated_at'])
        return JsonResponse({'image_url': user.profile_image.url})
    return JsonResponse({'error': 'No image uploaded'}, status=400)
```
</details>

<details>
<summary>🔽 models.py 코드 보기</summary>
  
```python

 from django.db import models

class User(models.Model):
    
    user_email = models.EmailField(unique=True) # 이메일을 받는데 이게 ID임
    user_password = models.CharField(max_length=128)  # 암호화된 비밀번호 저장
    user_name = models.CharField(max_length=50) 
    user_birthdate = models.DateField()
    user_phone = models.CharField(max_length=20)
    user_address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(
    upload_to='profile_images/',
    default='profile_images/default.png',
    blank=True
)
    
    class Meta:
        db_table = 'user'
        verbose_name = 'User'

    def __str__(self):
        return self.user_name
  ```
</details>
<details>
<summary>🔽 urls.py 코드 보기</summary>
  
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView , name='home'),
    path('login/', views.LoginView , name='login'),
    path('signup/', views.SignupView , name='signup'),
    path('members/', views.MembersView, name='members'),  
    path('members/<int:user_id>/', views.MembersDetailView, name='member_detail'),
    path('members/me', views.MeView, name='me_detail'),
    path('logout/', views.LogoutView, name='logout'),
    path('members/me/edit/', views.MeEditView, name='me_edit'),
    path('members/me/edit/image', views.MeImageView, name='me_edit_image'),
]
```
</details>

## 💻 FRONT 코드 예시

<details>
  <summary>🔽 home.html 코드 보기</summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-LN+7fdVzj6u52u30Kp6M/trliBMCMKTyK833zpbD+pXdCLuTusPj697FH4R/5mcr" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/js/bootstrap.bundle.min.js" integrity="sha384-ndDqU0Gzau9qJ1lfW4pNLlhNTkCfHzAVBReH9diLvGRem5+R9g2FzA8ZGN954O5Q" crossorigin="anonymous"></script>
    <title>HOME</title>
</head>
<body>
    <div class="d-flex justify-content-center align-items-center vh-100">
        <div class="text-center">
            <div class="mt-4">
                <a href="{% url 'login' %}" class="btn btn-primary"><h1>인력사무소</h1></a>
            </div>
            <div class="mt-4">
                <p>인력사무소에 오신 것을 환영합니다. 회원 가입 후 로그인하여 서비스를 이용하세요.</p>
            </div>
        </div>
    </div>
</body>
</html>
</details>
```

<details>
  <summary>🔽 login.html 코드 보기</summary>
  
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://getbootstrap.com/docs/5.3/assets/css/docs.css" rel="stylesheet">
    <title>로그인</title>
    <script defer src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/js/bootstrap.bundle.min.js"></script>
  </head>
 <body class="d-flex align-items-center justify-content-center vh-100">

  <div class="container" style="max-width: 400px;">
    <h2 class="text-center mb-3">로그인</h2>

    <form method="POST">
      {% csrf_token %}
      <h6 class="text-center mb-3">
        {% if error %}
          <span class="text-danger">{{ error }}</span>
        {% else %}
          로그인하세요
        {% endif %}        
        </h6>      
      <div class="mb-3">
        <label for="user_email" class="form-label">Email</label>
        <input type="email" class="form-control" id="user_email" name="user_email" required>
      </div>

      <div class="mb-3">
        <label for="user_password" class="form-label">비밀번호</label>
        <input type="password" class="form-control" id="user_password" name="user_password" required>
      </div>  

      <div class="d-grid">
        <button type="submit" class="btn btn-primary">로그인</button>
      </div>
      <div>
        <h6 class="text-center mb-3">
          <a href="{% url 'signup' %}">회원가입</a>        
        </h6>
      </div>
    </form>
  </div>

</body>
</html>
</details>
```

<details>
  <summary>🔽 medetail.html 코드 보기</summary>
  
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>내 정보 조회</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

    <style>
    .profile-image {
      width: 150px;
      height: 150px;
      object-fit: cover;
    }
    </style>
</head>
<body>
  <section style="background-color: #eee;">
  <div class="container py-4">

    <!-- 뒤로가기 -->
    <div class="row justify-content-center">
      <div class="col-md-6">
        <nav class="bg-light rounded-3 p-3 mb-4">
          <ol class="breadcrumb mb-0">
            <li class="breadcrumb-item"><a href="{% url 'members' %}">뒤로가기</a></li>
            <li class="breadcrumb-item active" aria-current="page">{{ user.user_name }}</li>
          </ol>
        </nav>
      </div>
    </div>

    <!-- 프로필 카드 -->
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="card mb-4 text-center">
          <div class="card-body">
            <!-- 프로필 이미지 -->
            {% if user.profile_image %}
              <img src="{{ user.profile_image.url }}?{{ user.updated_at.timestamp }}"
                  alt="avatar" class="rounded-circle profile-image mb-3" id="profileImage">
            {% else %}
              <img src="{{ MEDIA_URL }}profile_images/default.png"
                  alt="avatar" class="rounded-circle profile-image mb-3" id="profileImage">
            {% endif %}



            <!-- 이미지 업로드 폼 -->
            <form id="imageUploadForm" enctype="multipart/form-data" style="display: none;">
              <input type="file" name="profile_image" id="profileImageInput" class="form-control mb-2" accept="image/*">
              <button type="submit" class="btn btn-success btn-sm">이미지 변경</button>
            </form>

            <!-- 편집 버튼 -->
            <div class="d-flex justify-content-center mt-2">
              <button type="button" class="btn btn-outline-primary" onclick="editRow(this)">편집</button>
            </div>
          </div>
        </div>

        <!-- 사용자 정보 -->
        <div class="card">
          <div class="card-body">
            <div class="row mb-3">
              <div class="col-sm-3"><strong>Name</strong></div>
              <div class="col-sm-9" id="fullName">{{ user.user_name }}</div>
            </div>
            <div class="row mb-3">
              <div class="col-sm-3"><strong>Email</strong></div>
              <div class="col-sm-9" id="Email">{{ user.user_email }}</div>
            </div>
            <div class="row mb-3">
              <div class="col-sm-3"><strong>Phone</strong></div>
              <div class="col-sm-9" id="Phone">{{ user.user_phone }}</div>
            </div>
            <div class="row mb-3">
              <div class="col-sm-3"><strong>Address</strong></div>
              <div class="col-sm-9" id="Address">{{ user.user_address }}</div>
            </div>
          </div>
        </div>

        <!-- CSRF -->
        <input type="hidden" id="csrf_token" value="{{ csrf_token }}">
      </div>
    </div>
  </div>
</section>

<!-- jQuery -->
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

<!-- AJAX 스크립트 -->
<script>
  let isEditing = false;

  function editRow(btn) {
    const nameEl = document.getElementById('fullName');
    const emailEl = document.getElementById('Email');
    const phoneEl = document.getElementById('Phone');
    const addressEl = document.getElementById('Address');
    const uploadForm = document.getElementById('imageUploadForm');

    if (!isEditing) {
      nameEl.innerHTML = `<input type="text" id="nameInput" class="form-control" value="${nameEl.textContent.trim()}">`;
      emailEl.innerHTML = `<input type="email" id="emailInput" class="form-control" value="${emailEl.textContent.trim()}">`;
      phoneEl.innerHTML = `<input type="text" id="phoneInput" class="form-control" value="${phoneEl.textContent.trim()}">`;
      addressEl.innerHTML = `<input type="text" id="addressInput" class="form-control" value="${addressEl.textContent.trim()}">`;

      btn.textContent = '저장';
      uploadForm.style.display = 'block';  // 이미지 폼 표시
      isEditing = true;
    } else {
      const data = {
        user_name: document.getElementById('nameInput').value,
        user_email: document.getElementById('emailInput').value,
        user_phone: document.getElementById('phoneInput').value,
        user_address: document.getElementById('addressInput').value,
        csrfmiddlewaretoken: document.getElementById('csrf_token').value
      };

      $.ajax({
        url: "{% url 'me_edit' %}",
        method: "POST",
        data: data,
        success: function (response) {
          nameEl.textContent = response.user_name;
          emailEl.textContent = response.user_email;
          phoneEl.textContent = response.user_phone;
          addressEl.textContent = response.user_address;
          btn.textContent = '편집';
          uploadForm.style.display = 'none'; // 폼 숨김
          isEditing = false;
          alert("수정 완료");
        },
        error: function (xhr) {
          alert("오류: " + xhr.responseText);
        }
      });
    }
  }

  // 이미지 업로드 AJAX
  $(document).ready(function () {
    $('#imageUploadForm').on('submit', function (e) {
      e.preventDefault();
      const formData = new FormData(this);
      formData.append('csrfmiddlewaretoken', $('#csrf_token').val());

      $.ajax({
        url: "{% url 'me_edit_image' %}",
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,
        success: function (data) {
          $('#profileImage').attr('src', data.image_url);
          alert("이미지 변경 완료");
        },
        error: function (xhr) {
          alert("업로드 실패: " + xhr.responseText);
        }
      });
    });
  });
</script>
</body>
</html>
```
</details>

