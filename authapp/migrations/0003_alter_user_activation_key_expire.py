# Generated by Django 3.2 on 2021-07-26 08:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20210721_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expire',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 28, 8, 56, 19, 149063, tzinfo=utc)),
        ),
    ]
