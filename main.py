from products import add_multiple_products
from analysis import calculate_total_cost
from display import display_bill


print("=" * 55)
print("              GROCERY BILLING SYSTEM")
print("=" * 55)

products = add_multiple_products()

if len(products) > 0:
    total = calculate_total_cost(products)

    display_bill(products)

    print(f"\nFinal Amount to Pay: ₹{total:.2f}")
else:
    print("No products were added.")

print("\nThank you for shopping!")
