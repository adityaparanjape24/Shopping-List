final_list = [] #Creating  2 Empty list to add next list into it
my_list = []
final_list.append(my_list)#Here my_list will be added to empty Final_list


def add_item(my_list, item=None):   #Declared function to add items in list when by default items are none and adding it in my_list
    if item is not None and item != "":
        my_list.append(item)


def get_items():#This function is used to return my_list list
    return my_list


def get_final_list():
    return final_list


def shopping_interface(): #This function actually deals with creating lists 
    print("Welcome to Shopping List")
    add_more = 'y' # This is a condition for creating list, when this will be y then only rest paart will execute
    shopping_item = input("Enter the name of the item\n").lower() # We accpet user input and store it in shopping_item variable
    add_item(my_list,shopping_item) # Item from user is stored in my_list and to add_item function
    counter = 0 # this counter is for no.of list we are creating
    while add_more =='y':  # Created While loop so that it can be used infinite times 
          shopping_item= input().lower() #input is blank so that it does not print "Enter the name of the item" everytime for adding new item
          x = final_list[counter] #created a variable for final_list so thaat it can be called later
          add_item(x,shopping_item) #calling final_list and shopping_item
          if shopping_item == "": #if shopping item is empty add new items
            add_more = input("Do you want to add more items Y / N  ?\n").lower() # if shopping item is blank we can add items
            if add_more == 'n': # when we don't want to add items in list it will print the created list   
                print("Thank you.")
                print(x) #here we call the final list with shopping list
                show_numbered_shopping_list()
                new = input("Do you want to create more list Y / N ?\n ").lower()# here we can create new list 
                if new == 'y':#when it will be Y the only new list will be created 
                   add_more ='y'
                   counter += 1
                   new_list = [] #created a empty list so that the items in next list will added here and later it will be appended in final_list
                   final_list.append(new_list) # Final_list will be appended with the upcoming list
                

def show_shopping_list(): # this function is created to print items in our list
    print("hear are the items in your shopping list")
    for item in get_items():
        print(item)

def show_numbered_shopping_list():# in this funtion items are prited in numberd format
    print("Here are the items in your shopping list")
    item_counter=0 # at start we don't have any item so item counter is 0
    for shopping_list in final_list:
        item_counter += 1 # after adding items in our list it starts numbering
        print(f"Shopping list {item_counter}")

        product_counter = 0
        for product in shopping_list:
            product_counter +=1
            print(f"{product_counter}.{product}")


def check_item() :
    item = input("Which item do you want to check from the shopping list: ").lower()
    item_found = False
    for shopping_list in final_list:
        if item in shopping_list:
            item_found = True
            print("Yes, " + item + " is in your list")
            break
    if item_found == False:
      print(item +  " is not on your list") 
               

shopping_interface()
show_numbered_shopping_list()
check_item()
