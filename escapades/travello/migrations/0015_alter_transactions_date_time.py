# Generated by Django 3.2.9 on 2021-11-16 15:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0014_alter_transactions_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='Date_Time',
            field=models.CharField(default=datetime.datetime(2021, 11, 16, 15, 31, 9, 831568, tzinfo=utc), max_length=19),
        ),
    ]
