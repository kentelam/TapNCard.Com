# Generated by Django 3.2.19 on 2023-06-08 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0014_auto_20230607_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='background_banner',
            field=models.ImageField(blank=True, default='media/images/profile/TapNCard_Default_Profile_Banner.png', upload_to='images/profile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='profile_picture',
            field=models.ImageField(blank=True, default='media/images/profile/defaultBizman.jpg', upload_to='images/profile'),
        ),
    ]
