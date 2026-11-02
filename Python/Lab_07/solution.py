# Lab 07 - Calendar Verification System

print("===========================================")
print("        CALENDAR VERIFICATION SYSTEM       ")
print("===========================================")

year = int(input("Enter year: "))
if year <= 0:
    print("Error: Year must be a positive integer.")
    exit()

print("\n-------------------------------------------")
print(f"Year: {year}")

is_leap = False
reason = ""

if year % 100 == 0:
    if year % 400 == 0:
        is_leap = True
        reason = "Century year divisible by 400"
    else:
        is_leap = False
        reason = "Century year not divisible by 400"
else:
    if year % 4 == 0:
        is_leap = True
        reason = "Divisible by 4 and not a century year"
    else:
        is_leap = False
        reason = "Not divisible by 4"

if is_leap:
    print("Status: LEAP YEAR")
    print("Days in Year: 366 days")
    print("Days in February: 29 days")
else:
    print("Status: COMMON YEAR")
    print("Days in Year: 365 days")
    print("Days in February: 28 days")

print(f"Reason: {reason}")
print("-------------------------------------------")
