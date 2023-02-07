# Generated by Django 4.1.4 on 2023-01-27 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_footerinfos_delete_pay_delete_people'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('images', models.ImageField(upload_to='blog')),
            ],
        ),
        migrations.DeleteModel(
            name='BlogImages',
        ),
    ]
