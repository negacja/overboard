# Generated by Django 2.0.2 on 2018-05-10 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0007_auto_20180510_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersnotification',
            name='notification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='notifications.Notification'),
        ),
    ]