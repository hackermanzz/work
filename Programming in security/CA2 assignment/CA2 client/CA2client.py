# Enter 3 to enter the admin Login feature.
# username and password :admin
import socket
import msvcrt as keypress
import re
import time
blank = ''
cartItems = []
cartPrices = []
totalPrice = 0
def menuPreparation():
    global cartItems , cartPrices
    print('====================================================')
    msg = input("Hello and Welcome to the SPAM 2.0\nPlease state whether you would like to\n1.Same day delivery\n2.Catering\n >>")
    while True:
        if msg == '1':
            buf = msg.encode()
            clientsocket.sendall(buf)
            menu = clientsocket.recv(255)
            decodedMenu = menu.decode()
            combinedList = decodedMenu.split(sep=',')
            lengthOfList = int(len(combinedList)/2)
            menuItems = combinedList[:lengthOfList]
            menuPrices = combinedList[lengthOfList:]
            clientsocket.close()
            return mainMenuNavigation(menuItems,menuPrices)
        elif msg == '2':
            buf = '2'
            clientsocket.send(buf.encode())
            print('====================================================')
            msg = input("Which day would you like to order for?\n1.Monday\n2.Tuesday\n3.Wednesday\n4.Thursday\n5.Friday\n6.Saturday\n7.Sunday\n>>").lower()
            while True:
                if msg == '1' or msg == 'monday':
                    day = 'monday'
                    clientsocket.send(day.encode())
                    return Preorder()
                elif msg == '2' or msg == 'tuesday':
                    day = 'tuesday'
                    clientsocket.send(day.encode())
                    return Preorder()
                elif msg == '3' or msg == 'wednesday':
                    day = 'wednesday'
                    clientsocket.send(day.encode())
                    return Preorder()
                elif msg == '4' or msg == 'thursday':
                    day = 'thursday'
                    clientsocket.send(day.encode())
                    return Preorder()
                elif msg == '5' or msg == 'friday':
                    day = 'friday'
                    clientsocket.send(day.encode())
                    return Preorder()
                elif msg == '6' or msg == 'saturday':
                    day = 'saturday'
                    clientsocket.send(day.encode())
                    return Preorder()
                elif msg == '7' or msg == 'sunday':
                    day = 'sunday'
                    clientsocket.send(day.encode())
                    return Preorder()
                else:
                    print('Please enter a valid choice')
                    msg = input("Which day would you like to order for?\n1.Monday\n2.Tuesday\n3.Wednesday\n4.Thursday\n5.Friday\n6.Saturday\n7.Sunday\n>>").lower()
        elif msg == '3':
            msgEncoded = msg.encode()
            clientsocket.send(msgEncoded)
            return adminLogin()
        else:
            print("Please enter a valid choice")
            msg = input("Hello and Welcome to the SPAM 2.0\nPlease state whether you would like to\n1.order\n2.advance booking\n >>")
def Preorder():
    preorderMenu = clientsocket.recv(255)
    menuPrep = preorderMenu.decode()
    combinedList = menuPrep.split(sep=',')
    lengthOfList = int(len(combinedList)/2)
    menuItems = combinedList[:lengthOfList]
    menuPrices = combinedList[lengthOfList:]
    clientsocket.close()
    return printMenu(menuItems,menuPrices)
def getnewsocket():
	return socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def waitForPressedKey():
    keypress.getch()
def mainMenuNavigation(items,prices):
    global cartItems , cartPrices
    choice = ''
    while choice =='':
        choice = input("1. Display Today's Menu\n2. Search Menu\n3. Display Cart\n4. Check Out\n \n Please input your choice of action('X' to exit)\n:").lower()
        if choice =='1':
            return printMenu(items,prices)
        elif choice == '2':
            return searchMenu(items, prices)
        elif choice == '3':
            return displayCart(items, prices)
        elif choice == '4':
            return preCheckOut(cartItems, cartPrices)
        elif choice == 'x':
            print("Goodbye!")
            clientsocket.close()
        else:
            print('Please enter a valid choice')
            choice = ''
def printMenu(items, prices):
    global blank
    print('====================================================')
    print("Here is the menu for today: \n")
    for item in items:
        index = items.index(item)
        print(f"{item.capitalize()}\t:\t${(prices[index])}.00")
    proceed = input("\nWould you like to start ordering?\n1.Yes\n2.No\n>>").lower()
    while True:
        if proceed == '1' or proceed == 'yes':
            return addToCart(items,prices)
        elif proceed == '2' or proceed == 'no':
            print("Returning back to the main menu")
            return mainMenuNavigation(items,prices)
        else:
            print("Please enter a valid choice")
            proceed = input("\nWould you like to start ordering?\n1.Yes\n2.No\n>>").lower()
def searchMenu(items,prices):
    print("Search Menu".center(24,'-'))
    userSearch = input('Enter the keyword of the dishes that you would want to find\n>>')
    find = 0
    for item in items:
        if userSearch.lower() in item:
            print(item)
            find = 1
    if find == 0:
        print("Sorry we could'nt find the dishes you were looking for")
        print("Enter any key to continue...")
        waitForPressedKey()
        return searchMenu(items,prices)
    print("Returning back to the Main Menu ...")
    mainMenuNavigation(items,prices)            
