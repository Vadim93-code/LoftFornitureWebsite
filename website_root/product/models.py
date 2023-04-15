from django.db import models


class Product(models.Model):
    # Information that shows on product card:
    product_img = models.ImageField(upload_to="product", default="./static/img/product_img.png")  # Main product image
    product_name = models.CharField(default="None", max_length=200, verbose_name="Name")  # Product's Name
    product_price = models.IntegerField(default=0, verbose_name="Price")  # Product's Price
    product_discount = models.IntegerField(default=0, verbose_name="Discount")  # Product's Discount

    product_width = models.CharField(default="None", max_length=50, verbose_name="Width")  # Width of Product
    product_depth = models.CharField(default="None", max_length=50, verbose_name="Depth")  # Depth of Product
    product_height = models.CharField(default="None", max_length=50, verbose_name="Height")  # Height of Product

    product_color = models.CharField(default="None", max_length=100, verbose_name="Color")  # Product's Color
    product_description = models.CharField(default="None", max_length=10000, verbose_name="Description")  # Product's Description
    product_grade = models.CharField(default="None", max_length=200, verbose_name="Grade")  # Product's Grade
    product_category = models.CharField(default="None", max_length=200, verbose_name="Category")  # Product's Category

    # Sleeping Place (Width x Depth x Height) or None if it not exists
    product_sleeping_place = models.CharField(default="None", max_length=200, verbose_name="Sleeping Place")

    # Seat Place (Width x Depth x Height) or None if it not exists
    product_seat_place = models.CharField(default="None", max_length=200, verbose_name="Seat Place")

    # Frame of Product (Materials what use for create product), "None" if it not exists
    product_frame = models.CharField(default="None", max_length=500, verbose_name="Frame")

    # Materials what use for create product legs, "None" if it not exists
    product_material_of_legs = models.CharField(default="None", max_length=500, verbose_name="Material of Legs")

    # Materials what use for create products pillow, "None" if it not exists
    product_material_of_pillow = models.CharField(default="None", max_length=500, verbose_name="Material of Pillow")

    # Space for Underware, "False" if it not exists
    product_space_for_underware = models.BooleanField(default="False", verbose_name="Space for Underware")

    # USB port if it exists, if not select "False" in the field
    product_usb_port = models.BooleanField(default="False", verbose_name="USB Port")

    # Removable cover, if it not exists select "False"
    product_removable_cover = models.BooleanField(default="False", verbose_name="Removable Cover")

    # Decorative pillows, if it not exists select "False" in the field
    product_decorate_pillows = models.BooleanField(default="False", verbose_name="Decorate Pillows")

    # Manufacturer (country which made that)
    product_manufacturer = models.CharField(default="None", max_length=200, verbose_name="Manufacturer")

    def __str__(self):
        return self.product_name


class FormForEmail(models.Model):
    user_name = models.CharField("User Name", max_length=50)
    user_email = models.CharField("User Email", max_length=50)
    user_message = models.CharField("User Message", max_length=500)
    user_file = models.FileField(upload_to='product', default="./static/img/product_img.png")

    def __str__(self):
        return self.user_email


class User(models.Model):
    user_first_name = models.CharField("User first name", max_length=200)

