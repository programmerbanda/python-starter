# 1. Print numbers from 1 to 100.

# for x in range(1, 101):
#     print(x)

# 2. Print even numbers from 1 to 100.

# for num in range(1, 101):
#     if num % 2 == 0 :
#         print(num)

# 3. Print odd numbers from 1 to 100.

# for num in range(1, 101) :
#     if num % 2 != 0:
#         print(num)

# 4. Print multiplication table of a number.

num = int(input("Please Enter Number ? "))

for i in range(1, 11) :
    print(f"{num} * {i} = {num * i}")
    print(num, "*", i, "==", num * i)
