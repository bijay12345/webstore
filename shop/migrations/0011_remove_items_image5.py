# Generated by Django 4.1.4 on 2023-01-30 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_items_image2_items_image3_items_image4_items_image5'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='image5',
        ),
    ]
