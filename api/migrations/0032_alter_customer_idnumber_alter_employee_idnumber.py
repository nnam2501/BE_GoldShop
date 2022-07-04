# Generated by Django 4.0.4 on 2022-06-16 14:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_remove_receiptdetail_jewerly_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='idNumber',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(regex='^\\d{12,12}$')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='idNumber',
            field=models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(regex='^\\d{12,12}$')]),
        ),
    ]