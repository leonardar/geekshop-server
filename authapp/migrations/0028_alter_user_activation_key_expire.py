# Generated by Django 3.2 on 2021-08-10 15:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0027_alter_user_activation_key_expire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expire',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 12, 15, 9, 25, 836186, tzinfo=utc)),
        ),
    ]
