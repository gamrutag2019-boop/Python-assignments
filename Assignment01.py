# Q1. Check whether a number is positive, negative, or zero.

number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# Q2. Check whether a number is even or odd.

number = int(input("Enter an integer: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# Q3. Find the greater of two numbers.

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
if a > b:
    print("Greater number:", a)
elif b > a:
    print("Greater number:", b)
else:
    print("Both numbers are equal.")


# Q4. Find the greatest of three numbers.

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
if a >= b and a >= c:
    print("Greatest number:", a)
elif b >= a and b >= c:
    print("Greatest number:", b)
else:
    print("Greatest number:", c)


# Q5. Check whether a person is eligible to vote (age >= 18).

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")


# Q6. Check whether a year is a leap year.

year = int(input("Enter a year: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year.")
else:
    print("Not a leap year.")


# Q7. Check whether a character is a vowel or consonant.

char = input(" Enter one alphabet: ").lower()
if len(char) != 1 or not char.isalpha():
    print("Please enter exactly one alphabet.")
elif char in "aeiou":
    print("It is a vowel.")
else:
    print("It is a consonant.")


# Q8. Check whether a number is divisible by both 5 and 11.

number = int(input("Enter an integer: "))
if number % 5 == 0 and number % 11 == 0:
    print("The number is divisible by both 5 and 11.")
else:
    print("The number is not divisible by both 5 and 11.")


# Q9. Check whether a number is a multiple of both 3 and 7.

number = int(input("Enter an integer: "))
if number % 3 == 0 and number % 7 == 0:
    print("The number is a multiple of both 3 and 7.")
else:
    print("The number is not a multiple of both 3 and 7.")


# Q10. Assign grades based on marks: 90-100 A, 80-89 B, 70-79 C, 60-69 D, below 60 F.

marks = float(input("Enter marks out of 100: "))
if marks < 0 or marks > 100:
    print("Invalid marks. Enter a value from 0 to 100.")
elif marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# Q11. Check whether a character is uppercase or lowercase.

char = input("Enter one alphabet: ")
if len(char) != 1 or not char.isalpha():
    print("Please enter exactly one alphabet.")
elif char.isupper():
    print("Uppercase letter.")
else:
    print("Lowercase letter.")


# Q12. Find whether the entered alphabet is a vowel using if-elif.

char = input("Enter one alphabet: ").lower()
if len(char) != 1 or not char.isalpha():
    print("Please enter exactly one alphabet.")
elif char == "a":
    print("Vowel")
elif char == "e":
    print("Vowel")
elif char == "i":
    print("Vowel")
elif char == "o":
    print("Vowel")
elif char == "u":
    print("Vowel")
else:
    print("Consonant")


# Q13. Check whether three sides can form a triangle.

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))
if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    print("These sides can form a triangle.")
else:
    print("These sides cannot form a triangle.")


# Q14. Determine the type of triangle (Equilateral, Isosceles, Scalene).

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))
if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle.")
elif a == b == c:
    print("Equilateral triangle.")
elif a == b or a == c or b == c:
    print("Isosceles triangle.")
else:
    print("Scalene triangle.")


# Q15. Find the largest among four numbers.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
d = float(input("Enter fourth number: "))
largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c
if d > largest:
    largest = d
print("Largest number:", largest)


# Q16. Check whether a number is a three-digit number.

number = int(input("Enter an integer: "))
if 100 <= abs(number) <= 999:
    print("It is a three-digit number.")
else:
    print("It is not a three-digit number.")


# Q17. Calculate electricity bill using sample slab rates.

units = float(input("Enter electricity units consumed: "))
if units < 0:
    print("Units cannot be negative.")
elif units <= 100:
    bill = units * 1.50
    print("Electricity bill: Rs.", round(bill, 2))
elif units <= 200:
    bill = 100 * 1.50 + (units - 100) * 2.50
    print("Electricity bill: Rs.", round(bill, 2))
elif units <= 300:
    bill = 100 * 1.50 + 100 * 2.50 + (units - 200) * 4.00
    print("Electricity bill: Rs.", round(bill, 2))
else:
    bill = 100 * 1.50 + 100 * 2.50 + 100 * 4.00 + (units - 300) * 6.00
    print("Electricity bill: Rs.", round(bill, 2))


# Q18. Calculate income tax using illustrative income slabs (practice only).

income = float(input("Enter annual taxable income in Rs.: "))
if income < 0:
    print("Income cannot be negative.")
elif income <= 300000:
    tax = 0
    print("Illustrative tax amount: Rs.", tax)
elif income <= 600000:
    tax = (income - 300000) * 0.05
    print("Illustrative tax amount: Rs.", round(tax, 2))
elif income <= 900000:
    tax = 15000 + (income - 600000) * 0.10
    print("Illustrative tax amount: Rs.", round(tax, 2))
elif income <= 1200000:
    tax = 45000 + (income - 900000) * 0.15
    print("Illustrative tax amount: Rs.", round(tax, 2))
else:
    tax = 90000 + (income - 1200000) * 0.20
    print("Illustrative tax amount: Rs.", round(tax, 2))


