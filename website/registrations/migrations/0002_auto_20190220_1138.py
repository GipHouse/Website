# Generated by Django 2.1.7 on 2019-02-20 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='giphouseprofile',
            name='snumber',
        ),
        migrations.AddField(
            model_name='giphouseprofile',
            name='student_number',
            field=models.CharField(max_length=8, null=True, unique=True),
        ),
    ]
