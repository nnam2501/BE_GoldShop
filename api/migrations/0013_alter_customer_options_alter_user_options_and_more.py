# Generated by Django 4.0.4 on 2022-05-21 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_employee_options_alter_employee_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
        migrations.AlterModelTable(
            name='customer',
            table='customer',
        ),
        migrations.AlterModelTable(
            name='supplier',
            table='supplier',
        ),
        migrations.AlterModelTable(
            name='typejewerly',
            table='typejewerly',
        ),
        migrations.AlterModelTable(
            name='user',
            table='account',
        ),
    ]
