products = ["Chips","Soda","Candy","Cookies","Water","Sandwich"] ### Products
prices = [2.00,2.50,1.50,3.00,1.00,5.00] ### Number of prices
5
shopping_cart = [] ## Shopping cart

def display_products(): ### Function for displaying products
    print("Available Items")
    for i in range(len(products)): ### Iterates through product list
        print(f"{i + 1}. {products[i]}  ${prices[i]}0")
        
    print()

def add_product():
    choice = 0
    while choice not in [1,2,3,4,5,6]:
        for i in range(len(products)):
            print(f"{i + 1}. {products[i]}")
        
        choice = int(input("Enter product number: "))
    
    
    shopping_cart.append(products[choice - 1])
    print(f"{products[choice - 1]} was added to you cart!")

def remove_product():
    remove = 0
    if shopping_cart == []:
                print("Your cart is empty!")
                return
    print("YOUR SHOPPING CART!!!")
    for i in range(len(shopping_cart)):
        print(f"{i + 1}. {shopping_cart[i]}")
        remove = int(input("What item would you like to remove?: "))
        shopping_cart.remove(remove)
        print(f"{shopping_cart[remove]} has been removed")

def view_cart():
    print("YOUR SHOPPING CART!!")
    
    if shopping_cart == []:
        return "EMPTY CART"
    
    for i in range(len(shopping_cart)):
        print(f"{i + 1}. {shopping_cart[i]}")

    print(f"Total Items: {len(shopping_cart)}")

def shopping_total(): 
    print("CURRENT TOTAL")
    subtotal = 0
    for i in range(len(shopping_cart)):
        item = shopping_cart[i]
        
        index = products.index(item) ### Takes the index from the product list
        price = prices[index]
        
        print(f"{item}: ${price:.2f}")
        subtotal += price
    
    print(f"Subtotal: {subtotal:.2f}")
    return subtotal

def checkout(subtotal):
    
    if(subtotal < 10.00): ## Determines what the subtotal qualifies
        discount = 0.00
    elif(10.00 <= subtotal < 20.00):
        discount = 0.05
    elif(20.00 <= subtotal < 40.00):
        discount = 0.10
    else:
        discount = 0.15
    
    final_total = subtotal - subtotal * discount
    print("CHECKOUT")
    print(f"Subtotal: {subtotal}")
    print(f"Discount: {discount * 100}%")
    print(f"Amount Saved: {subtotal * discount}")
    
    print(f"Final Total: {final_total}")
    print("Thank you for shopping!")
    return final_total
    
    
    

            
    
        
    

option = 0
while(option != 6):  ### Starting menu
    print("1. View Available Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Shopping Cart")
    print("5. View Current Total")
    print("6. Checkout")
    
    option = int(input("Enter your choice: ")) ## Selects choice
    
    if(option == 1): ## Displays
        print()
        display_products()
    
    elif(option == 2): ## adds
        print()
        add_product()
    
    elif(option == 3): ## Removes
        print()
        remove_product()
    
    elif(option == 4): ## VIEWING
        print()
        view_cart()
    
    elif(option == 5): ### SHOPPING TOTAL
        print()
        sub = shopping_total()
    
    elif(option == 6): ### CHECKOUT
        print()
        checkout(sub)
    
    else:
        print("Please make a valid option")