def addToCart(items,prices):
    print('====================================================')
    user_add_to_cart=' '
    fail = True
    while True:
        user_add_to_cart = input('Please enter the index of the item that you want to add to cart\n(Press ENTER to proceed)\n>>')
        for item in items:
            indexes_for_reference = (items.index(item)) +1
            if user_add_to_cart  == f'{indexes_for_reference}':
                cartItems.append(items[indexes_for_reference-1])
                cartPrices.append((prices[indexes_for_reference-1]))
                print('\n====================================================\n~'+ items[indexes_for_reference-1] + '~ \nhas been added to your cart\n====================================================')
                fail = False
                break
            else:
                fail = True
        if fail !=False :
            print('Please enter a valid choice')
        if user_add_to_cart=='':
            if len(cartItems) == 0:
                emptyList=(input('Your cart is empty, Would you like to add items to cart?\n1.Yes\n2.No\n>>').lower()).strip()
                while True:
                    if emptyList == 'yes' or emptyList =='1':
                        return printMenu(items,prices)
                    elif emptyList == '2' or emptyList == 'no':
                        print("moving back to the Main Menu")
                        return printMenu(items,prices)
                    else:
                        print('Please enter a valid choice')
            else:
                return displayCart(items,prices)
def displayCart(items,prices):
    global cartItems , cartPrices
    print("Here are the items that you have added:\n")
    print('====================================================')
    for items in cartItems:
        print(items)
    print('====================================================')
    userToPay = input("Would you like to proceed to the check out?\n1.Yes\n2.No\n>>")
    while True:
        if userToPay == '1' or userToPay.lower() == 'yes':
            print("Proceeding to check out ...")
            return preCheckOut(cartItems , cartPrices)
        elif userToPay == '2' or userToPay.lower() == 'no':
            print('Returning back to the main menu ...')
            return mainMenuNavigation(items , prices)
        else:
            userToPay = input("Would you like to proceed to the check out?\n1.Yes\n2.No\n>>")
def preCheckOut(cartItems,cartPrices):
    print('====================================================')
    checkOutCartPrices = []
    for priceTag in cartPrices:
        price = int(priceTag)
        checkOutCartPrices.append(price)
    totalPrice = round(sum(checkOutCartPrices),2)
    discount = input("Do you have any of the discounts?\n1.SPAM membership\n2.Senior Citizen\n3.SP student\n4.None\n>>")
    while True:
        if discount == '1':
            print("Please scan your membership card") 
            waitForPressedKey()
            totalPrice = (totalPrice/100 )*80
            print(f"Your amount payable is ${totalPrice}")
        elif discount == '2':
            print("Please scan your senior citizen card")
            waitForPressedKey()
            totalPrice = (totalPrice/100)*75
            print(f"Your amount payable is ${totalPrice}")
        elif discount == '3':
            print("Please scan your student ID card")
            waitForPressedKey()
            totalPrice = (totalPrice/100)*85
            print(f"Your amount payable is ${totalPrice}")
        elif discount == "4":
            print(f"Your amount payable is ${totalPrice}")
        else:
            print("Please enter a valid choice")
            discount = input("Do you have any of the discounts?\n1.SPAM membership\n2.Senior Citizen\n3.SP student\n>>")
        return checkOut(totalPrice,cartItems)
def checkOut(totalPrice, cartItems):
    print('====================================================')
    paymentMethods = input("Choose one of the payment method\n1.Cash\n2.PayLah/PayNow\n3.NETS\n>> ").lower()
    while True:
        if paymentMethods == '1':
            clientPay = input(f"Total cost  :   ${round(totalPrice,2)}\nEnter the amount that you are paying:\n>>")
            if clientPay.isnumeric():
                if int(clientPay)>int(totalPrice):
                    change = int(clientPay) - int(totalPrice)
                    print(f"Thank you for shopping with us! This is your change:\nChange: {change}")
                    return fileLogging(totalPrice,cartItems)
                elif int(clientPay) == int(totalPrice):
                    print(f"Thank you for shopping with us")
                    return fileLogging(totalPrice,cartItems)
                elif int(clientPay)<int(totalPrice):
                    short = int(totalPrice) - int(clientPay)
                    print(f"Sorry the amount that you gave is not enough. Please enter again\nYou are short: {short}")
                    clientPay = input("Please enter the amount that you are payment\n>>")
        if paymentMethods == '2':
            print('Please scan the QR code')
            waitForPressedKey()
            print(f"Thank you for shopping with us")
            return fileLogging(totalPrice,cartItems)
        if paymentMethods == '3':
            PIN = input("Please enter your PIN number")
            if len(PIN) > 7:
                print("Approved.")
                waitForPressedKey()
            print(f"Thank you for shopping with us")
            return fileLogging(totalPrice,cartItems)
        else:
            print("please enter a valid choice")
            paymentMethods = input("Choose one of the payment method\n1.Cash\n2.PayLah/PayNow\n3.NETS\n>> ").lower()
    return fileLogging(totalPrice,cartItems)
