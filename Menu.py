def option3():
    #do something
    print('updating ticket')

# how can I make a reuseable menu 
def menu():
    answer = int(input("1.add ticket \n2.cancel ticket \n3.update ticket\n"))
    match answer:
        case 1:
            print('this is 1') 
        case 2: 
            print('this is 2')
        case 3: 
            option3()
        case _ :
            print(f'invalid number option:{answer}')
            menu()
            
            

print("hello")
menu()
 
class MyMenu:
    # have like a state management 
    pass