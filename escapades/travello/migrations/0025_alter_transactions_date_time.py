# Generated by Django 4.0.2 on 2022-06-13 08:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0024_alter_transactions_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='Date_Time',
            field=models.CharField(default=datetime.datetime(2022, 6, 13, 8, 40, 56, 865554, tzinfo=utc), max_length=19),
        ),
    ]
