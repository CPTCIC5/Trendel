# Generated by Django 4.0.6 on 2022-08-06 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0021_remove_productreview_author_productreview_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='seller_ID_method',
            field=models.CharField(choices=[('Aadhar Card', 'Aadhar Card'), ('PAN Card', 'PAN Card')], max_length=20),
        ),
    ]