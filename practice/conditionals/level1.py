# 1. Check if a number is positive, negative, or zero.


# num = int(input("Please Enter number "))

# if num < 0 :
#     print("Negative", num)
# elif num > 0 :
#     print("Positive", num)
# else :
#     print("Zero", num)


# 2. Check if a number is even or odd.

# checkNumber = int(input("Please Enter number :- "))

# if checkNumber % 2 == 0 :
#     print("Even", checkNumber)
# else :
#     print("Odd")


# 3. Find the greatest of two numbers.

# numOne = int(input("Please Enter Number One :- "))
# numTwo = int(input("Please Enter Number Two :- "))
# if numOne > numTwo : 
#     print("Number One is Greatest")
# else :
#     print("Number Two is Greatest")


# 4. Find the greatest of three numbers.
# numberOne = int(input("Please Enter Number One :- "))
# numberTwo = int(input("Please Enter Number Two :- "))
# numberThree = int(input("Please Enter Number Three :- "))


# if numberOne > numberTwo and numberOne > numberThree :
#     print("Number One is Greatest", numberOne)
# elif numberTwo > numberOne and numberTwo > numberThree : 
#     print("Number Two is Greatest", numberTwo)
# else :
#     print("Number Three is Greatest", numberThree)


# 5. Check if a year is a leap year.

# year = int(input("Please Enter Year :- "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
#     print("This is a leap year", year)
# else :
#     print("This is not a leap year", year)

# 6. Check if a person is eligible to vote (age ≥ 18).

# age = int(input("Please Enter Your Age :- "))
# if age < 18 : 
#     print("You're not eligible for vote", age)
# else :
#     print("You're eligible for vote", age)

# 7. Check if a number is divisible by both 3 and 5.
# num = int(input("Please Enter Number :- "))
# if num % 3 == 0 and num % 5 == 0 :
#     print("This number is divisible by 3 and 5", num)
# else :
#     print("This number is not divisible by 3 and 5", num)

# 8. Check if a character is a vowel or consonant.
# username = input("Please Enter a username :- ")
# if username == "a" or "e" or "i" or "o" or "u" :

# 9. Check if a number is a multiple of 7 or not.
# number = int(input("Please Enter Number :- "))
# if number % 7 == 0 :
#     print("This number is divisible by 7 ", number)
# else : 
#     print("This number is not divisible by 7 ", number)


# 10. Create a simple calculator using if-else (+, -, *, /).

numOne = int(input("Please Enter a Number One :- "))
operators = input("Please Enter a Operators :- ")
numTwo = int(input("Please Enter a Number Two :- "))

if operators == "+" :
    print(numOne + numTwo)
elif operators == "-" :
    print(numOne - numTwo)
elif operators == "*" : 
    print(numTwo * numOne)
else : 
    print(numOne / numTwo)