# Generated by Django 4.1.4 on 2023-02-02 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_rename_items_orderitem_item_orderitem_ordered_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='None', max_length=1000),
            preserve_default=False,
        ),
    ]
