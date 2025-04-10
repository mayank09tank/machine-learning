# # Incrementing a Number Using +=
num = 20
num += 10  # Increases num by 10
print(num)  # Output: 30

# Write a Python program to check if a given year is a leap year or not
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")


# Write a program that asks the user to enter their marks and displays their grade: • 90-100: A 
marks = int(input("Enter your marks: "))

if 90 <= marks <= 100:
    grade = "A"
elif 80 <= marks < 90:
    grade = "B"
elif 70 <= marks < 80:
    grade = "C"
elif 60 <= marks < 70:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")






