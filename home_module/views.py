from django.shortcuts import render
from django.views.generic.base import TemplateView

from account_module.models import User
from site_setting.models import SiteSetting, Slider


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slider'] = Slider.objects.filter(is_active=True)
        return context


class AboutView(TemplateView):
    template_name = 'home_module/about_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_setting'] = SiteSetting.objects.filter(is_main_setting=True).first()
        return context


def site_footer_component(request):
    site_setting = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_setting': site_setting
    }
    return render(request, 'shared/site_footer_component.html', context)


def site_header_component(request):
    site_setting = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_setting': site_setting
    }
    return render(request, 'shared/site_header_component.html', context)


