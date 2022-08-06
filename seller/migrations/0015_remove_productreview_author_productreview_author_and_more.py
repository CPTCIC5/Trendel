# Generated by Django 4.0.6 on 2022-08-05 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seller', '0014_alter_seller_seller_id_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productreview',
            name='author',
        ),
        migrations.AddField(
            model_name='productreview',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='seller',
            name='seller_ID_method',
            field=models.CharField(choices=[('PAN Card', 'PAN Card'), ('Aadhar Card', 'Aadhar Card')], max_length=20),
        ),
    ]
