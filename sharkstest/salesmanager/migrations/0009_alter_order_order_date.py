# Generated by Django 3.2.16 on 2022-10-16 19:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('salesmanager', '0008_alter_carmodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=django.utils.timezone.localdate),
        ),
    ]