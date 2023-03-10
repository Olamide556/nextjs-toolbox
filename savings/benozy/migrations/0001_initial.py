# Generated by Django 4.1.5 on 2023-01-10 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='SavingCalc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved_on', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=15)),
                ('day', models.IntegerField()),
                ('month', models.CharField(max_length=10)),
                ('is_paid', models.BooleanField(default=False)),
                ('category', models.ManyToManyField(related_name='item', to='benozy.category')),
                ('price', models.ManyToManyField(related_name='amount', to='benozy.price')),
            ],
        ),
    ]
