#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number>=0:
	Sn=number%10
else:
	Sn=(number%10)-10

if Sn>5 :
	print(f"Last digit of {number} is {Sn} is greater than 5")
elif Sn==0:
	print(f"Last digit of {number} is {Sn} and is 0")
elif Sn<6 and  Sn!=0 :
	print(f"Last digit of {number} is {Sn} and is less than 6 and not 0")
