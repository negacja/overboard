# Generated by Django 2.0.2 on 2018-05-10 23:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20180510_2104'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notifications', '0009_auto_20180510_2148'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserNotificationAnsweredQuestion',
            new_name='UserNotificationNewAnswer',
        ),
    ]