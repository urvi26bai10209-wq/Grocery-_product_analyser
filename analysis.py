def calculate_final_price(product):
    price = product["price"]
    quantity = product["quantity"]

    amount = price * quantity

    if product["discount"] == "yes":
        discount = amount * 0.10
        final_price = amount - discount
    else:
        final_price = amount

    return final_price


def calculate_total_cost(products):
    total = 0

    for product in products:
        total += calculate_final_price(product)

    return total