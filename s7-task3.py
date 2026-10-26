total = float(input("Enter your zomato order total: "))

if total > 299 :
    print("Apply free delivery")

elif total >= 200 :
    print("Add more items for free delivery")

else :
    print("Delivery charges apply")