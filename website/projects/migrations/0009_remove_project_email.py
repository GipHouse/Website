# Generated by Django 3.0.3 on 2020-03-25 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20200325_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='email',
        ),
    ]
