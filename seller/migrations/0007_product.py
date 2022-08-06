# Generated by Django 4.0.6 on 2022-08-05 04:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0006_auto_20220731_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=60)),
                ('product_image', models.ImageField(upload_to='product_images', validators=[django.core.validators.validate_image_file_extension])),
                ('price', models.PositiveIntegerField()),
                ('offer_price', models.PositiveIntegerField()),
                ('size', models.CharField(max_length=60)),
                ('material_type', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('generic_name', models.CharField(max_length=60)),
                ('fit_type', models.CharField(max_length=60)),
                ('material_composition', models.CharField(max_length=60)),
                ('quantity', models.PositiveIntegerField()),
                ('product_published_at', models.DateTimeField(auto_now_add=True)),
                ('product_seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.seller')),
            ],
            options={
                'ordering': ['-product_seller', '-product_published_at'],
            },
        ),
    ]
