# Generated by Django 4.1.4 on 2023-02-03 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_payment_order_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='item',
            field=models.ManyToManyField(related_name='orders', to='shop.orderitem'),
        ),
    ]
