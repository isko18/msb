# Generated by Django 4.2.6 on 2023-11-08 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_contact_email_remove_contact_to_whom_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='satisfied',
        ),
        migrations.RemoveField(
            model_name='about',
            name='service',
        ),
        migrations.AddField(
            model_name='about',
            name='clients',
            field=models.IntegerField(default=1, verbose_name='Кол-во Довольные клиенты'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='level',
            field=models.IntegerField(default=1, verbose_name='Уровень удовлетворенности'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='staff',
            field=models.IntegerField(default=1, verbose_name='Кол-во опытных сотрудников'),
            preserve_default=False,
        ),
    ]
