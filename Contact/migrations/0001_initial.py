# Generated by Django 5.1.7 on 2025-03-21 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام شما')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('phone_number', models.CharField(max_length=12, verbose_name='شماره تلفن')),
                ('description', models.TextField(verbose_name='پیام شما')),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
