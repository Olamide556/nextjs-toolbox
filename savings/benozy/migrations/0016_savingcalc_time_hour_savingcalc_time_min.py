# Generated by Django 4.1.5 on 2023-01-12 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benozy', '0015_alter_savingcalc_day_alter_savingcalc_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='savingcalc',
            name='time_hour',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='savingcalc',
            name='time_min',
            field=models.IntegerField(null=True),
        ),
    ]