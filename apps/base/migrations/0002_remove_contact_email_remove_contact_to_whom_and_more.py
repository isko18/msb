# Generated by Django 4.2.6 on 2023-11-08 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='to_whom',
        ),
        migrations.AddField(
            model_name='contact',
            name='cause',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Причина'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(blank=True, null=True, verbose_name='Сообщение'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Имя пользователя'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=155, null=True, verbose_name='Почта'),
        ),
    ]