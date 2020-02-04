cart = []
fruit = ['apple',]
meal = ['Lamb']
vegestable = ['']
menu = ['apple', 'cherry']


def greeting():
    print(' ------------Welcome to Grocery Store------------')
    print('Could we know your name ?')
    name = input('> ')
    print(f"Hello {name}, how may I help you today ")


def rule():
    print("""
1> Add item
2> Delete item
3> Check cart
4> Exit
""")

def add_item():
    for index, item in enumerate(menu):
        print(str(index + 1) , item)

    add_ind = int(input('Please select the item\'s number to add: ')) -1
    item = menu[add_ind]
    cart.append(item)
    #print(cart)
    


def delete_item():
    print('Your cart have: ')
    for index,item in enumerate(cart)
        print(str(index + 1) , item)

    print('Please type the number you want to delete: ')
    del_ind = int(input('> '))  - 1
    item = cart[del_ind]
    cart.remove(item)


def display_cart():
    print('Your cart have: ')
    for index in range(len(cart)):
        print(str(index + 1)  + " " + cart[index])


def run_app():
    greeting()
    while True:
        rule()
        command = input('> ')
        if command == '1':
            add_item()
        elif command == '2':
            delete_item()
        elif command == '3':
            display_cart()
        elif command == '4':
            print('Hope to see you again in the future')
            break
        else:
            print('please follow the stucture.')



run_app()


    