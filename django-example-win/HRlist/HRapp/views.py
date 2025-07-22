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
        user_email = request.POST.get('user_email')
        user_password = request.POST.get('user_password')
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
        except User.DoesNotExist:
            res_data['error'] = "해당 이메일의 사용자가 없습니다."

        return render(request, 'login.html', res_data)

def LogoutView(request):
    request.session.flush()
    return redirect('login')

def SignupView(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        user_password = request.POST.get('user_password')
        password_check = request.POST.get('password_check')
        user_address = request.POST.get('user_address')
        user_phone = request.POST.get('user_phone')
        user_birthdate = request.POST.get('user_birthdate')
        res_data = {}

        if not all([user_name, user_email, user_password, password_check, user_address, user_phone, user_birthdate]):
            res_data['error'] = "모든 값을 입력해주세요."
        elif user_password != password_check:
            res_data['error'] = "비밀번호가 일치하지 않습니다."
        elif len(user_phone.replace('-', '')) != 11:
            res_data['error'] = "전화번호는 11자리로 입력해주세요."
        elif len(user_birthdate) != 10 or not user_birthdate.replace('-', '').isdigit():
            res_data['error'] = "생년월일은 YYYY-MM-DD 형식으로 입력해주세요."
        else:
            User.objects.create(
                user_name=user_name,
                user_email=user_email,
                user_password=make_password(user_password),
                user_address=user_address,
                user_phone=user_phone,
                user_birthdate=user_birthdate
            )
            return redirect('login')

        return render(request, 'signup.html', res_data)

def MembersView(request):
    query = request.GET.get('search', '')
    users = User.objects.filter(user_name__icontains=query) if query else User.objects.all()

    today = date.today()
    user_data = []
    for user in users:
        age = today.year - user.user_birthdate.year - ((today.month, today.day) < (user.user_birthdate.month, user.user_birthdate.day))
        user_data.append({
            'id': user.id,
            'name': user.user_name,
            'email': user.user_email,
            'age': age,
        })

    return render(request, 'members.html', {'users': user_data, 'query': query})

def MembersDetailView(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'membersdetail.html', {'user': user})

def MeView(request):
    user_id = request.session.get('user')
    if not user_id:
        return redirect('login')
    my_user = get_object_or_404(User, id=user_id)
    return render(request, 'medetail.html', {'user': my_user})

@csrf_exempt
def MeEditView(request):
    if request.method == 'POST':
        user_id = request.session.get('user')
        if not user_id:
            return JsonResponse({'message': 'no session'}, status=401)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({'message': 'user not found'}, status=404)

        user.user_name = request.POST.get('user_name')
        user.user_email = request.POST.get('user_email')
        user.user_phone = request.POST.get('user_phone')
        user.user_address = request.POST.get('user_address')
        user.save()

        return JsonResponse({
            'user_name': user.user_name,
            'user_email': user.user_email,
            'user_phone': user.user_phone,
            'user_address': user.user_address,
        })

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_profile_image(request):
    if request.method == 'POST':
        user_id = request.session.get('user')
        if not user_id:
            return JsonResponse({'message': 'no session'}, status=401)

        user = get_object_or_404(User, id=user_id)

        if 'profile_image' in request.FILES:
            user.profile_image = request.FILES['profile_image']
            user.save()
            image_url = user.profile_image.url
            return JsonResponse({'image_url': image_url})

    return JsonResponse({'message': 'Invalid request'}, status=400)
