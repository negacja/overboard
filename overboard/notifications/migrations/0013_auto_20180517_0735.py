# Generated by Django 2.0.2 on 2018-05-17 07:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0012_remove_usersnotification_related_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernotificationnewanswer',
            name='notif_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date received'),
        ),
    ]