# Generated by Django 4.0.4 on 2022-05-18 16:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_supplier_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='phoneNumber',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex='^\\d{10,10}$')]),
        ),
    ]