# Q19. Check if a student passes (minimum 35 marks in each subject).

s1 = float(input("Enter marks in subject 1: "))
s2 = float(input("Enter marks in subject 2: "))
s3 = float(input("Enter marks in subject 3: "))
if s1 >= 35 and s2 >= 35 and s3 >= 35:
    print("Student has passed.")
else:
    print("Student has failed.")


# Q20. Check whether a number is within a given range.

number = float(input("Enter a number: "))
low = float(input("Enter the lower limit: "))
high = float(input("Enter the upper limit: "))
if low > high:
    print("Invalid range: lower limit must not exceed upper limit.")
elif low <= number <= high:
    print("The number is within the range.")
else:
    print("The number is outside the range.")


# Q21. Build a simple calculator using if-elif-else (+, -, *, /).

a = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))
if operator == "+":
    print("Result:", a + b)
elif operator == "-":
    print("Result:", a - b)
elif operator == "*":
    print("Result:", a * b)
elif operator == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operator.")


# Q22. Check whether a year is a century leap year.

year = int(input("Enter a year: "))
if year % 100 == 0 and year % 400 == 0:
    print("It is a century leap year.")
elif year % 100 == 0:
    print("It is a century year, but not a leap year.")
elif year % 4 == 0:
    print("It is a leap year, but not a century year.")
else:
    print("It is not a leap year.")


# Q23. Determine the season based on the month number (simplified Indian seasons).

month = int(input("Enter month number (1-12): "))
if month in (3, 4, 5):
    print("Summer")
elif month in (6, 7, 8, 9):
    print("Monsoon")
elif month in (10, 11):
    print("Autumn / post-monsoon")
elif month in (12, 1, 2):
    print("Winter")
else:
    print("Invalid month number.")


# Q24. Find the number of days in a month, considering leap years.

month = int(input("Enter month number (1-12): "))
year = int(input("Enter year: "))
if month < 1 or month > 12:
    print("Invalid month.")
elif month == 2:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("February has 29 days.")
    else:
        print("February has 28 days.")
elif month in (4, 6, 9, 11):
    print("This month has 30 days.")
else:
    print("This month has 31 days.")


# Q25. Check whether a password meets minimum conditions (8 characters and at least one digit).

password = input("Enter a password: ")
has_digit = any(char.isdigit() for char in password)
if len(password) >= 8 and has_digit:
    print("Password meets the minimum conditions.")
else:
    print("Password must be at least 8 characters long and contain a digit.")


# Q26. Determine ticket price based on age category (sample prices).

age = int(input("Enter age: "))
if age < 0:
    print("Invalid age.")
elif age < 5:
    print("Ticket price: Free")
elif age <= 17:
    print("Ticket price: Rs. 100")
elif age <= 59:
    print("Ticket price: Rs. 200")
else:
    print("Ticket price: Rs. 120")


# Q27. Calculate discount based on purchase amount (sample slabs).

amount = float(input("Enter purchase amount in Rs.: "))
if amount < 0:
    print("Amount cannot be negative.")
else:
    if amount >= 5000:
        discount_rate = 0.20
    elif amount >= 3000:
        discount_rate = 0.15
    elif amount >= 1000:
        discount_rate = 0.10
    else:
        discount_rate = 0
    discount = amount * discount_rate
    final_amount = amount - discount
    print("Discount: Rs.", round(discount, 2))
    print("Amount to pay: Rs.", round(final_amount, 2))


# Q28. Check driving licence eligibility using age and eyesight condition (practice example).

age = int(input("Enter age: "))
eyesight_ok = input("Does your eyesight meet the required standard? (yes/no): ").strip().lower()
if age >= 18 and eyesight_ok == "yes":
    print("You meet these basic practice conditions.")
elif age < 18:
    print("You do not meet the minimum age condition.")
elif eyesight_ok != "yes":
    print("You do not meet the eyesight condition.")
else:
    print("Please enter yes or no for eyesight.")


# Q29. Create a login system with username and password validation (practice credentials).

correct_username = "student"
correct_password = "python123"
username = input("Enter username: ")
password = input("Enter password: ")
if username == correct_username and password == correct_password:
    print("Login successful.")
elif username != correct_username and password != correct_password:
    print("Incorrect username and password.")
elif username != correct_username:
    print("Incorrect username.")
else:
    print("Incorrect password.")


# Q30. Create a menu-driven program using if-elif-else.

while True:
    print("CALCULATOR MENU")
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")
    choice = input("Enter your choice (A-E): ").strip().upper()

    if choice == "E":
        print("Calculator closed. Goodbye!")
        break
    elif choice in ("A", "B", "C", "D"):
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if choice == "A":
            print("Result:", a + b)
        elif choice == "B":
            print("Result:", a - b)
        elif choice == "C":
            print("Result:", a * b)
        elif choice == "D":
            if b == 0:
                print("Cannot divide by zero.")
            else:
                print("Result:", a / b)
    else:
        print("Invalid choice. Please select A, B, C, D, or E.")