class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.quantity = 0

class Cart:
    def __init__(self):
        self.products = []
    
    def add(self, product, quantity):
        product.quantity = quantity
        self.products.append(product)
    
    def subtotal(self):
        return sum(product.price * product.quantity for product in self.products)
    
    def discount(self):
        total_quantity = sum(product.quantity for product in self.products)
        max_quantity = max(product.quantity for product in self.products)
        
        if self.subtotal() > 200:
            return "flat_10_discount", 10
        elif max_quantity > 10:
            return "bulk_5_discount", 0.05
        elif total_quantity > 20:
            return "bulk_10_discount", 0.1
        elif total_quantity > 30 and max_quantity > 15:
            return "tiered_50_discount", 0.5
        else:
            return None, 0
    
    def cal_discount(self):
        discount_name, discount_value = self.discount()
        subtotal = self.subtotal()
        return discount_name, subtotal * discount_value
    
    def giftwrap_fee(self):
        return sum(product.quantity for product in self.products)
    
    def shipping_fee(self):
        total_quantity = sum(product.quantity for product in self.products)
        return (total_quantity + 9) // 10 * 5
    
    def cal_total(self):
        subtotal = self.subtotal()
        discount_name, discount_amount = self.cal_discount()
        shipping_fee = self.shipping_fee()
        gift_wrap_fee = self.giftwrap_fee()
        total = subtotal - discount_amount + shipping_fee + gift_wrap_fee
        return subtotal, discount_name, discount_amount, shipping_fee, gift_wrap_fee, total

def main():
    products = [
        Product("Product A", 20),
        Product("Product B", 40),
        Product("Product C", 50)
    ]
    
    cart = Cart()
    
    for product in products:
        quantity = int(input(f"Enter quantity of {product.name}: "))
        gift_wrapped = input(f" {product.name} wrapped as a gift? (yes/no): ").lower() == "yes"
        if gift_wrapped:
            quantity += 1
        cart.add(product, quantity)
    
    subtotal, discount_name, discount_amount, shipping_fee, gift_wrap_fee, total = cart.cal_total()
    
    print("\n\n=== Receipt ===")
    for product in cart.products:
        print(f"{product.name}: Quantity - {product.quantity}, Total - ${product.price * product.quantity}")
    print(f"\nSubtotal: ${subtotal}")
    print(f"Discount Applied: {discount_name}, Amount Saved: ${discount_amount}")
    print(f"Shipping Fee: ${shipping_fee}")
    print(f"Gift Wrap Fee: ${gift_wrap_fee}")
    print(f"\nTotal: ${total}")

if __name__ == "__main__":
    main()