# Generated by Django 4.1 on 2022-09-06 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d'),
        ),
    ]
