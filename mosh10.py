price=10000
good_credit=True
#good_credit=False
if good_credit:
    #print("put down 10%")
    down_payment=0.1*price
else:
    down_payment=0.2*price
print(f"down_payment: ${down_payment}")                         