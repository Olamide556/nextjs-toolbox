# Generated by Django 4.1.5 on 2023-01-10 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('benozy', '0002_price_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savingcalc',
            name='image',
        ),
    ]
