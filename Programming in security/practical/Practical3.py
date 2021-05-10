def Q1():
    ports_open = input('Please enter the ports that were found to be open\n>>').split(sep=" ")
    ports_to_check = input('Please enter the port to be checked\n >>')
    for x in range(0,len(ports_open)):
        if ports_open[x]==ports_to_check:
            print(f"Yes the port {ports_to_check} is open")
            break
        else:
            print(f'Oops seems like the port {ports_to_check} is not open')




def Q2():
    dishes = input("Please enter your restaurant dishes, seperated by a comma :\n").split(sep=',')
    userSearch = input("Please enter the dish that you want to find: \n")
    count = 0
    for x in dishes:
        if userSearch in x:
            print(f'{x}')
            count = 1
    if count == 0 : 
        print('Sorry we couldnt find your item')



def Q3():
    marks = [80,39,79,81,79,70,84,57,66,86]
    print('This Score that qualify for "A"')
    int_marks = []
    for i in marks:
        if i > 80:
            print(f"{i}\n")
        if i > 0:
            int_marks.append(int(f'{i}') )
Q3()
