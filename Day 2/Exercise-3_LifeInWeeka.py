# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


day = 90 * 365
weeks = 90 * 52
months = 90 * 12
a = day - int(age) * 365
b = weeks - int(age) * 52
c = months - int(age) * 12

#You have 12410 days, 1768 weeks, and 408 months left.

print(f"You have {a} days, {b} weeks, and {c} months left.")

