# Generated by Django 4.0.4 on 2022-06-27 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0041_alter_order_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-id']},
        ),
    ]
