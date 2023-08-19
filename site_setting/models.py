from django.db import models

# Create your models here.


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200, verbose_name='نام سایت')
    site_url = models.CharField(max_length=200, verbose_name='دامنه سایت')
    address = models.CharField(max_length=200, verbose_name='ادرس')
    email = models.CharField(max_length=200, null=True, blank=True, verbose_name='ایمیل')
    fax = models.CharField(max_length=200, null=True, blank=True, verbose_name='فکس')
    phone = models.CharField(max_length=300, null=True, blank=True, verbose_name='شماره تماس')
    copy_right = models.TextField(verbose_name='متن کپی رایت')
    about_us_text = models.TextField(verbose_name='متن درباره ما')
    site_logo = models.ImageField(upload_to='images/setting', verbose_name='لوگو سایت')
    is_main_setting = models.BooleanField(verbose_name='تنظیمات اصلی')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.site_name


class Slider(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    url = models.URLField(max_length=500, verbose_name='لینک اسلایدر')
    url_title = models.CharField(max_length=300, verbose_name='عنوان لینک ')
    description = models.CharField(max_length=300, null=True, verbose_name='توضیحات')
    logo = models.ImageField(upload_to='images/slider', verbose_name='تصویر اسلایدر')
    is_active = models.BooleanField(verbose_name='فعال/غیر فعال')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'

    def __str__(self):
        return self.title
