# Generated by Django 2.2.1 on 2019-06-07 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='img',
            new_name='image',
        ),
    ]
