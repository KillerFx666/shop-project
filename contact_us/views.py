

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView, CreateView, ListView

from site_setting.models import SiteSetting
from .forms import ContactModelForm
from .models import ContactUS, ProfileUser
from django.views import View


def store_files(file):
    with open('uploads/image.jpg', 'wb+')as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class ContactView(CreateView):
    template_name = 'contact_us/contact-us.html'
    form_class = ContactModelForm
    success_url = '/contact-us/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['site_setting'] = SiteSetting.objects.filter(is_main_setting=True).first()
        return context

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)


class CreateProfileView(CreateView):
    template_name = 'contact_us/create-profile-page.html'
    model = ProfileUser
    fields = '__all__'
    success_url = '/contact-us/create-profile'


class ProfileList(ListView):
    model = ProfileUser
    template_name = 'contact_us/profiles_view.html'
    context_object_name = 'profiles'


