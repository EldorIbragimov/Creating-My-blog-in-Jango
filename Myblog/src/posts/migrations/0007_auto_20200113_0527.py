# Generated by Django 3.0.2 on 2020-01-13 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_postview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment_count',
        ),
        migrations.RemoveField(
            model_name='post',
            name='view_count',
        ),
    ]