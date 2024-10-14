purchaseAmount = float(input("Enter purchase amount: "))

# Tax is 18%
tax = purchaseAmount * 0.18

print("Sales tax is ", int(tax * 100) / 100)
print("Total price is ",(int(tax * 100) / 100) + purchaseAmount)