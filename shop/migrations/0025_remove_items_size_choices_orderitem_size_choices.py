# Generated by Django 4.1.4 on 2023-02-04 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_items_size_choices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='size_choices',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='size_choices',
            field=models.CharField(choices=[('N', 'None'), ('S', 'SMALL'), ('M', 'MEDIUM'), ('ML', 'MEDIUM LARGE'), ('L', 'LARGE'), ('XL', 'EXTRA LARGE'), ('XXL', 'EXTRA EXTRA LARGE')], default='N', max_length=5),
            preserve_default=False,
        ),
    ]