# Generated by Django 4.0.6 on 2022-08-08 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0024_category_alter_seller_seller_id_method_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='seller_ID_method',
            field=models.CharField(choices=[('Aadhar Card', 'Aadhar Card'), ('PAN Card', 'PAN Card')], max_length=20),
        ),
    ]