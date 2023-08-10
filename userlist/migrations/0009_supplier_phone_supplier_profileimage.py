# Generated by Django 4.0.6 on 2022-07-28 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlist', '0008_auto_20220724_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='phone',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='profileimage',
            field=models.FileField(default=None, null=True, upload_to='profileimage/'),
        ),
    ]
