# Generated by Django 4.1.2 on 2022-10-11 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=models.ImageField(default='./static/img/background-slider.jpg', upload_to=None),
        ),
    ]
