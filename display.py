def display_bill(products):
    print("\n")
    print("=" * 55)
    print("                    GROCERY BILL")
    print("=" * 55)

    print(f"{'Product':<15}{'Qty':<8}{'Price':<12}{'Discount':<10}{'Amount':<10}")
    print("-" * 55)

    total = 0

    for product in products:
        price = product["price"]
        quantity = product["quantity"]

        amount = price * quantity

        if product["discount"] == "yes":
            discount = amount * 0.10
            final_amount = amount - discount
        else:
            final_amount = amount

        total += final_amount

        print(
            f"{product['name']:<15}"
            f"{quantity:<8}"
            f"₹{price:<11.2f}"
            f"{product['discount']:<10}"
            f"₹{final_amount:<10.2f}"
        )

    print("-" * 55)
    print(f"{'TOTAL BILL':<45}₹{total:.2f}")
    print("=" * 55)
    print("          Thank you for shopping!")
    print("=" * 55)