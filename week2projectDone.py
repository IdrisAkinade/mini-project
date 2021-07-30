def read_to_file_and_append (file_name, list_to_read):
    with open(file_name,"r") as temp_var_name:
        for item in temp_var_name.readlines():
            list_to_read.append(item.replace("\n",""))
    
def writing_to_file (file_name, list_name):
    with open (file_name, "w") as temp_variable:
        for item in list_name:
            temp_variable.write(item + "\n")

def list_to_dict(list_name):
        return {key:value for key,value in enumerate(list_name)}

products = []
couriers = []


read_to_file_and_append ("products.txt", products)
read_to_file_and_append ("couriers.txt", couriers)


def welcome():
    
    print("") 
    print("\t\033[34m  #################### \033[0m ")
    print("\t\033[1;37;40m     A Cup Of Joy  \033[0;37;40 ")
    print("\t\033[34m  ####################  \033[0m")
    enter = input("\n Press Enter To Use The App ")
    if  enter == "":
        main_menu()
    else:
        print("Invalid !!! Please Press Enter")
        welcome()

# Displays the main menu to the user
def main_menu():
    main_menu_option = "" 
    print("") 
    print("\t------------------- ")
    print("\t\033[34m      Main Menu     \033[0m")
    print("\t-------------------")
    print("""\033[33m
        [0] - Exit App
        [1] - Product Menu Option
        [2] - Courier Menu Option
    \033[0m""")
    main_menu_option =  int(input("\n Please Select Main Menu Options : ")) 
        
    if main_menu_option == 0:
        read_to_file_and_append("products.txt", products)
        writing_to_file("couriers.txt", couriers)
        print("\n\033[32m Products And Couriers List Have Been Saved \033[0m ")
        print("\n\t\033[31m Thank you & Goodbye.\033[0m")
        print("")
        exit()
        
    elif main_menu_option == 1:
        product_menu()
        
    elif main_menu_option == 2:
        courier_menu()
        
    else:
        print("\n\033[31m The Selection Provided Is Invalid.\033[0m")
        main_menu()
        
# Displays the product menu to the user 
def product_menu():
    again = ""
    print("") 
    print("\t --------------------")
    print("\t\033[34m*** Product Menu ***\033[0m") 
    print("\t --------------------")
    print(""""\033[33m
        [0] - Main Menu
        [1] - Product List
        [2] - Create A New Product
        [3] - Update A Product
        [4] - Delete A Product
        \033[0m""")
    
    product_menu_option =  int(input("\n Please Select A Product Menu Options : "))
    while product_menu_option < 0 or product_menu_option > 4:
        print("\n\033[31m The Selection Provided Is Invalid.\033[0m")
        product_menu_option = int(input("\n Please Select One Of The Five Options Given  "))
        
    if  product_menu_option == 0:
        main_menu()

    elif product_menu_option == 1:
        print("\n\033[32m The Product List Is :\033[0m",products)
        
    elif product_menu_option == 2:
        new_product_name = input("\n Please Enter A New Product Name : ")
        products.append(new_product_name)
        writing_to_file("products.txt", products)
        print("\n\033[32m The New Product List Is :\033[0m",products)
        
    elif product_menu_option == 3:
        print(list_to_dict(products))
        product_index_value = int(input("\n Please Enter The Index value Of The Product You Want To Update : "))
        while product_index_value < 0 or product_index_value > 8:
            print("\n\033[31m The selection provided is invalid.\033[0m")
            product_index_value = int(input("\n Please Select Number from 0 to 8 "))
        new_product_name = input("\n Please Enter A New Product Name For The Product: ")
        products[product_index_value] = new_product_name
        writing_to_file("products.txt", products)
        print("\n\033[32m The Updated Product List Is :\033[0m",products)

    elif product_menu_option == 4:
        print("\n\033[32m The Product List Is :\033[0m",list_to_dict(products))
        delete_product_index_value = int(input("\n Please Enter The Index value Of The Product You Want To Delete : "))
        while delete_product_index_value < 0 or delete_product_index_value > 8:
            print("\n\033[31m The selection provided is invalid.\033[0m")
            delete_product_index_value = int(input("\n Please Select Number from 0 to 8 "))
        del products[delete_product_index_value] 
        writing_to_file("products.txt", products)
        print("\n\033[32m The New Product List Is :\033[0m",products)
            
    again = input("\n\t\033[34m Is There Anything Else You Would Like To Do ? \033[0m \033[31m Yes\033[0m  or \033[33m No \033[0m") 
    again = again.lower()

    if again =="yes" or again =="y":
        product_menu()
    else:
        print("\n\t\033[31m Thank you & Goodbye.\033[0m")
        print("")
        exit()        
    
# Displays the courier menu to the user 
def courier_menu():
    courier_menu_option = ""
    print("") 
    print("\t -----------------")
    print("\t\033[34m*** Courier Menu ***\033[0m")
    print("\t -----------------")
    print("""\033[33m
        [0] - Return To Main Menu
        [1] - Couriers List
        [2] - Create A New Courier
        [3] - Update A Courier
        [4] - Delete A Courier
        \033[0m""")

    courier_menu_option =  int(input("\n Please Select A Courier Menu Options : "))
    while courier_menu_option < 0 or courier_menu_option > 4:
        print("\n\033[31m The Selection Provided Is Invalid.\033[0m")
        courier_menu_option = int(input("\n Please Select One Of The Five Options Given  "))

    if  courier_menu_option == 0:
        main_menu()
        
    elif courier_menu_option == 1:
        print("\n\033[32m The Courier List Is :\033[0m",couriers)
        
    elif courier_menu_option == 2:
        new_courier_name = input("\n Please Enter A New Courier Name : ")
        couriers.append(new_courier_name)
        writing_to_file("couriers.txt", couriers)
        print("\n\033[32m The New Product List Is :\033[0m",couriers)

    elif courier_menu_option == 3:
        print(list_to_dict(couriers))
        courier_index_value = int(input("\n Please Enter The Index value Of The Courier You Want To Update : "))
        while courier_index_value < 0 or courier_index_value > 8:
            print("\n\033[31m The selection provided is invalid.\033[0m")
            courier_index_value = int(input("\n Please Select Number from 0 to 8 "))
        new_courier_name = input("\n Please Enter A New Courier Name For The Product: ")
        couriers[courier_index_value] = new_courier_name
        writing_to_file("couriers.txt", couriers)
        print("\n\033[32m The Updated Product List Is :\033[0m",couriers)
        
    elif courier_menu_option == 4:
        print("\n\033[32m The Courier List Is :\033[0m",list_to_dict(products))
        delete_courier_index_value = int(input("\n Please Enter The Index value Of The Courier You Want To Delete : "))
        while delete_courier_index_value < 0 or delete_courier_index_value > 8:
            print("\n\033[31m The selection provided is invalid.\033[0m")
            delete_courier_index_value = int(input("\n Please Select Number from 0 to 8 "))
        del couriers[delete_courier_index_value] 
        writing_to_file("couriers.txt", couriers)
        print("\n\033[32m The New Courier List Is :\033[0m",couriers)
        
    again = input("\n\t\033[34m Is There Anything Else You Would Like To Do ? \033[0m \033[31m Yes\033[0m  or \033[33m No \033[0m") 
    again = again.lower()

    if again =="yes" or again =="y":
        courier_menu()
    else:
        print("\n\t\033[31m Thank you & Goodbye.\033[0m")
        print("")
        exit()       
welcome()     