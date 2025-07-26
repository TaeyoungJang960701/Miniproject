from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import date
from django.contrib import messages
from datetime import datetime


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

def format_phone_number(phone):
    # '01011112222' -> '010-1111-2222'
    return f"{phone[:3]}-{phone[3:7]}-{phone[7:]}"


def SignupView(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    
    elif request.method == 'POST':
        user_name = request.POST.get('user_name', '')
        user_email = request.POST.get('user_email', '')
        user_password = request.POST.get('user_password', '')
        password_check = request.POST.get('password_check', '')
        user_address = request.POST.get('user_address', '')
        user_phone = request.POST.get('user_phone', '')
        user_birthdate = request.POST.get('user_birthdate', '').strip()

        # 생년월일 자동 포맷
        if len(user_birthdate) == 8 and user_birthdate.isdigit():
            user_birthdate = f"{user_birthdate[:4]}-{user_birthdate[4:6]}-{user_birthdate[6:]}"

        error = None        

        if not (user_name and user_password and password_check and user_address and user_phone and user_birthdate and user_email):
            error = "모든 값을 입력해주세요."
        elif User.objects.filter(user_email=user_email).exists():
            error = "이미 존재하는 이메일 입니다."
        elif user_password != password_check:
            error = "비밀번호가 일치하지 않습니다."
        elif len(user_phone) != 11 or not user_phone.isdigit():
            error = "전화번호는 11자리 숫자로 입력해주세요."
        else:
            try:
                datetime.strptime(user_birthdate, '%Y-%m-%d')
            except ValueError:
                error = "생년월일은 유효한 날짜여야 합니다."

        if error:
            context = {
                'error': error,
                'user_name': user_name,
                'user_email': user_email,
                'user_address': user_address,
                'user_phone': user_phone,
                'user_birthdate': user_birthdate
            }
            return render(request, 'signup.html', context)

        # 회원 생성
        formatted_phone = format_phone_number(user_phone)
        user = User(
            user_name=user_name,
            user_email=user_email,
            user_password=make_password(user_password),
            user_address=user_address,
            user_phone=formatted_phone,
            user_birthdate=user_birthdate
        )
        user.save()        
        
        return redirect('/login/')



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
    
def intro(request):
    return render(request, 'intro.html')

def members(request):
    users = User.objects.all()  # 또는 원하는 queryset
    return render(request, 'members.html', {'users': users})

def minigame(request):
    return render(request, 'minigame.html')


def minesweeperView(request):
    return render(request, 'minesweeper.html')
