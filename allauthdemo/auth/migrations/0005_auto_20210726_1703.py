# Generated by Django 2.2.18 on 2021-07-26 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allauthdemo_auth', '0004_auto_20210713_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='life',
            name='less_than_10',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='life',
            name='only_for_a_year',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='life',
            name='permanent_need',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='life',
            name='permanent_need_but_can_be_changed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='life',
            name='small_budget',
            field=models.BooleanField(default=False),
        ),
    ]