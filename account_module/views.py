from django.contrib.auth import login, logout
from django.http import Http404, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View
from .forms import RegisterFrom, LoginForm, ForgotPasswordForm, ResetPasswordFrom
from .models import User
from utils.email_service import send_email
# Create your views here.


class RegisterView(View):
    def get(self, request):
        register_form = RegisterFrom()
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/Register.html', context)

    def post(self, request):
        register_form = RegisterFrom(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            email = register_form.cleaned_data.get('email')
            password = register_form.cleaned_data.get('password')
            user_name: bool = User.objects.filter(username__iexact=username).exists()
            user: bool = User.objects.filter(email__iexact=email).exists()
            if user:
                register_form.add_error('email', 'این ایمل از قبل ثبت شده')
                if user_name:
                    register_form.add_error('username', 'این نام کاربری از قبل ثبت شده')
            else:
                new_user = User(username=username, email=email, email_active_code=get_random_string(72))
                new_user.set_password(password)
                new_user.is_active = False
                new_user.save()
                send_email('فعال سازی حساب کابری', new_user.email, {'user': new_user}, 'emails/active_account.html')
                return redirect(reverse('login-page'))

        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/Register.html', context)


class ActivateAccount(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                # todo show: now account is active to user
                return redirect(reverse('login-page'))
            else:
                # todo show: your account was activate to user
                pass

        raise Http404


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_pass = login_form.cleaned_data.get('password')
            user_email_or_name = login_form.cleaned_data.get('email')
            if User.objects.filter(email__iexact=user_email_or_name).first():
                user: User = User.objects.filter(email__iexact=user_email_or_name).first()
            else:
                user: User = User.objects.filter(username__iexact=user_email_or_name).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما فعال نشده است')
                else:
                    is_password_correct = user.check_password(user_pass)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('home-page'))
                    else:
                        login_form.add_error('password', 'کلمه عبور اشتباه است')
            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)


class ForgetPasswordView(View):
    def get(self, request: HttpRequest):
        forget_pass_form = ForgotPasswordForm()
        context = {
            'forget_pass_form': forget_pass_form
        }
        return render(request, 'account_module/forgot_password.html', context)

    def post(self, request: HttpRequest):
        forget_pass_form = ForgotPasswordForm(request.POST)
        if forget_pass_form.is_valid():
            user_email = forget_pass_form.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                send_email('بازیابی کلمه عبور', user_email, {'user': user}, 'emails/forgot_password.html')
                return redirect(reverse('login-page'))

        context = {
            'forget_pass_form': forget_pass_form
        }
        return render(request, 'account_module/forgot_password.html', context)


class ResetPasswordView(View):
    def get(self, request: HttpRequest, active_code):
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if user is None:
            return redirect(reverse('login-page'))
        reset_pass_form = ResetPasswordFrom()
        context = {
            'reset_pass_form': reset_pass_form,
            'user': user
        }
        return render(request, 'account_module/reset_password.html', context)

    def post(self, request: HttpRequest, active_code):
        reset_pass_form = ResetPasswordFrom(request.POST)
        if reset_pass_form.is_valid():
            user: User = User.objects.filter(email_active_code__iexact=active_code).first()
            if user is None:
                return redirect(reverse('login-page'))
            new_password = reset_pass_form.cleaned_data.get('password')
            user.set_password(new_password)
            user.email_active_code = get_random_string(72)
            user.is_active = True
            user.save()
            return redirect(reverse('login-page'))


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login-page'))

