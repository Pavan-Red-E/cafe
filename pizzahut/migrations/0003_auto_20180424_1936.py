# Generated by Django 2.0.4 on 2018-04-24 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzahut', '0002_userform_message'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserForm',
            new_name='Contact',
        ),
    ]
