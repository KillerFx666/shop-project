from django.contrib.auth import logout
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, CreateView
from django.urls import reverse
from account_module.models import User
from .forms import EditProfileModelForm, ChangePassForm


class UserPanelDashboardPage(TemplateView):
    template_name = 'user_panel_module/user_panel_dashboard_page.html'


class EditUserProfilePage(View):
    def get(self, request: HttpRequest):
        user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(instance=user)
        context = {
            'form': edit_form,
            'user': user
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)

    def post(self, request: HttpRequest):
        user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(request.POST, request.FILES, instance=user)
        if edit_form.is_valid():
            edit_form.save(commit=True)
        context = {
            'form': edit_form,
            'user': user
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)


class ChangePasswordPage(View):
    def get(self, request: HttpRequest):
        form = ChangePassForm()
        context = {
            'form': form,
        }
        return render(request, 'user_panel_module/change_password_page.html', context)

    def post(self, request: HttpRequest):
        form = ChangePassForm(request.POST)
        if form.is_valid():
            user: User = User.objects.filter(id=request.user.id).first()
            current_password = form.cleaned_data.get('current_password')
            if user.check_password(current_password):
                user.set_password(form.cleaned_data.get('password'))
                user.save()
                logout(request)
                return redirect(reverse('login-page'))
            else:
                form.add_error('password', 'کلمه عبور وارد شده اشتباه می باشد')

        context = {
            'form': form,
        }
        return render(request, 'user_panel_module/change_password_page.html', context)



def user_panel_menu_component(request: HttpRequest):
    return render(request, 'user_panel_module/components/user_panel_menu_component.html')