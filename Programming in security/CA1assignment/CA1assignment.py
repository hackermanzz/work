import msvcrt as keyPress
from datetime import datetime
import sys
from datetime import date
import calendar
import csv
Menu_prices=[]
Menu_items=[]
cartItems=[]
cartPrices=[]
cost = 0
cartDict={}
# Declaration of global functions
def preMenuFunction():
    my_date = date.today()
    dateToday =calendar.day_name[my_date.weekday()]
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("\n\n\nCurrent Time =", current_time)# printing of real time
    print(dateToday)# printing of real date
    blank =''
    print(f'{blank:*^30}' + '\nWelcome to SPAM\n'+ f'{blank:*^30}')#Main Starting print
    return checkForWhichDay(dateToday)
# Function to make display the real time according to the computer's clock
def adminLogin():
    adminLoginChoice =''
    while adminLoginChoice == '':
        adminLoginChoice= input("\nDo you have an admin account? Enter 'yes' or 'no'\n>>")
        if adminLoginChoice == 'yes':
            with open('admin.txt' , 'r') as file:
                file_reader = csv.reader(file)
                user_find(file_reader)
                file.close()
        elif adminLoginChoice == 'no':
            adminLoginChoice = ''
            return registerForAdmin()
        else:
            adminLoginChoice ==''
# Fu1nction to open the file that contains the admin credentials
def user_find(file):
    user = input('Enter your username: \n')
    for row in file:
        if row[0] == user:
            print('username found', user)
            user_found = [row[0],row[1]]
            pass_check(user_found)
            break
        else:
            print("Not found")
# Function to crosscheck the text file with the
def pass_check(user_found):
    user = input('Enter your password: \n')
    if user_found[1]==user:
        print("password match")
        return adminRights()
    else:
        print("password not match")
# Function that checks the password of the given username
def registerForAdmin():
    with open('admin.txt' , 'a') as f:
        newAdminUserName = input("Please enter your new admin username\n>>")
        newAdminPassword = input("Please enter your new password\n>>")
        f.write(newAdminUserName + ',' + newAdminPassword + '\n')
    print("Successfully registered\n")
    return adminLogin()
# Function that allows the user to register for admin privileges which will be stored in a file
def adminRights():
    global Menu_items, Menu_prices
    adminInputFunction = input("What would you like to do ?\n1. Add Changes the menu\n2. Remove menu items\n>>")
    while adminInputFunction == '1' or adminInputFunction == '2':
        if adminInputFunction == '1':
            return AdminAdd()
        elif adminInputFunction == '2':
            return AdminRemove()
# Function that dictates what the admin user can do while having these privileges
def AdminAdd():
    global Menu_items, Menu_prices
    remove_or_add = input("Would you like to add or remove items : \n1.Add menu items\n2.Remove Menu prices \n>>")
    if remove_or_add == '1':
        items_to_add = input('Enter the name of the menu items that you would want to add to the menu: ').lower()
        Prices_to_add = int(input('Enter the price of the item that you wish to add'))
        Menu_items.append(items_to_add)
        Menu_prices.append(Prices_to_add)
        print(Menu_items ,' with price ' , Menu_prices)
    elif remove_or_add == '2':
        choicesToRemove = input('Items that are on display today :' , Menu_items , '\n Please enter the index of the item that you would want to remove : ')
        discountinued_items = Menu_items.pop(Menu_items[choicesToRemove])
        print('This are the items that were removed' , discountinued_items)
    elif remove_or_add == '':
        return None
    else: 
        print("Sorry that is not one of the choices")
# Function that allows the admin to modify and add changes to the menu
def AdminRemove():
    global Menu_prices,Menu_items
    remove_or_add = input("Would you like to add or remove items : \n1.Add menu items\2.Remove Menu Items \n>>")
    if remove_or_add == '1':
        items_to_add = input('Enter the menu items that you would want to add to the menu: ').lower()
        Menu_prices.append(items_to_add)
    elif remove_or_add == '2':
        choicesToRemove = input('Items that are on display today :' , Menu_items , '\n Please enter the index of the item that you would want to remove : ')
        discountinued_items = Menu_items.pop(Menu_items[choicesToRemove])
        print('This are the items that were removed' , discountinued_items)
    elif remove_or_add == '':
        return None
    else: 
        print("Sorry that is not one of the choices")
