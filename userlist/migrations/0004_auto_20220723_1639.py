# Generated by Django 3.2.9 on 2022-07-23 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userlist', '0003_auto_20220723_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='password',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='password',
        ),
    ]