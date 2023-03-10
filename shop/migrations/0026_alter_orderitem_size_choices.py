# Generated by Django 4.1.4 on 2023-02-04 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_remove_items_size_choices_orderitem_size_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='size_choices',
            field=models.CharField(choices=[('N', 'None'), ('S', 'SMALL'), ('M', 'MEDIUM'), ('ML', 'MEDIUM LARGE'), ('L', 'LARGE'), ('XL', 'EXTRA LARGE'), ('XXL', 'EXTRA EXTRA LARGE')], default='M', max_length=5),
        ),
    ]
