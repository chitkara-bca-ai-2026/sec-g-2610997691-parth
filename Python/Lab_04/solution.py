# Lab 04 - Data Conversion Utility

print("==========================================")
print("          DATA CONVERSION UTILITY         ")
print("==========================================")

name = input("Enter Product Name : ")
price_str = input("Enter Price        : ")
qty_str = input("Enter Quantity     : ")

price = float(price_str)
qty = int(qty_str)
total_price = price * qty
amount_str = str(total_price)

print("\n------------------------------------------")
print("           TYPE CASTING SUMMARY           ")
print("------------------------------------------")
print(f"{'Variable':<15} {'Value':<15} {'Python Type'}")
print("------------------------------------------")
print(f"{'product_name':<15} {name:<15} {type(name)}")
print(f"{'price':<15} {price:<15} {type(price)}")
print(f"{'quantity':<15} {qty:<15} {type(qty)}")
print(f"{'total_price':<15} {total_price:<15} {type(total_price)}")
print(f"{'amount_str':<15} {amount_str:<15} {type(amount_str)}")

print("\n------------------------------------------")
print("               TAX INVOICE                ")
print("------------------------------------------")
print(f"Product Name    : {name}")
print(f"Price per Unit  : Rs. {price:.2f}")
print(f"Quantity        : {qty}")
print("------------------------------------------")
print(f"Invoice Total   : Rs. {total_price:.1f}")
print("==========================================")
