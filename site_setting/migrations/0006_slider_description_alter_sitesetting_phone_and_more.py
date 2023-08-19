# Generated by Django 4.2.2 on 2023-07-27 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setting', '0005_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='description',
            field=models.CharField(max_length=300, null=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='phone',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='شماره تماس'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='url',
            field=models.URLField(max_length=500, verbose_name='لینک اسلایدر'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='url_title',
            field=models.CharField(max_length=300, verbose_name='عنوان لینک '),
        ),
    ]