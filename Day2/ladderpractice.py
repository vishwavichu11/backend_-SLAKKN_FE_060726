amount=float(input("Enter your Amount:"))

if amount>=5000:
    discount = amount*0.20
    Total_bill=amount-discount
    print("congratulations you got 20% discount and Total bill is",Total_bill)
elif amount>=3000 and amount<=5000:
    discount=amount*0.15
    Total_bill=amount-discount
    print("congratulations you got 15% discount and Total bill is",Total_bill)
elif amount>=2000 and amount<=3000:
    discount=amount*0.10
    Total_bill=amount-discount
    print("congratulations you got 10% discount and Total bill is",Total_bill)
elif amount<=2000:
    discount=0
    print("Sorry  No discount available")
else:
    discount=0
    print("invalid")

   
  
    
