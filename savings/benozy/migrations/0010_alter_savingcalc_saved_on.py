# Generated by Django 4.1.5 on 2023-01-11 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benozy', '0009_rename_name_category_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savingcalc',
            name='saved_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
