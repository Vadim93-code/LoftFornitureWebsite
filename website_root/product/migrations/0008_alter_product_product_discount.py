# Generated by Django 4.1.2 on 2022-10-23 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_product_product_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_discount',
            field=models.IntegerField(default=0, max_length=200, verbose_name='Discount'),
        ),
    ]
