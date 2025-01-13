#mini cafe project using python 
print("Welcome to Caa Cafe")
menu={
    "coffee":80,
    "tea":40,
    "maggie":40,
    "juice":70,
    "coldrink":90
}
print("Here is Menu For You Sir | Madam")
print(menu)
order_total=0
order1=input("what would you like to order:")
if order1 in menu:
    order_total+=menu[order1]
    print("Your bill is :",order_total)
else:
    print("Sorry Not Available ")

order2=input("You want something else (Yes/No)")    
if order2=="Yes":
    order2x=input("Add in your Order please:")
    if order2x in menu:
        order_total+=menu[order2x]
        print("Your bill is :",order_total)
    else:
        print("Sorry Not Available:")
else:
    print("Ok Thanku")

if order_total>0:
    print("You will recieve your order soon")
    print("Your Total Bill is:",order_total)
else:
    print("You Ordered Nothing")

print("Thanks for Visiting Caa Cafe")    