# Function that allows the admins user to be able to modify and add changes to the prices of the menu items
def inputFunction():
    choice = ''
    adminLoginOrNot = ' '
    while adminLoginOrNot != '':
        adminLoginOrNot = input(' Would you like to login as an admin "yes" or "no"\n>>').lower()
        if adminLoginOrNot == 'yes':
            adminLoginOrNot = ''
            return adminLogin()
        elif adminLoginOrNot == 'no':
            adminLoginOrNot = ''
        else:
            print("Please enter a valid choice")
            adminLoginOrNot =' '
    while choice =='':
        choice = input("1. Display Today's Menu\n2. Search Menu\n3. Display Cart\n4. Check Out\n \n Please input your choice of action(ENTER to exit)\n:")
        if choice =='1':
            return displayMenu()
        elif choice == '2':
            return searchMenu()
        elif choice == '3':
            return displayCart()
        elif choice == '4':
            return preCheckOut()
        elif choice == '':
            print('Goodbye!')
        else:
            print('Please enter a valid choice')
            choice = ''
# Initial input function for the user to navigate the menu system
def waitForPressedKey():
    keyPress.getch()
# Custom Function to make the 'Please enter any key to continue,' function
def displayMenu():
    global Menu_items,Menu_prices
    print(f"Today's Menu".center(24,'-')+"\n"+Menu_items[0]+"\t"+"$"+str(Menu_prices[0])+"\n"+Menu_items[1]+"\t"+"$"+str(Menu_prices[1])+"\n"+Menu_items[2]+"\t"+"$"+str(Menu_prices[2])+"\n"+Menu_items[3] + "\t$" + Menu_prices[3]+"\nEnter any key to continue...")
    waitForPressedKey()
    choice = ''
    while choice != ' ':
        choice= input("\nWould you like to order anything? Enter 'yes' or 'no'\n>>").lower()
        if choice == 'yes':
            choice = ' '
            return addToCart()
        elif choice == 'no':
            choice = ' '
            return inputFunction()
        else:
            print("That is not a valid choice")
# Function that display the menu and allows the customer to add items to cart
def addToCart():
    global Menu_items,Menu_prices,cartItems,cartPrices
    user_add_to_cart=' '
    while True:
        user_add_to_cart = input('\nPlease enter the index of the item that you want to add to cart\n>>')
        for items in Menu_items:
            indexes_for_reference = (Menu_items.index(items)) +1
            if user_add_to_cart  == f'{indexes_for_reference}':
                cartItems.append(Menu_items[indexes_for_reference-1])
                cartPrices.append(Menu_prices[indexes_for_reference-1])
                print('\n~'+Menu_items[indexes_for_reference-1]+ ' has been added to your cart~\n')
                fail = False
                break
            else:
                fail = True
        if fail !=False :
            print('Please enter a valid choice')
        if user_add_to_cart=='':
            if len(cartItems) == 0:
                print(cartItems)
                emptyList=input('You have nothing in your Cart would you like to browse the menu again? Type "yes" to display Menu again or press "Enter" to exit?').lower()
                while True:
                    if emptyList == 'yes':
                        return displayMenu()
                    elif emptyList == '':
                        print("moving back to the Main Menu")
                        displayMenu()
                        break
                    else:
                        print('Please enter a valid choice')
                        continue
            else:
                return displayCart()
# Function that allows the user to be able to add items from the menu to the cart
def searchMenu():
    global Menu_items
    print("Search Menu".center(24,'-'))
    userSearch= input('Enter the keyword of the dishes that you would want to find\n>>')
    find = 0
    for items in Menu_items:
        if userSearch.lower() in items:
            print(items)
            find = 1
    if find == 0:
        print("Sorry we could'nt find the dishes you were looking for")
        print("Enter any key to continue...")
        waitForPressedKey()
        return searchMenu()
    displayMenu()
# Function that allows the user to be able to search for specific items in the menu
def displayCart():
    global cartItems,cartPrices,cost
    cost = 0
    for items in cartItems:
        index_for_price_cart = cartItems.index(items)
        print(items ,'\t:\t$', cartPrices[index_for_price_cart])
        
    for prices in cartPrices:
        cost += float(prices)
    
    confirmItems= input(f'\n This are the items you have in your cart.\n Press "Y" to proceed to the check out or "N" continue browsing \n Total Cost : ${cost}0\n>>').lower()
    if confirmItems == 'y':
        return preCheckOut()
    elif confirmItems == 'n':
        return displayMenu()
