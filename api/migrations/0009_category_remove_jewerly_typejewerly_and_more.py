# Generated by Django 4.0.4 on 2022-05-21 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_supplier_phonenumber_employee_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.RemoveField(
            model_name='jewerly',
            name='typeJewerly',
        ),
        migrations.AddField(
            model_name='jewerly',
            name='typeJewerly',
            field=models.ManyToManyField(blank=True, null=True, to='api.typejewerly'),
        ),
        migrations.AddField(
            model_name='typejewerly',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.category'),
        ),
    ]
