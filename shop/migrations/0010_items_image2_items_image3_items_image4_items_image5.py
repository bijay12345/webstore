# Generated by Django 4.1.4 on 2023-01-30 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_items_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='image2',
            field=models.ImageField(default='default.jpg', upload_to='products'),
        ),
        migrations.AddField(
            model_name='items',
            name='image3',
            field=models.ImageField(default='default.jpg', upload_to='products'),
        ),
        migrations.AddField(
            model_name='items',
            name='image4',
            field=models.ImageField(default='default.jpg', upload_to='products'),
        ),
        migrations.AddField(
            model_name='items',
            name='image5',
            field=models.ImageField(default='default.jpg', upload_to='products'),
        ),
    ]
