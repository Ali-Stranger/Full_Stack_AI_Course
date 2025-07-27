#q1 celsius to fahrenhite
# temp=int(input("enter temperature in celsius: "))
# var=9/5
# far=(temp*var)+32
# print(f"Temperature in Fahrenheit is {far}") 


#q2 Area of rectangle
# len=int(input("enter lenght: "))
# wid=int(input("enter width: "))
# var=len * wid
# print(f"Area of Rectangle is {var}")

#q3 Compound interest rate
# P=int(input("enter P: "))
# R=int(input("enter R: "))
# T=int(input("enter T: "))
# CI = P * (1 + R/100)**T - P
# print(f"Compound Interest is {CI:.2f}")


#q4 Perimeter of Rectangle
# len=int(input("enter lenght: "))
# wid=int(input("enter width: "))
# var= 2 *(len + wid)
# print(f"Perimeter of Rectangle is {var}")


#q5 Average of three numbers
# num1=int(input("enter 1st number: "))
# num2=int(input("enter 2nd number: "))
# num3=int(input("enter 3rd Number: "))

# average = (num1+num2+num3)/3
# print(f"Average is {average}")

#q6 Square and cube of number
# num1=int(input("enter  number: "))
# square = num1*num1
# cube = num1*num1*num1
# print(f"Square is {square}")
# print(f"Cube is {cube}")

#q7 equally distribute candies
# num1=int(input("enter  total number of students: "))
# num2=int(input("enter  total number of candies: "))
# dis= num2 // num1
# left= num2 % num1
# print(f"Each student will get: {dis}")
# print(f"leftover candies are: {left}")

#q8 porfit and loss
# cp=int(input("enter  cost price: "))
# sp=int(input("enter  selling price: "))
# if sp > cp:
#     profit = sp - cp
#     print(f"Profit: {profit}")
# elif cp > sp:
#     loss = cp - sp
#     print(f"Loss: {loss}")
# else:
#     print("No Profit No Loss")

#q9 averagr, total and percentage of 5 subjects

# sub1=int(input("enter 1st subject marks: "))
# sub2=int(input("enter 2nd subject marks: "))
# sub3=int(input("enter 3rd subject marks: "))
# sub4=int(input("enter 4th subject marks: "))
# sub5=int(input("enter 5th subject marks: "))

# total= sub3+sub2+sub1+sub4+sub5
# average = (sub1+sub2+sub3+sub4+sub5)/5
# percentage = (total / 500) * 100
# print(f"Average is {average}")
# print(f"Total is {total}")
# print(f"Percentage is {percentage}")

#q10 basic pay
# basic=int(input("enter  basic salary: "))
# hra = 0.20 * basic
# da = 0.15 * basic
# total_salary = basic + hra + da
# print(f"\nHRA: {hra}")
# print(f"DA: {da}")
# print(f"Total Salary: {total_salary}")

#q11 Age in months and days
# age=int(input("Enter your age in years: "))
# age_months = age * 12
# age_days = age * 365
# print("Your age in months is:", age_months)
# print("Your approximate age in days is:", age_days)

#q12 currency converter
# usdt=int(input("Enter amount in USDT: "))
# pkr=usdt*289
# print(f"The amounnt in PKR is: ", pkr  )

#q13 Sum of first n natural numbers
# n=int(input("Enter first n natural numbers to calculate their sum: "))
# sum = n * (n + 1) / 2
# print(f"The Sum is: ", sum  )


#q14 percentage of correct answers
# tq=int(input("Enter number of questions: "))
# cq=int(input("Enter number of correct questions: "))
# percent= (cq / tq) * 100
# print(f"The Percentage is: ", percent  )

# #q15 calculate speed
# distance=int(input("Enter distance: "))
# time=int(input("Enter time: "))
# speed = distance / time
# print(f"The Speed is: ", speed  )


#q16 calculate bmi
# weight=int(input("Enter weight: "))
# height=float(input("Enter height: "))
# BMI = weight / (height ** 2)
# print(f"The BMI is: ", BMI  )