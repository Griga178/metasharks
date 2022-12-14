# Generated by Django 3.2.16 on 2022-10-14 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salesmanager', '0002_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ammount', models.IntegerField(help_text='Введите колличество автомобилей')),
                ('order_date', models.DateField(blank=True)),
                ('color_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='salesmanager.color')),
                ('model_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='salesmanager.carmodel')),
            ],
            options={
                'ordering': ['order_date'],
            },
        ),
    ]
