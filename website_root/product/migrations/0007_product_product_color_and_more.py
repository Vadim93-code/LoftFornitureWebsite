# Generated by Django 4.1.2 on 2022-10-22 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_product_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_color',
            field=models.CharField(default='None', max_length=100, verbose_name='Color'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_decorate_pillows',
            field=models.BooleanField(default='False', verbose_name='Decorate Pillows'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_depth',
            field=models.CharField(default='None', max_length=50, verbose_name='Depth'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_description',
            field=models.CharField(default='None', max_length=10000, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_discount',
            field=models.CharField(default='None', max_length=200, verbose_name='Discount'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_frame',
            field=models.CharField(default='None', max_length=500, verbose_name='Frame'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_grade',
            field=models.CharField(default='None', max_length=200, verbose_name='Grade'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_height',
            field=models.CharField(default='None', max_length=50, verbose_name='Height'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_manufacturer',
            field=models.CharField(default='None', max_length=200, verbose_name='Manufacturer'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_material_of_legs',
            field=models.CharField(default='None', max_length=500, verbose_name='Material of Legs'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_material_of_pillow',
            field=models.CharField(default='None', max_length=500, verbose_name='Material of Pillow'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_removable_cover',
            field=models.BooleanField(default='False', verbose_name='Removable Cover'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_seat_place',
            field=models.CharField(default='None', max_length=200, verbose_name='Seat Place'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_sleeping_place',
            field=models.CharField(default='None', max_length=200, verbose_name='Sleeping Place'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_space_for_underware',
            field=models.BooleanField(default='False', verbose_name='Space for Underware'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_usb_port',
            field=models.BooleanField(default='False', verbose_name='USB Port'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_width',
            field=models.CharField(default='None', max_length=50, verbose_name='Width'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.CharField(default='None', max_length=200, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(default='None', max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.CharField(default='None', max_length=200, verbose_name='Price'),
        ),
    ]
