# Generated by Django 3.2.19 on 2023-06-07 02:48

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0002_auto_20230607_0142'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='ProfilePost',
        ),
    ]
