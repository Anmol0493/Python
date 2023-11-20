# Print numbers using loop
# for i in range(10):
#     i += 1
#     print(i)

# for i in range(-11, -1):
#     i += 1
#     print(i)

# for i in range(5):
#     print(i)
# else:
#     print("Done")


# Print the number pattern
# i=1
# while i <= 10:
#     print(i)
#     i += 1

# row = int(input("Enter Number: "))
# for i in range(row, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()


# Calculate the sum of all numbers from 1 to a given number
# row = int(input("Enter Number: "))
# for i in range(1, row+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()
# # or
# s = 0
# x = int(input("Enter Number: "))
# for i in range(1, x+1):
#     s += i
# print(s)
# # or
# x = int(input("Enter Number: "))
# s = sum(range(1, x+1))
# print(s)


# Write a program to print multiplication table of a given number
# num = int(input("Enter Number: "))
# for i in range(1, 11):
#     x = num * i
#     print(f"{num} * {i} = {x}")


# Display numbers from a list using loop
# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#     if i > 500:
#         break
#     elif i > 150:
#         continue
#     elif i % 5 == 0:
#         print(i)


# Count the total number of digits in a number
# num = int(input("Enter Number: "))
# count = 0
# while num != 0:
#     num //= 10
#     count += 1
# print(count)


# Print list in reverse order using a loop
# list = [10, 20, 30, 40, 50]
# newList = reversed(list)
# for i in newList:
#     print(i)


# Write a program to display all prime numbers within a range
# a = int(input("Enter first number of range: "))
# b= int(input("Enter second number of range: "))
# primeList = []
# compositeList = []
# for i in range(a, b + 1):
#     if i % 2 != 0:
#         primeList.append(i)
#     else:
#         compositeList.append(i)
# print(f"Prime number List: {primeList}")
# print(f"Composite number list: {compositeList}")


# Display Fibonacci series up to 10 terms
# term = int(input("Enter term of number: "))
# num = [0,1]
# print("fibonacci series:")
# for i in range(1, term):
#     num.append(num[-2] + num[-1])
# for j in num:
#     print(j, end=" ")


# Find the factorial of a given number
# num = int(input("Enter the number: "))
# factorial = 1
# print(num, end="! = ")
# for i in range(num, 0 , -1):
#     factorial *= i
#     print(i , end=" * " if i > 1 else " ")
# print("= ", factorial)


# Reverse a given integer number
# num = int(input("Enter the number: "))
# print("Reversed number is:",str(num)[::-1])
# # or
# reversed_num = 0
# while num != 0:
#     digit = num % 10
#     reversed_num *= 10
#     reversed_num += digit
#     num //= 10
# print("Reversed number is:", reversed_num)


# Use a loop to display elements from a given list present at odd and even positions
# list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print("Odd positions: ")
# for i in list[0::2]:
#     print(i, end=" ")
# print()
# print("Even positions: ")
# for j in list[1::2]:
#     print(j, end=" ")


# Calculate the cube of all numbers from 1 to a given number
# num = int(input("Enter the number: "))
# for i in range(1, num+1):
#     print(f"Current number: {i} and the cube is {i*i*i}")


# Find the sum of the series upto n terms
# term = int(input("Enter the number of term: "))
# num = int(input("Enter the number less than 10: "))
# x = num
# sum_seq = 0
# for i in range(0, term):
#     print(num, end="")
#     if i < term -1:
#         print(" + ", end="")
#     sum_seq += num
#     num = num * 10 + x
# print(" =", sum_seq)


# Print the following pattern
# rows = int(input("Enter the number of rows: "))
# for i in range(0, rows, 1):
#     for j in range(0, i+1):
#         print("* ")
#     print("\r")
# for i in range(rows, 0, -1):
#     for j in range(0, i-1):
#         print("* ")
#     print("\r")
# # or
# for i in range(1, rows * 2):
#     if i <= rows:
#         print("* " * i)
#     else:
#         print("* " * (rows *2 - i))