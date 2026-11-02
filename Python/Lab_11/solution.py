# Lab 11 - Online Account Registration
import getpass

username = input("Enter your username: ")
password = input("Enter your password: ")

print("==========================================")
print("        PASSWORD VALIDATION REPORT        ")
print("==========================================")
print(f"Username: {username}")
print(f"Password: {'*' * len(password)}")
print("\n--- Validation Rules ---")

length_pass = len(password) >= 8
digit_pass = any(c.isdigit() for c in password)
upper_pass = any(c.isupper() for c in password)

print(f"[{'PASS' if length_pass else 'FAIL'}] Minimum 8 characters ({len(password)} characters)")
print(f"[{'PASS' if digit_pass else 'FAIL'}] At least one digit")
print(f"[{'PASS' if upper_pass else 'FAIL'}] At least one uppercase letter")

print("\n--- Result ---")
if length_pass and digit_pass and upper_pass:
    print("Password is VALID!")
    print(f"Account created successfully for {username}!")
else:
    print("Password is INVALID!")

print("\n==========================================")
