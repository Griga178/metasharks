# Generated by Django 3.2.16 on 2022-10-16 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salesmanager', '0009_alter_order_order_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='ammount',
            new_name='amount',
        ),
    ]
