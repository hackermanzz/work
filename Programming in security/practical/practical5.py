import os
print(os.getcwd())

f=open("files\\students.txt")
for line in f:
    print(line , end =" ")
f.close()

with open("files\\notes.txt" , 'w') as f:
    f.write('Hello world')

with open("files\\notes.txt" , 'w') as f:
    for line in f:
        print(line)