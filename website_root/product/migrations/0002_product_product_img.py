# Generated by Django 4.1.2 on 2022-10-11 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_img',
            field=models.ImageField(default='./static/img/background-slider.jpg', upload_to='img/'),
        ),
    ]
