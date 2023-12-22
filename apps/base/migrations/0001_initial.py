# Generated by Django 4.2.6 on 2023-11-08 13:22

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality='100', scale=None, size=[1920, 1080], upload_to='about_image', verbose_name='Фотография')),
                ('satisfied', models.IntegerField(verbose_name='Довольные клиенты')),
                ('service', models.IntegerField(verbose_name='Наши услуги')),
                ('awards', models.IntegerField(verbose_name='Награды')),
                ('experience', models.IntegerField(verbose_name='Годы опыта')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=255, verbose_name='Категория услуги')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='Имя пользователя')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта')),
                ('phone', models.CharField(max_length=155, verbose_name='Номер телефона')),
                ('to_whom', models.CharField(max_length=255, verbose_name='Кому')),
                ('message', models.TextField(verbose_name='Введите ваше сообщение')),
            ],
            options={
                'verbose_name': 'Оставленный отзыв',
                'verbose_name_plural': 'Оставленные отзывы',
            },
        ),
        migrations.CreateModel(
            name='Faqs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=155, verbose_name='Вопрос')),
                ('answer', models.TextField(verbose_name='Ответ')),
            ],
            options={
                'verbose_name': 'Часто задаваемый вопрос',
                'verbose_name_plural': 'Часто задаваемые вопросы',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality='100', scale=None, size=[1920, 1080], upload_to='image_history', verbose_name='Фотография')),
                ('year', models.CharField(max_length=255, verbose_name='Год')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовок')),
                ('descriptions', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Наша история',
                'verbose_name_plural': 'Наша история',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='logo/', verbose_name='Логотип')),
                ('image_banner1', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality='100', scale=None, size=[1920, 1080], upload_to='banner_image', verbose_name='Фотография баннера №1')),
                ('title_1', models.CharField(max_length=255, verbose_name='Заголовок для фотографии №1')),
                ('image_banner2', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality='100', scale=None, size=[1920, 1080], upload_to='banner_image', verbose_name='Фотография баннера №2')),
                ('title_2', models.CharField(max_length=255, verbose_name='Заголовок для фотографии №2')),
                ('image_banner3', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality='100', scale=None, size=[1920, 1080], upload_to='banner_image', verbose_name='Фотография баннера №3')),
                ('title_3', models.CharField(max_length=255, verbose_name='Заголовок для фотографии №3')),
                ('phone', models.CharField(max_length=255, verbose_name='Номер телефона или ')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Почта')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('skype', models.URLField(blank=True, null=True, verbose_name='Skype')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
            ],
            options={
                'verbose_name': 'Настройки сайта',
                'verbose_name_plural': 'Настройки сайта ',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptions', models.CharField(max_length=255, verbose_name='Название услуги')),
                ('peice', models.IntegerField(verbose_name='Цена')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='base.category')),
            ],
            options={
                'verbose_name': 'Цену',
                'verbose_name_plural': 'Цены',
            },
        ),
    ]