# Generated by Django 4.1.2 on 2022-12-12 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_alter_product_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormForEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, verbose_name='User Name')),
                ('user_email', models.CharField(max_length=50, verbose_name='User Email')),
                ('user_message', models.CharField(max_length=500, verbose_name='User Message')),
            ],
        ),
    ]
