# Generated by Django 2.2.18 on 2021-07-13 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allauthdemo_auth', '0003_auto_20210713_0411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='healthrates',
            old_name='profit',
            new_name='premium',
        ),
    ]
