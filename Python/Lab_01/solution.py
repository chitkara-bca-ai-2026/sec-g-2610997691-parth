# Lab 01 - Student Fee Calculator

tuition = float(input("Enter Tuition Fee: "))
lab = float(input("Enter Lab Fee: "))
library = float(input("Enter Library Fee: "))
exam = float(input("Enter Exam Fee: "))
discount = float(input("Enter Discount Amount: "))

total = tuition + lab + library + exam
after_discount = total - discount
annual = after_discount * 2
monthly = annual / 12

print(f"\nTuition Fee: {tuition}")
print(f"Lab Fee: {lab}")
print(f"Library Fee: {library}")
print(f"Exam Fee: {exam}")
print(f"Total Fee: {total}")
print(f"Discount: {discount}")
print(f"Fee after Discount: {after_discount}")
print(f"Annual Fee: {annual}")
print(f"Monthly Installment: {monthly:.2f}")
