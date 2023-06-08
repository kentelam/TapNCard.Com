# Generated by Django 3.2.19 on 2023-06-07 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0013_remove_postimage_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PostImage',
        ),
        migrations.AddField(
            model_name='post',
            name='background_banner',
            field=models.ImageField(default='media/images/profile/TapNCard_Default_Profile_Banner.png', upload_to='images/profile'),
        ),
        migrations.AddField(
            model_name='post',
            name='profile_picture',
            field=models.ImageField(default='media/images/profile/defaultBizman.jpg', upload_to='images/profile'),
        ),
    ]
