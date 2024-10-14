a = float(input())

# convert the amount to cents
remainingAmount = int(a * 100)


# find the number of one dollars
dollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

#find the number of quaters
quaters = remainingAmount // 25
remainingAmount = remainingAmount % 25

#find the number of dimes 
dimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

#find the number of nickels
nickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

#find the number of pennies
pennies = remainingAmount

print("Your amount", a, 'consists of'),
print(" ",dollars,"dollars"),
print(" ",quaters, "quaters"),
print(" ",dimes,"dimes"),
print(" ",nickels,"nickels"),
print(" ",pennies,"pennies")