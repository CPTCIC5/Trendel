# Generated by Django 3.2.10 on 2022-07-31 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_alter_seller_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='phone_no',
            field=models.CharField(default=8349811004, max_length=10),
            preserve_default=False,
        ),
    ]
