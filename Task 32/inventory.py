#========The beginning of the class==========
class Shoe:
#In this function you must initialise the following attributes:
#country
#code
#product
#cost
#quantity
            
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity 
        pass

#code to return the cost of the shoe in this method        
    def get_cost(self):
        return self.cost
        
#code to return the quantity of the shoes
    def get_quantity(self):
        return self.quantity
        
        
#code to return a string representation of a class
    def __str__(self) -> str:
                return super().__str__()
    pass
        
#=============Shoe list===========
 #create a list of objects for the shoe list
with open('inventory.txt') as f:
    lines = f.readlines

#==========Functions outside the class==============
def read_shoes_data(self):
    return self.read_shoes_data
    
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
def capture_shoes(self):
    return self.capture_shoes
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

def view_all(self):
    return self.view_all
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

def re_stock(self):
    return self.re_stock
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

def search_shoe(self):
    return self.search_shoe
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

def value_per_item(self):
    return self.value_per_item
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

def highest_qty(self):
    return self.highest_qty
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
while True:
    menu = input('''
    Main Menu:
    rs - read all shoe data
    cs - capture shoe
    va - view all shoe data
    re - restock 
    s - search shoe
    v - value per item
    h - view highest shoe quantity
    ''')

    rs = input("read_shoes_data") 
    cs = input("capture shoe data")
    va = input("view all shoe data")
    re = input("restock")
    s = input("search shoe")
    v = input("value per item")
    h = input("view highest shoe quantity")

    menu = 0
    while menu <8:
        print("1. rs - read all shoe data\n2. cs - capture shoe\n3. va - view all shoe data\n4.re - restock\n5.s - search shoe\n6. v - value per item\n7. h - view highest shoe quantity")
        menu = int(input("pick a menu option: "))
        if menu >7:
            print("Goodbye and have a nice day")
        else:
            print("you picked " + str(menu))