# Generated by Django 3.2 on 2021-07-26 12:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_alter_user_activation_key_expire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expire',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 28, 12, 59, 22, 397474, tzinfo=utc)),
        ),
    ]
