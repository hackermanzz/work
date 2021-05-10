def main(choice):
    if choice == 'q' or choice=='Q':
        print('goodbye')
    elif choice == 1 :
        print('Processing please wait...\n.\n.\n.\n.\n')
        return odd()
    elif choice == 2 :
        print('Processing please wait...\n.\n.\n.\n.\n')
        return comparison()
    elif choice == 3 :
        print('Processing please wait...\n.\n.\n.\n.\n')
        return sum()
    elif choice == 4 :
        print('Processing please wait...\n.\n.\n.\n.\n')
        return Display()
    else:
        print("Please enter a valid choice")
#--------------------------------------------------------------------------------------->
#--------------------------------------------------------------------------------------->
def odd():
    title='Odd or Even'
    blank=''
    print(f'{blank:*^40}\n {title} \n{blank:*^40}')
    userInput = input('Enter a number\n>>')
    if userInput.isnumeric():
        userInput_number = int(userInput)
        if userInput_number %2 != 0:
            final = 'odd'
        else :
            final = 'even'
            print(f'The number you have entered is {final}')
    elif userInput == 'q' or userInput == 'Q':
        print('goodbye')
    else:
        print('Please enter a valid choice')
#--------------------------------------------------------------------------------------->
#--------------------------------------------------------------------------------------->
def comparison():
    title='Which is bigger'
    blank=''
    print(f'{blank:*^40}\n {title} \n{blank:*^40}')
    userInput1 = input('Enter the first number or "q" to quit\n>>')
    userInput2 = input('Enter the second number or "q" to quit\n>>')
    if userInput1.isnumeric() and userInput2.isnumeric():
        userInput1_number = int(userInput1)
        userInput2_number = int(userInput2)
        if userInput1_number > userInput2_number:
            print(f'{userInput1_number} is bigger than {userInput2_number}')
        else:
            print(f'{userInput2_number} is bigger than {userInput1_number}')
    elif userInput1 =='Q' or userInput2 =='Q':
        print('goodbye')
#--------------------------------------------------------------------------------------->
#--------------------------------------------------------------------------------------->
def sum():
    title='Addition'
    blank=''
    print(f'{blank:*^40}\n {title} \n{blank:*^40}')
    total = 0
    userInput = input('Enter a number that u want to add or "Q" to stop\n>>')
    while userInput !='Q' and userInput.isnumeric():
        total+= eval(userInput)
        userInput=input(f'Current sum is {total}\n>>')
    if userInput=='Q':
        print('goodbye')
    else:
        print("please enter a valid number")
#--------------------------------------------------------------------------------------->
#--------------------------------------------------------------------------------------->
def Display():
    title='In the range'
    blank=''
    print(f'{blank:*^40}\n {title} \n{blank:*^40}')
    userInput1 = input('Enter the starting number for the range\n>>')
    userInput2 = input('Enter the ending number for the range\n>>')
    if userInput1.isnumeric() and userInput2.isnumeric():
        for x in range(eval(userInput1),eval(userInput2)):
            if x%2==0:
                print(f'The numbers are {x}')
    else:
        print('Please enter valid numbers')
    if userInput1 == 'Q' and userInput2 == 'Q':
        print('goodbye')
#--------------------------------------------------------------------------------------->
#--------------------------------------------------------------------------------------->
blank=''
userInput= input(f'{blank:*^40}\n ST2414 PSEC Practical 2 Qn 1\n{blank:*^40}\nEnter a choice: ')
if userInput.isnumeric():
    userInput_int = int(userInput)
    if userInput_int<5:
        choice =int(userInput_int)
        main(choice)
    else:
        print(f"{userInput} is not a valid choice\nPlease enter a valid choice next time\n>>")
elif userInput == 'q' or userInput=='Q':
    main(userInput)
else :
    print(f'{userInput} is not a valid choice\n Please enter a valid choice next time\n>>')


