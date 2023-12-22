# Generated by Django 4.2.6 on 2023-11-08 13:22

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название услуги')),
                ('descriptions', models.TextField(verbose_name='Описание услуги')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality='100', scale=None, size=[1920, 1080], upload_to='service_image/', verbose_name='Фотография услуги')),
            ],
            options={
                'verbose_name': 'Добавить услугу',
                'verbose_name_plural': 'Добавить услуги',
            },
        ),
    ]