# Function that prints out the current items in the cart and confirms if the user wants to continue browsing or proceed to check out
def preCheckOut():
    global cartItems, cartPrices, cartDict
    remove_items_from_cart = ' '
    while remove_items_from_cart != 'no':
        remove_items_from_cart = input("Would you like to remove anything from your cart? \n1. yes\n2. no\n>>").lower()
        if remove_items_from_cart == 'yes':
            index_to_remove_from_cart = input('Please enter the index of the item that you would like to remove\n>>')
            for items in cartItems:
                if index_to_remove_from_cart =='1' or index_to_remove_from_cart =='2' or index_to_remove_from_cart =='3' or index_to_remove_from_cart =='4':# find the user input in the cartItems
                    print(items , 'with the price' , cartPrices[eval(index_to_remove_from_cart)-1], 'has been removed \n')
                    item_remove_index = eval(index_to_remove_from_cart)-1
                    cartItems.remove(cartItems[item_remove_index])
                    cartPrices.remove(cartPrices[item_remove_index])
                    print(cartItems, '\n')
                    index_to_remove_from_cart = ''
        elif remove_items_from_cart == 'no':
            print("Proceeding to check out")
            return checkOut(cartItems,cartPrices)
# Function that allows the user to remove unwanted items from cart / which also removes the price from the price list
def checkOut(cartItems , cartPrices):
    global cost
    print("Checking Out".center(24,'-'))
    for items in cartItems:
        index_of_items = cartItems.index(items)
        print(items , '\t:\t$' , cartPrices[index_of_items])
    paymentTypes= input('\n These are the items that you have selected, What type of payment would you like to proceed with?\n1. Cash payment\n2. NETS payment\n3. Credit card / Debit card\n4. Bit-Coins')
    discountType= input('Are you one of the following?\n1. member\n2. premium member\n3. Senior Citizen\n4. Staff \n Enter "no" if you are not registered for any of them').lower()
    if discountType == '1':# If statement to determine whether the user has any type of membership
        cost = (cost /100)*90
        print('The membership that you have chosen is : member')
    elif discountType == '2':
        cost = (cost /100)*75
        print('The membership that you have chosen is : premium member')
    elif discountType == '3':
        cost = (cost /100)*85
        print('The membership that you have chosen is : Senior Citizen')
    elif discountType == '4':
        cost = (cost /100)*70
        print('The membership that you have chosen is : Staff')
    elif discountType == 'no':
        print('The membership that you have chosen is : none')
    while paymentTypes != '':# If statement that determines the type of payment that the user will be using
        if paymentTypes =='1':
            cashPaidByCustomer = int(input('Please enter the amount of cash that you are paying with\n>>'))
            verify = 0
            while verify == 0:
                if cashPaidByCustomer >  cost:
                    change = cashPaidByCustomer-cost
                    print(f'This is your change : ${change}\n Thank you for shopping with us')
                    verify = 1
                    paymentTypes = ''
                elif cashPaidByCustomer == cost:
                    print('Payment recieved and verified, thank you for shopping with us!')
                    verify = 1
                    paymentTypes = ''
                else:
                    amountShort = cost - cashPaidByCustomer
                    print(f"Sorry the amount you provided was not enough, You are short of {amountShort}")
        if paymentTypes =='2':
            print('Please enter you card:')
            waitForPressedKey()
            PINnumber = int(input('Please enter your pin number'))
            while verify ==0:
                if PINnumber >1:
                    print('Your payment was recieved and verified, Thank you for shopping with us')
                    verify = 1
                    paymentTypes = ''
                else:
                    print('Please enter your pin again')
# Function that allows the users to pay and also allow the usages of discounts
def checkForWhichDay(dateToday):
    iteratingList = ['Monday','Teusday','Wednesday','Thursday','Friday','Saturday','Sunday']
    for days in iteratingList:
        if dateToday in days:
            with open(f"menu{days}.txt" , "r") as f:
                menu = f.read()
                with open(f"price{days}.txt" , 'r') as e:
                    prices = e.read()
            return stripAndPutIntoLists(menu , prices)
# Function that cross check with real time
def stripAndPutIntoLists(menu ,prices):
    global cartDict,Menu_items,Menu_prices
    menu_ready = (menu.strip()).split(sep=',')
    prices_ready = (prices.strip()).split(sep=',')
    for item in menu_ready:
        Menu_items.append(item)
    for price in prices_ready:
        Menu_prices.append(price)
    return Menu_prices, Menu_items
preMenuFunction() 
inputFunction()