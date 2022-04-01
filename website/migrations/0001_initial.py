"""Import line"""
# Generated by Django 4.0 on 2022-02-09 16:54

from django.db import migrations, models


class Migration(migrations.Migration):
    """Class line"""
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NFT',
            fields=[
                ('id',
                 models.BigAutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('image',
                 models.TextField()),
                ('name',
                 models.TextField()),
                ('price',
                 models.IntegerField()),
            ],
        ),
    ]
