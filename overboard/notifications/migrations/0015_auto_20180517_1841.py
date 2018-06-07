# Generated by Django 2.0.2 on 2018-05-17 18:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0006_auto_20180517_0735'),
        ('notifications', '0014_auto_20180517_0845'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notif_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='date received')),
                ('content', models.CharField(default='', max_length=200)),
                ('title', models.CharField(default='', max_length=200)),
                ('related_answer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.Answer')),
                ('related_question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='usernotificationnewanswer',
            name='related_question',
        ),
        migrations.RemoveField(
            model_name='usernotificationnewanswer',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserNotificationNewAnswer',
        ),
    ]