from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'تم تسجيل الدخول بنجاح')
            return redirect('home')  # تأكد أن 'home' معرف في urls
        else:
            messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة')

    return render(request, 'accounts/login.html')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'اسم المستخدم مستخدم بالفعل')
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            messages.success(request, 'تم إنشاء الحساب وتسجيل الدخول')
            return redirect('home')

    return render(request, 'accounts/signup.html')
   