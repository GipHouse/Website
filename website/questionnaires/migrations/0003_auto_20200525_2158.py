# Generated by Django 3.0.6 on 2020-05-25 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaires', '0002_auto_20191026_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='optional',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='agreementanswerdata',
            name='value',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neutral'), (4, 'Agree'), (5, 'Strongly Agree')], null=True),
        ),
        migrations.AlterField(
            model_name='openanswerdata',
            name='value',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='qualityanswerdata',
            name='value',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Very Poor'), (2, 'Poor'), (3, 'Average'), (4, 'Good'), (5, 'Very Good')], null=True),
        ),
    ]