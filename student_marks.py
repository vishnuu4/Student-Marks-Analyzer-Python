name = input("Enter your name: ")

a = int(input("Enter your marks in sub1: "))
b = int(input("Enter your marks in sub2: "))
c = int(input("Enter your marks in sub3: "))
d = int(input("Enter your marks in sub4: "))
e = int(input("Enter your marks in sub5: "))

total = a + b + c + d + e
average = total / 5
percentage = total / 500 * 100

print(f"Student: {name}")
print(f"Total marks: {total}")
print(f"Average: {average}")
print(f"Percentage: {percentage}%")

if percentage >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")
