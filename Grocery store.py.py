#Grocery store item list
#prices are followed by category names
product=["Oil","Soft drinks","Chocholate","Tooth paste","Noodles"]
catagory=[{"Emami":150,"Patanjali":140,"Saffola":155},{"Pepsi":95,"Coca cola":90,"Thumps up":95},{"Dairy milk": 160, "Kit kat": 120, "Perk": 70},{"Colgate":50,"Pepsodent":45,"Closeup":40},{"Maggi":60,"Yipiee":60,"Chings":55}]
cart=[]
price=[]
qnt=[]
while(1):
  x=input("press y to enter items into cart or press n to exit").lower()
  if x=="n":
    break
  if x=="y":
    print("Our store has following product please select  :")
    for a in product:
      print(a)
    p=input("Enter the product name").capitalize()
    indx=product.index(p)
    for a,b in catagory[indx].items():
      print(a,":",b)
    item=input("Please enter the catagory name").capitalize()
    qnty=int(input("Please enter the quantity??"))
    cart.append(item)
    price.append(catagory[indx][item]*qnty)
    qnt.append(qnty)
print(cart,price)
print("**************Your total bill is**************")
for a in range(len(cart)):
  print(qnty,"*",cart[a],"price =", price[a])
print("TOTAL amount Rs : ",sum(price))    
    
  
      