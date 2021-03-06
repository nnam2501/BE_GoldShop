# Generated by Django 4.0.4 on 2022-06-11 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_alter_jewerly_jewerlyimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='firstName',
            new_name='fullName',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='firstName',
            new_name='fullName',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='lastName',
        ),
    ]
