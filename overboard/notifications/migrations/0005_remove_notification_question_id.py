# Generated by Django 2.0.2 on 2018-05-10 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_notification_related_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='question_id',
        ),
    ]
