# Generated by Django 3.0.2 on 2020-01-30 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20191107_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
