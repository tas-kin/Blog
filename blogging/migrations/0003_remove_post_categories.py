# Generated by Django 2.2.6 on 2019-10-12 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0002_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
    ]