def fileLogging(price,cartItems):
    global host,clientsocket
    clientBought = ''
    clientsocket = getnewsocket()
    host = 'localhost'
    clientsocket.connect((host ,8089))
    msg = 'file'
    encodedMsg = msg.encode()
    clientsocket.send(encodedMsg)
    time.sleep(2.5)
    clientsocket.send(str(price).encode())
    time.sleep(2.5)
    for items in cartItems:
        clientBought = clientBought+items+'\n'
    clientsocket.send(clientBought.encode())
def adminLogin():
    adminUsername = input("Enter your username: ")
    adminPassword = input("Enter your password: ")
    combined = (adminPassword+','+adminUsername).encode()
    clientsocket.send(combined)
    time.sleep(2.5)
    approval = clientsocket.recv(255)
    if approval.decode() == 'yes':
        clientsocket.close()
        return adminRights() #allows access to the admin rights
    else:
        print("invalid credentials")
        return menuPreparation()
def adminRights():
    clientsocket = getnewsocket()
    host = "localhost"
    clientsocket.connect((host, 8089))
    msg = '1'
    clientsocket.send(msg.encode())
    time.sleep(1)
    menu = clientsocket.recv(255)
    decodedMenu = menu.decode()
    combinedList = decodedMenu.split(sep=',')
    lengthOfList = int(len(combinedList)/2)
    menuItems = combinedList[:lengthOfList]
    menuPrices = combinedList[lengthOfList:]
    adminChoice = input("Admin Rights:\n1.Add items\n2.Remove items\n>>")
    while True:
        if adminChoice == '1':
            clientsocket.send(adminChoice.encode())
            return adminAdd(menuItems , menuPrices)
        elif adminChoice == '2':
            clientsocket.send(adminChoice.encode())
            return adminRemove(menuItems , menuPrices)
        else:
            print("Invalid choice")
            adminChoice = input("Admin Rights:\n1.Add items\n2.Remove items")
def adminAdd(items , prices):
    updatedItems = ''
    updatedPrices = ''
    print('======================================')
    print("This is the menu for today")
    for item in items:
        index = items.index(item)
        print(f"{item.capitalize()}\t:\t{(prices[index])}")
    itemsToadd = input('Enter the name of the item to add: ').capitalize()
    priceOfItem = input("Enter the price of the item: ")
    while True:
        if priceOfItem.isnumeric():
            items.append(itemsToadd.strip())
            prices.append(priceOfItem.strip())
            break
        else:
            print("Price set must be a number!")
            priceOfItem = input("Enter the price of the item: ")
    msg = input("Would you like to add any more items?\n1.Yes\n2.No\n>>").lower()
    if msg == '1' or msg == 'yes':
        return adminAdd(items, prices)
    elif msg == '2' or msg == 'no':
        for item in items:
            updatedItems += item+','
        for price in prices:
            updatedPrices += price+','
        updatedMenu = updatedItems+updatedPrices
        encodedUpdatedMenu = updatedMenu.encode()
        clientsocket = getnewsocket()
        host = "localhost"
        clientsocket.connect((host, 8089))
        msg = '4'
        clientsocket.send(msg.encode())
        time.sleep(2.4)
        clientsocket.send(encodedUpdatedMenu)
        return mainMenuNavigation(items,prices)
    else:
        print("Please enter a valid choice")
        msg = input("Would you like to add any more items?\n1.Yes\n2.No\n>>").lower()
def adminRemove(items , prices):
    print('======================================')
    print("This is the menu for today")
    updatedItems = ''
    updatedPrices = ''
    for item in items:
        index = items.index(item)
        print(f"{item.capitalize()}\t:\t${(prices[index])}.00")
    itemsToRemove = input('Enter the index of the item that you want to remove: ')
    if itemsToRemove.isnumeric():
        indexToRemove = int(itemsToRemove) - 1
        items.remove(items[indexToRemove])
        prices.remove(prices[indexToRemove])
    print('======================================')
    print("This is the menu now")
    for item in items:
        index = items.index(item)
        print(f"{item.capitalize()}\t:\t${(prices[index])}.00")
    msg = input("Would you like to remove other items?\n1.Yes\n2.No\n>>").lower()
    if msg == '1' or msg =='yes':
        return adminRemove(items,prices)
    elif msg == '2' or msg == 'no':
        for item in items:
            updatedItems += item+','
        for price in prices:
            updatedPrices += price+','
        updatedMenu = updatedItems+updatedPrices
        encodedUpdatedMenu = updatedMenu.encode()
        clientsocket = getnewsocket()
        host = "localhost"
        clientsocket.connect((host, 8089))
        msg = '5'
        clientsocket.send(msg.encode())
        time.sleep(2.4)
        clientsocket.send(encodedUpdatedMenu)
        return mainMenuNavigation(items,prices)
    else:
        print("Please enter a valid choice")
        msg = input("Would you like to remove other items?\n1.Yes\2.No\n>>").lower()
clientsocket = getnewsocket()
host = "localhost"
clientsocket.connect((host, 8089))
menuPreparation()

print('Goodbye')