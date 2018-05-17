# Generated by Django 2.0.2 on 2018-05-11 11:21

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.query_utils


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20180510_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='content_type',
            field=models.ForeignKey(blank=True, limit_choices_to=django.db.models.query_utils.Q(django.db.models.query_utils.Q(('app_label', 'core'), ('model', 'question'), _connector='AND'), django.db.models.query_utils.Q(('app_label', 'core'), ('model', 'answer'), _connector='AND'), _connector='OR'), null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
    ]