# Generated by Django 2.2 on 2019-04-14 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0002_auto_20190308_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giphouseprofile',
            name='github_username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]