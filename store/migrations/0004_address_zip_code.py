# Generated by Django 4.1.6 on 2023-02-09 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_add_slug_to_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip_code',
            field=models.CharField(default='-', max_length=10),
            preserve_default=False,
        ),
    ]
