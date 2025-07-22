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
        'user_address': user.user_address
    })

def MemberSearch(request):
    query = request.GET.get('search', '')
    if query:
        members = User.objects.filter(user_name__icontains=query)
    else:
        members = User.objects.all()
    return render(request, 'members.html', {'users': members})

def MeImageView(request):
    user_id = request.session.get('user')
    user = get_object_or_404(User, id=user_id)

    if 'profile_image' in request.FILES:
        user.profile_image = request.FILES['profile_image']
        user.save(update_fields=['profile_image', 'updated_at'])  # ✅ updated_at 갱신 강제 포함
        return JsonResponse({'image_url': user.profile_image.url})
    return JsonResponse({'error': 'No image uploaded'}, status=400)
