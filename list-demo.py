import sys

list=[]
def insert(formal_list):
    list.append(formal_list)

def update():
    print("Enter the old and new values: ")
    old = int(input())
    if(old in list):
        new= int(input())
        list[list.index(old)]= new
    else:
        print("Old value does not exist")

def delete():
    print("Enter the element to be deleted: ")
    num= int(input())
    if(num in list):
        list.remove(num)
    else:
        print("Element not found")

def select():
    print(list)
    
while(True):
    print("MENU\n1.Insert\n2.Update\n3.Delete\n4.Select\n5.Exit")
    print("Enter your choice: ")
    choice= int(input())
    if(choice==1):
        print("Enter USN, Name and Marks in order: ")
        element=[input(), input(), input()]
        insert(element)

    elif(choice==2):
        update()
    elif(choice==3):
        delete()
    elif(choice==4):
        select()
    elif(choice==5):
        sys.exit()
    else:
        print("Invalid choice, choose again.")

