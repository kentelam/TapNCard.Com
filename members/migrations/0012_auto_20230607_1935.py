# Generated by Django 3.2.19 on 2023-06-07 19:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0011_auto_20230607_1917'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProfileImage',
            new_name='PostImage',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
