# Generated by Django 3.0.2 on 2020-01-08 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_featured'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='profile_pictur',
            new_name='profile_picture',
        ),
    ]
