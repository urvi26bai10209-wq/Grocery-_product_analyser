def add_product():
    print("\n--- ADD GROCERY PRODUCT ---")

    name = input("Enter product name: ")
    category = input("Enter category: ")
    quantity = float(input("Enter quantity: "))
    price = float(input("Enter price: ₹"))
    discount=input("is discount available(yes/no):")
    product = {
    "name": name,
    "category": category,
    "quantity": quantity,
    "price": price,
    "discount": discount
    }

    print("Product added successfully!")

    return product


def display_product(product):
    print("\n--- PRODUCT DETAILS ---")
    print("Product Name :", product["name"])
    print("Category     :", product["category"])
    print("Quantity     :", product["quantity"])
    print("Price        : ₹", product["price"])
    print("Discount     :", product["discount"])


def add_multiple_products():
    products = []

    while True:
        product = add_product()
        products.append(product)

        choice = input("\nDo you want to add another item? (yes/no): ")

        if choice.lower() != "yes":
            break

    return products