#discounts
CATEGORY_DISCOUNTS = {
    "Electronics": 0.10,
    "Clothing": 0.15,
    "Books": 0.05,
    "Home": 0.12
}

TIER_DISCOUNTS = {
    "Premium": 0.05,
    "Standard": 0.00,
    "Budget": 0.02
}


def read_products(file_path):
    """Read products from a file and return a list of dictionaries."""
    products = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) != 4:
                    print(f"Skipping invalid line: {line}")
                    continue
                name, base_price, category, tier = parts
                try:
                    base_price = float(base_price)
                except ValueError:
                    print(f"Invalid price for product '{name}': {base_price}")
                    continue
                products.append({
                    "name": name,
                    "base_price": base_price,
                    "category": category,
                    "tier": tier
                })
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    return products


def calculate_final_price(product):
    """Calculate final price, total discount percent, and discount amount."""
    category_discount = CATEGORY_DISCOUNTS.get(product["category"], 0)
    tier_discount = TIER_DISCOUNTS.get(product["tier"], 0)
    total_discount = category_discount + tier_discount
    discount_amount = product["base_price"] * total_discount
    final_price = product["base_price"] - discount_amount
    return round(final_price, 2), round(total_discount * 100, 2), round(discount_amount, 2)


def generate_pricing_report(products, report_file):
    """Generate pricing report and print summary."""
    total_discount_sum = 0
    try:
        with open(report_file, 'w') as f:
            # Header
            header = f"{'Product Name':20} {'Base Price':12} {'Discount (%)':14} {'Discount Amt':14} {'Final Price':12}\n"
            f.write(header)
            f.write("-" * len(header) + "\n")

            # Write each product
            for product in products:
                final_price, discount_percent, discount_amount = calculate_final_price(product)
                total_discount_sum += discount_percent
                f.write(
                    f"{product['name']:20} {product['base_price']:12.2f} {discount_percent:14.2f} {discount_amount:14.2f} {final_price:12.2f}\n")

        # Print summary to console
        total_products = len(products)
        avg_discount = total_discount_sum / total_products if total_products > 0 else 0
        print(f"Total products processed: {total_products}")
        print(f"Average discount applied: {avg_discount:.2f}%")

    except PermissionError:
        print(f"Error: Cannot write to file '{report_file}'.")


def main():
    products_file = "products.txt"
    report_file = "pricing_report.txt"

    products = read_products(products_file)
    if products:
        generate_pricing_report(products, report_file)


if __name__ == "__main__":
    main()
