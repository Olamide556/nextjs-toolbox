# Generated by Django 4.1.5 on 2023-01-11 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('benozy', '0004_remove_savingcalc_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savingcalc',
            name='price',
        ),
    ]