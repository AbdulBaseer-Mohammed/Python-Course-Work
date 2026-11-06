'''
l=[12,9,3,4,5,10,2,4,5,2,4,5]

i =0
j = len(l)-1

while i<=j:
    if i==j:
        print(l[i])
    else:
        print(l[i]+l[j])
    i+=l
    j-=l 
 
   '''
'''
bill = 0

while True:
    product = input("Enter the product name: ")
    if product == 'STOP':
        print("Total Bill:",bill)
        break
    price = int(input("Enter the price"))
    quantity = int(input("Enter the quantity:"))
    bill+=price*quantity
    '''
'''
print(" ABC SUPER MARKET ")

name = input("Enter Customer Name: ")

item1 = input("Enter Item 1 Name: ")
price1 = float(input("Enter Item 1 Price: "))
qty1 = int(input("Enter Item 1 Quantity: "))

item2 = input("Enter Item 2 Name: ")
price2 = float(input("Enter Item 2 Price: "))
qty2 = int(input("Enter Item 2 Quantity: "))

total1 = price1 * qty1
total2 = price2 * qty2

total = total1 + total2

if total >= 1000:
    discount = total * 0.10
else:
    discount = 0

final_amount = total - discount

print("\n========== CUSTOMER BILL ==========")
print("Customer Name:", name)

print("-----------------------------------")
print("Item       Price    Qty    Amount")
print("-----------------------------------")

print(item1, price1, qty1, total1)
print(item2, price2, qty2, total2)

print("-----------------------------------")
print("Total Amount:", total)
print("Discount:", discount)
print("Final Amount:", final_amount)
print("-----------------------------------")
print("Thank You! Visit Again!")
'''
'''
print("================================")
print("         ABC RESTAURANT")
print("================================")

name = input("Enter Customer Name: ")

print("\n----------- FOOD MENU -----------")
print("1. Chicken Biryani - Rs.250")
print("2. Mutton Biryani  - Rs.300")
print("3. Veg Biryani     - Rs.180")
print("4. Chicken 65      - Rs.200")
print("5. Fried Rice      - Rs.150")
print("--------------------------------")

choice = int(input("Enter Food Choice: "))
quantity = int(input("Enter Quantity: "))

if choice == 1:
    item = "Chicken Biryani"
    price = 250
elif choice == 2:
    item = "Mutton Biryani"
    price = 300
elif choice == 3:
    item = "Veg Biryani"
    price = 180
elif choice == 4:
    item = "Chicken 65"
    price = 200
elif choice == 5:
    item = "Fried Rice"
    price = 150
else:
    print("Invalid Food Choice!")
    exit()

total = price * quantity

print("\n================================")
print("          CUSTOMER BILL")
print("================================")
print("Restaurant : ABC Restaurant")
print("Customer   :", name)
print("--------------------------------")
print("Food Item  :", item)
print("Price      : Rs.", price)
print("Quantity   :", quantity)
print("--------------------------------")
print("Total Bill : Rs.", total)
print("================================")
print("       THANK YOU!")
print("       VISIT AGAIN!")
print("================================")
'''

Products = {
  'sugar':40,
  'salt':30,
  'cooking oil':120,
  'bread':40,
  'weed':32,
 }

  #Display Menu
print("Welcome to the store".center(50,'-'))
print("Product Name",'Price')
for i in Products:
      print(i.ljust(12,' '),':',product[i])
      



      carts ={} 
      while True:
        cart = input("Enter the product Name(exit):").lower()
        if cart =='exit':
          break
        qua = int(input("Enter the quality: "))
        carts[cart]=qua


print("Bill".center(50,'-'))
print('Product Name Quantity ($)Price')  
bill=0
for i in carts:
    print(i.ljust(12,' '),str(carts[i]).ljust(12,' '),products[i])
    bill +=  carts[i]*products[i]

    print(f"Total  bill: ${bill}")
    print("Thanks for shopping")               


