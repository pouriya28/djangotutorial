# Generated by Django 5.1.7 on 2025-03-20 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=50, verbose_name='نام')),
                ('url', models.URLField(blank=True, max_length=500, null=True, verbose_name='آدرس وب\u200cسایت')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Home/', verbose_name='عکس')),
            ],
        ),
    ]
