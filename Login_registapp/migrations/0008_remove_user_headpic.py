# Generated by Django 2.0.6 on 2019-06-30 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login_registapp', '0007_auto_20190527_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='headpic',
        ),
    ]
