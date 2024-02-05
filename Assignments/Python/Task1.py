'''
Task 1 
Suppose you are the owner of a grocery shop. So, make a dictionary of items and their prices present in your shop, to track for 
your internal purpose. 
d = {chips: 50, snacks: 80, chocolate: 50} and so on
Now ask the user one by one what all the things he/she wants to buy. Ask at each iteration if the user wants to add more items 
to his cart. If yes, show all the options present and ask them to type one of them. Also ask the quantity how much they want to 
buy in the whole number like1,2,3, etc. 
If the users type no, Calculate the total amount and display what all items have been added into their bill and amount for each 
item along with the total billing amount. 
Also handle the situation, for if the user selects a wrong item not present in the list display the message Wrong Item Selected 
and ask for input again.
'''


inventory_with_unit_price = {
    'pantene_shampoo' : {'small_sachet' : 5, 'big_sachet' : 10, 'small_bottle' : 100, 'big_bottle' :200 }, 
    'himalaya_anti_dandruff_shampoo' : {'small_sachet' : 5, 'big_sachet' : 10, 'small_bottle' : 110, 'big_bottle' :220}, 
    'Santoor_Soap' : {'small_bar' : 10, 'big_bar' : 25, '3+1 combo' : 75},
    'Dettol_Soap' : {'small_bar' : 12, 'big_bar' : 24, '3+1 combo' : 70},
    'Dove_Soap' : {'small_bar' : 20, 'big_bar' : 40, '3+1 combo' : 120},
    'Peanuts_1kg' : 125, 
    'Maida_1kg' : 60, 
    'Wheat_10kg' : 500,
    'Jowar_10kg' : 600
                             }

print('Welcome to Texas_Supermart\n')


loop_trigger = True
cart = {}

while loop_trigger == True:
    for item, packaging_wise_price in inventory_with_unit_price.items():
        print(item,' >> ', packaging_wise_price)
    #print(f'Our Inventory :\n {inventory_with_unit_price.items()}')
    item = input('Please choose items to buy from below inventory by typing the item_name as shown in inventory list:\n')
    packaging = input('Please choose the packaging size if applicable or else type NA')
    quantity = int('Please enter the quantity required for the same')

    wanna_buy_something_else = input('Would you like to buy something else as well ? Type Yes or No')
    if wanna_buy_something_else == 'Yes':
        loop_trigger = True
    else :
        loop_trigger = False
        

