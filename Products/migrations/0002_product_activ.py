# Generated by Django 5.1.7 on 2025-03-19 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='activ',
            field=models.BooleanField(default=True),
        ),
    ]
