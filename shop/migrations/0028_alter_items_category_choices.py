# Generated by Django 4.1.4 on 2023-02-06 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_remove_orderitem_size_choices_orderitem_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='category_choices',
            field=models.CharField(choices=[('DF', 'None'), ('GL', 'goggles'), ('S', 'Shirts'), ('PN', 'Pants'), ('SK', 'Skirts'), ('SH', 'Shoes')], max_length=5),
        ),
    ]
