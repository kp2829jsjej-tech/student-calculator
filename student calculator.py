
print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter student name: ")

total = 0

for i in range(1, 6):
    mark = int(input(f"Enter subject {i} marks: "))
    total += mark

percentage = total / 5

print("\n===== RESULT =====")
print("Student Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage, "%")

if percentage >= 90:
    print("Grade: A")
elif percentage >= 75:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 40:
    print("Grade: D")
else:
    print("Grade: Fail")

