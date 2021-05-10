import socket
from datetime import datetime
from datetime import date
import calendar
import uuid
from time import gmtime, strftime
import csv
def cateringOptions(con):
    previewDay = con.recv(255)
    print(previewDay)
    Day = (previewDay.decode()).capitalize()
    with open(f'{Day}.txt') as preview:
        menuExtracted = preview.read()
        menuEncoded = menuExtracted.encode()
        con.sendall(menuEncoded)
        print("Menu has been successfully sent over to the client")
def menuPrep(con):
    print("connected")
    while True:
        buf = con.recv(255)
        choice = buf.decode()
        if choice == '1':
            with open(f'{dateToday}.txt') as file:
                menuExtracted = file.read()
                menuEncoded = menuExtracted.encode()
                con.sendall(menuEncoded)
                print("Menu has been successfully sent over to the client")
                break
        elif choice == '2':
            return cateringOptions(con)
        elif choice == '3':#Admin login fucntion
            return adminLogin(con)
        elif choice == '4':
            return adminAdd(con)
        elif choice == '5':
            return adminRemove(con)
        else:
            buf = con.recv(255)
            fileContents = buf.decode()
            print("logging file")
            return fileLogging(con , fileContents)
def fileLogging(con, fileContents):
    global my_id,timeNow,datetime
    count = 1
    items = (con.recv(2048)).decode()
    with open('logfile.txt' , 'a') as f:
        f.write(f'\n\n{str(dateToday)}\n=====Client session:{str(my_id)}=====\nClient made a payment of ${fileContents} at {timeNow}')
        clientItems = items.split(sep='\n')
        clientItems.remove(clientItems[-1])
        for food in clientItems:
            f.write(f'\n{count}: {food}')
            count = count+1
        f.write('\n=============================================================')
def adminLogin(con):
    credentials = con.recv(255)
    combinedCredentials = credentials.decode()
    print(combinedCredentials)
    credentialsUser = combinedCredentials.split(sep=',')
    with open('admin.txt' , 'r') as file:
        file_reader = csv.reader(file)
        username = credentialsUser[0]
        password = credentialsUser[1]
        user_find(file_reader,username,password,con)
def user_find(file,username,password,con):
    for row in file:
        if row[0] == username:
            print('Username found', username)
            user_found = [row[0],row[1]]
            pass_check(user_found,password,con)
            break
        else:
            msgToSendBack = 'no'
            encodedMsgToSendBack = msgToSendBack.encode()
            con.send(encodedMsgToSendBack)
def pass_check(user_found,password,con):
    if user_found[1]==password:
        print('Password found')
        msgToSendBack = 'yes'
        encodedMsgToSendBack = msgToSendBack.encode()
        con.send(encodedMsgToSendBack)
        return adminRights(con)
    else:
        print("password incorrect")
        msgToSendBack = 'no'
        encodedMsgToSendBack = msgToSendBack.encode()
        con.send(encodedMsgToSendBack)
def adminRights(con):
    adminChoice = con.recv(255)
    decodedChoice = adminChoice.decode()
    if decodedChoice == '1':
        return adminAdd(con)
    elif decodedChoice == '2':
        print('reached here')
        return adminRemove(con)
def adminAdd(con):
    updatedMenu = con.recv(2048)
    decodedMenu = updatedMenu.decode()
    preUpdate = list(decodedMenu)
    preUpdate.pop()
    decodedMenu = ''.join(preUpdate)
    with open(f'{dateToday}.txt' , 'w') as file:
        file.write(decodedMenu)
    print('Menu has been updated')
def adminRemove(con):
    updatedMenu = con.recv(2048)
    decodedMenu = updatedMenu.decode()
    preUpdate = list(decodedMenu)
    preUpdate.pop()
    decodedMenu = ''.join(preUpdate)
    with open(f'{dateToday}.txt' , 'w') as file:
        file.write(decodedMenu)
    print('Menu has been updated')
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('0.0.0.0', 8089))
serversocket.listen(5) # become a server socket, maximum 5 connections
while True:
    timeNow = strftime("%H:%M:%S", gmtime())
    my_id = uuid.uuid1()
    my_date = date.today()
    dateToday =calendar.day_name[my_date.weekday()]
    print(dateToday)
    print("waiting a new call at accept()")
    connection, address = serversocket.accept()
    if menuPrep(connection) == 'file':
        None
print("Server stops")