#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
	lastDigit = abs(number)
	lastDigit = lastDigit % 10
	lastDigit *= -1
else:
	lastDigit = number % 10
print("Last digit of {} is {}".format(number, lastDigit), end= " ")
if lastDigit > 5:
	print("and is greater than 5")
elif lastDigit == 0:
	print("and is 0")
elif lastDigit < 6 and not 0:
	print("and is less than 6 and not 0")
