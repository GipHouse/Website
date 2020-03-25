# Generated by Django 3.0.3 on 2020-03-18 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20191027_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='is_archived',
            field=models.BooleanField(default=False, help_text='Setting a semester to archived will remove all GitHub teams and archive all their repositories for this semester.'),
        ),
    ]
