# Generated by Django 4.0.6 on 2022-09-07 05:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_user_profile_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 7, 11, 7, 27, 561491)),
        ),
    ]
