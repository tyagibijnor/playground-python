## calculate shoping items value

# Example usage

cart_test = [
        {'name': 'Apple', 'price': 5, 'quantity': 4},
        {'name': 'Banana', 'price': 3, 'quantity': 6},
        {'name': 'Orange', 'price': 8, 'quantity': 3}
    ]

cart_test2 = [
        {'name': 'Apple', 'price': 7, 'quantity': 14},
        {'name': 'Banana', 'price': 6, 'quantity': 60},
        {'name': 'Orange', 'price': 4, 'quantity': 43}
    ]
    
def calculate_total(cart_items):
    total = 0
    for item in cart_items:    
        total += item['price'] * item['quantity']
    return total
    
total_value = calculate_total(cart_test)
print(f"Total value of the cart: Rs.{total_value}")

total_value2 = calculate_total(cart_test2)
print(f"Total value2 of the cart: Rs.{total_value2}")
