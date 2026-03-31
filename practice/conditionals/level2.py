# 1. Find grade based on marks:

# 90+ → A
# 75–89 → B
# 50–74 → C
# below 50 → Fail

# studentMarks = int(input("Please Enter Your Marks ? "))
# if studentMarks >= 90 and studentMarks <= 100:
#     print("You got A", studentMarks)
# elif studentMarks >= 75 and studentMarks < 89:
#     print("You got B", studentMarks)
# elif studentMarks >= 50 and studentMarks < 74:
#     print("You got C", studentMarks)
# else :
#     print("Sorry You're Fail", studentMarks)


# 2. Check if a number is a palindrome.

num = int(input("Please Enter Number ? "))
convertedNumber = str(num)
print(type(convertedNumber))
if num == convertedNumber :
    print("This is Palindrome ", num)
else :
    print("This is not Palindrome", num)