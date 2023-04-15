def python_discount_function(discount, price):
    price = int(price)
    discount = int(discount)
    actual_price = price * ((100 - discount)/100)

    return actual_price
