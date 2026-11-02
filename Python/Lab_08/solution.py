# Lab 08 - School Result Processing

print("==================================================")
print("             SCHOOL RESULT PROCESSING             ")
print("==================================================")

name = input("Enter Student Name : ")
roll = input("Enter Roll Number  : ")

print("\n--- Enter Marks for 5 Subjects (0-100) ---")
total_marks = 0
failed = False

for i in range(1, 6):
    marks = float(input(f"Enter marks for Subject {i}: "))
    if marks < 0 or marks > 100:
        print("Error: Marks must be between 0 and 100.")
        exit()
    if marks < 40:
        failed = True
    total_marks += marks

percentage = (total_marks / 500) * 100

if failed:
    result = "FAIL"
    grade = "F"
    remarks = "Failed in one or more subjects"
else:
    result = "PASS"
    if percentage >= 90:
        grade = "A+"
        remarks = "Outstanding"
    elif percentage >= 80:
        grade = "A"
        remarks = "Excellent"
    elif percentage >= 70:
        grade = "B"
        remarks = "Very Good"
    elif percentage >= 60:
        grade = "C"
        remarks = "Good"
    elif percentage >= 50:
        grade = "D"
        remarks = "Satisfactory"
    elif percentage >= 40:
        grade = "E"
        remarks = "Pass"
    else:
        grade = "F"
        remarks = "Fail"

print("\n==================================================")
print("               STUDENT REPORT CARD                ")
print("==================================================")
print(f"  Student Name : {name}")
print(f"  Roll Number  : {roll}")
print("--------------------------------------------------")
print(f"  Total Marks  : {total_marks} / 500.0")
print(f"  Percentage   : {percentage:.2f}%")
print(f"  Result       : {result}")
print(f"  Grade        : {grade}")
print(f"  Remarks      : {remarks}")
print("==================================================")
