# Generated by Django 2.0.2 on 2018-03-04 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('overboardapp', '0002_auto_20180304_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(default='', max_length=600)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='answer',
            name='content',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='id',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='score',
        ),
        migrations.RemoveField(
            model_name='question',
            name='content',
        ),
        migrations.RemoveField(
            model_name='question',
            name='id',
        ),
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='question',
            name='score',
        ),
        migrations.AddField(
            model_name='answer',
            name='related_question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='overboardapp.Question'),
        ),
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vote',
            name='voter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='overboardapp.User'),
        ),
        migrations.AddField(
            model_name='answer',
            name='post_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='overboardapp.Post'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='post_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='overboardapp.Post'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vote',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='overboardapp.Post'),
        ),
    ]
