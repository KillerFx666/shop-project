from django import template
from jalali_date import datetime2jalali, date2jalali

register = template.Library()


@register.filter(name='time_jalali')
def create_time_jalali(value):
    return datetime2jalali(value)


@register.filter(name='date_jalali')
def create_date_jalali(value):
    return date2jalali(value)
