spent = 3
donated = 4

total_amount = spent + donated
print(total_amount)


items = 10
price = 2

total_price = items * price
print(total_price)

# Printing Multiple Variables
print(total_price, items, price)   # Output: 20 10 2
print("Total Price:", total_price, "Items:", items, "Price per item:", price)
print(f"Total Price: {total_price}, Items: {items}, Price per item: {price}")
print("Total Price: {}, Items: {}, Price per item: {}".format(total_price, items, price))   # Using positional placeholders
print("Total Price: {tp}, Items: {it}, Price per item: {pr}".format(tp=total_price, it=items, pr=price))    # Using named placeholders
print("Total Price: {0}, Items: {1}, Price per item: {2}".format(total_price, items, price))   # Using indexed placeholders
print("Total Price: {0}, Items: {1}, Price per item: {2}".format(total_price, items, price))   # Using indexed placeholders
print("Total Price: {tp}, Items: {it}, Price per item: {pr}".format(tp=total_price, it=items, pr=price))    # Using named placeholders
print("Total Price: {}, Items: {}, Price per item: {}".format(total_price, items, price))   # Using positional placeholders
print(f"Total Price: {total_price}, Items: {items}, Price per item: {price}")
print("Total Price:", total_price, "Items:", items, "Price per item:", price)
