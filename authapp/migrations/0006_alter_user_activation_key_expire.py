# Generated by Django 3.2 on 2021-07-26 13:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_alter_user_activation_key_expire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expire',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 28, 13, 0, 50, 587764, tzinfo=utc)),
        ),
    ]
