# Generated by Django 2.0.6 on 2019-05-26 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login_registapp', '0005_user_headpic'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='Birthday',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='Salary',
            field=models.FloatField(null=True),
        ),
    ]
