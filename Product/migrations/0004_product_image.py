# Generated by Django 4.1 on 2022-09-04 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_product_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='%/Y/%m/%d'),
        ),
    ]
