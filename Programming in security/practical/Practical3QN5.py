def swap(portlist):
    value=int(input('Enter port:'))
    temp = {p:s for s,p in portlist.items()}
    if value in temp:
        print(f'{temp[value]} service is running or port {value}')
    else:
        print(f'{value} is not found')


services= {}
s = input("Please enter service:port that were found to be open, seperated by a '|'\n")
pairs = s.split(sep='|')
for pair in pairs:
    svc = pair.split(':')
    services[svc[0].strip()]=int(svc[1].strip())

print("\nThese are the ports that were found and their corresponding device")
for service,port in services.items():
    print(f"\t{port}:{service}")
s =' '
while s != '':
    s= input('''
    1)Search for an open port   
    2)Searh for a service that is running
    3)Update dictionary
    Please enter request\n>
    ''')
    if s =='2':
        userSearch = input("Please enter the port that you wish to find")
        for userSearch in services:
            if userSearch in services.items():
                print(userSearch)
            else:
                print('.')


