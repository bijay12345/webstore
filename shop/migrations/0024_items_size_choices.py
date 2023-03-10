# Generated by Django 4.1.4 on 2023-02-04 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_rename_category_items_category_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='size_choices',
            field=models.CharField(choices=[('N', 'None'), ('S', 'SMALL'), ('M', 'MEDIUM'), ('ML', 'MEDIUM LARGE'), ('L', 'LARGE'), ('XL', 'EXTRA LARGE'), ('XXL', 'EXTRA EXTRA LARGE')], default='N', max_length=5),
            preserve_default=False,
        ),
    ]
