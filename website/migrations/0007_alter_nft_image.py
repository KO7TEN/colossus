"""Import line"""
# Generated by Django 4.0.1 on 2022-04-09 09:14

from django.db import migrations, models


class Migration(migrations.Migration):
    """Class line"""
    dependencies = [
        ('website', '0006_alter_nft_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nft',
            name='image',
            field=models.ImageField(null=True, upload_to='static/nft/nft_pack/'),
        ),
    ]
