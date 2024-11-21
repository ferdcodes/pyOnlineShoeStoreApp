import random
"""This code is the Python version of "OnlineShoeStoreApp" that I created using Java. This code 'emulates' 
an online shoe store. There are 6 different shoes and everytime the code runs, a different amount of stock
is assigned to each shoe. The user is asked to input what shoe they want and how much they want of the shoe.
After, it asks if the user is ready to checkout or not. Once done, the user is given their total amount.
Next update: The ability to take things out of the cart, using tuples/lists."""

def main() :
    #create variables for each shoe and assign a random int from 1-10 to each.
    joRan = random.randint(1,10)
    jtRan = random.randint(1, 10)
    jfRan = random.randint(1,10)
    ltoRan = random.randint(1, 10)
    kfRan = random.randint(1,10)
    ksRan = random.randint(1,10)

    #These variables keep track of the user's cart.
    joTotal = 0
    jtTotal = 0
    jfTotal = 0
    ltoTotal = 0
    kfTotal = 0
    ksTotal = 0

    #cont is a sentinel variable
    cont = 1
    #shoe is a variable that decides what shoe the user is asking for
    shoe = 0
    #price is the varaible that will hold the final price of the cart
    price = 0


    while cont == 1 :
        #valid is a sentinel variable used for the while loops within the main while loop.
        valid = 0
        print("Shoe Model:          Quantity:")
        print("1.Jordan 1:              %d" %joRan)
        print("2.Jordan 2:              %d" %jtRan)
        print("3.Jordan 4:              %d" %jfRan)
        print("4.Lebron 21:             %d" % joRan)
        print("5.Kobe 4:                %d" % joRan)
        print("6.Kobe 6:                %d" % joRan)
        shoe = int(input("Enter a shoe # (Enter 0 to checkout): "))


        if shoe == 1 :
            while valid == 0 :
                jOne = int(input("How many Jordan 1's would you like? "))
                if jOne <= joRan and jOne > -1:
                    joTotal = jOne
                    joRan -= jOne
                    cont = int(input("Added to cart. Enter 1 to continue shopping, enter 2 to checkout "))
                    if cont == 1:
                        #only ends inner loop
                        valid = 1
                    else :
                        #end inner loop and main loop
                        valid = 1
                        cont = 2
                #If the user inputs a number like -1 or a number bigger than the stock, asks user to input again
                else :
                    print("Invalid amount of Jordan 1 shoes, please enter a valid number.")

        elif shoe == 2 :
            while valid == 0 :
                jThree = int(input("How many Jordan 3's would you like? "))
                if jThree <= jtRan and jThree > -1 :
                    jtTotal = jThree
                    jtRan -= jThree
                    cont = int(input("Added to cart. Enter 1 to continue shopping, enter 2 to checkout "))
                    if cont == 1:
                        # only ends inner loop
                        valid = 1
                    else :
                        # end inner loop and main loop
                        cont = 2
                        valid = 1
                # If the user inputs a number like -1 or a number bigger than the stock, asks user to input again
                else :
                    print("Invalid amount of Jordan 3 shoes, please enter a valid number.")

        elif shoe == 3 :
            while valid == 0 :
                jFour = int(input("How many Jordan 4's would you like? "))
                if jFour <= jfRan and jFour > -1:
                    jfTotal = jFour
                    jfRan -= jFour
                    cont = int(input("Added to cart. Enter 1 to continue shopping, enter 2 to checkout "))
                    if cont == 1:
                        # only ends inner loop
                        valid = 1
                    else :
                        # end inner loop and main loop
                        cont = 2
                        valid = 1
                else : #If the user inputs a number like -1 or a number bigger than the stock, asks user to input again
                    print("Invalid amount of Jordan 4 shoes, please enter a valid number.")

        elif shoe == 4 :
            while valid == 0 :
                lto = int(input("How many LeBron 21's would you like? "))
                if lto <= ltoRan and lto > -1 :
                    ltoTotal = lto
                    ltoRan -= lto
                    cont = int(input("Added to cart. Enter 1 to continue shopping, enter 2 to checkout "))
                    if cont == 1:
                        # only ends inner loop
                        valid = 1
                    else :
                        # end inner loop and main loop
                        cont = 2
                        valid = 1
                else : #If the user inputs a number like -1 or a number bigger than the stock, asks user to input again
                    print("Invalid amount of LeBron 21 shoes, please enter a valid number. ")

        elif shoe == 5 :
            while valid == 0 :
                kFour = int(input("How many Kobe 4's would you like? "))
                if kFour <= kfRan and kFour > -1:
                    kfTotal = kFour
                    kfRan -= kFour
                    cont = int(input("Added to cart. Enter 1 to continue shopping, enter 2 to checkout "))
                    if cont == 1:
                        # only ends inner loop
                        valid = 1
                    else :
                        # end inner loop and main loop
                        cont = 2
                        valid = 1
            else : #If the user inputs a number like -1 or a number bigger than the stock, asks user to input again
                    print("Invalid amount of Kobe 4 shoes, please enter a valid number.")

        elif shoe == 6 :
            while valid == 0 :
                kSix = int(input("How many Kobe 6's would you like? "))
                if kSix <= ksRan and kSix > -1 :
                    ksTotal = kSix
                    joRan -= kSix
                    cont = int(input("Added to cart. Enter 1 to continue shopping, enter 2 to checkout "))
                    if cont == 1:
                        # only ends inner loop
                        valid = 1
                    else :
                        # end inner loop and main loop
                        cont = 2
                        valid = 1
                else : #If the user inputs a number like -1 or a number bigger than the stock, asks user to input again
                    print("Invalid amount of Kobe 6 shoes, please enter a valid number. ")

        else :
            cont = 0

    price = checkout(joTotal, jtTotal, jfTotal, ltoTotal, kfTotal, ksTotal)
    print("The price of your cart is $%d" %price)

def checkout(jOne, jThree, jFour, lto, kFour, kSix) :
    price = (jOne * 140) + (jThree * 250) + (jFour * 275) + (lto * 125) + (kFour * 225) + (kSix * 400)
    return (price)

main()
