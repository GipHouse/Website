# Generated by Django 3.0.3 on 2020-05-06 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_semester_is_archived'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semester',
            name='is_archived',
        ),
    ]
