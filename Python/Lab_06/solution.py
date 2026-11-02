# Lab 06 - Shop Billing System

print("========================================")
print("       CLOTHING STORE BILLING SYSTEM    ")
print("========================================")

name = input("Enter Customer Name: ")
garment = input("Enter Garment Name: ")
price = float(input("Enter Price of one garment: "))
qty = int(input("Enter Number of Garments: "))

total = price * qty

print("\n========================================")
print("                  BILL                  ")
print("========================================")
print(f"  Customer Name  : {name}")
print(f"  Garment Name   : {garment}")
print(f"  Price per Unit : Rs. {price}")
print(f"  Quantity       : {qty}")
print(f"  Total Amount   : Rs. {total}")
print("========================================")
