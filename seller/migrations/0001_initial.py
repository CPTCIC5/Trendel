# Generated by Django 4.0.6 on 2022-07-31 05:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=100)),
                ('seller_name', models.CharField(max_length=100)),
                ('shop_is_registered', models.BooleanField(default=False)),
                ('seller_ID_methods', models.CharField(choices=[('Aadhar Card', 'Aadhar Card'), ('PAN Card', 'PAN Card')], max_length=20)),
                ('seller_ID', models.CharField(blank=True, max_length=12, null=True, unique=True)),
                ('shop_address', models.CharField(max_length=250)),
                ('seller_registered_at', models.DateTimeField(auto_now_add=True)),
                ('seller_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
