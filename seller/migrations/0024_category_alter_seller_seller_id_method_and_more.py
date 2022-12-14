# Generated by Django 4.0.6 on 2022-08-08 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0023_productreview_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.AlterField(
            model_name='seller',
            name='seller_ID_method',
            field=models.CharField(choices=[('PAN Card', 'PAN Card'), ('Aadhar Card', 'Aadhar Card')], max_length=20),
        ),
        migrations.DeleteModel(
            name='ProductReview',
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ManyToManyField(to='seller.category'),
        ),
    ]
