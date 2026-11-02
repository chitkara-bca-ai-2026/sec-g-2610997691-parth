# Lab 05 - Engineering Calculation Tool
import math

print("======================================")
print("     ENGINEERING CALCULATION TOOL     ")
print("======================================")

val = float(input("Enter a numerical value: "))
exp = float(input("Enter an exponent: "))
dec = float(input("Enter a decimal measurement: "))

power = math.pow(val, exp)
sqrt_val = math.sqrt(val)
ceil_val = math.ceil(dec)
floor_val = math.floor(dec)

print("\n--- Results ---")
print(f"Value              : {val}")
print(f"Exponent           : {exp}")
print(f"Power (pow)        : {power}")
print(f"Square Root (sqrt) : {sqrt_val:.4f}")
print(f"Decimal Value      : {dec}")
print(f"Ceil Value         : {ceil_val}")
print(f"Floor Value        : {floor_val}")
print("======================================")
