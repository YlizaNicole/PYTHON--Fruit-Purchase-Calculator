#Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
#Display the maximum number of apples that you can buy and the remaining money that you will have.
#Display the output in the following format.
#You can buy ___ apples and your change is ___ pesos.

def getdetails():
    Money= int (input('Enter amount of money: '))
    Priceapp= int (input ('price of apple:'))
    max_app= Money // Priceapp
    Change= Money - max_app * Priceapp
    return Money, Priceapp,max_app, Change

def display(maxF, changeF):
    print (f"You can buy {maxF} apples and your change is {changeF} pesos")

#steps
#Enter the amount of money and price of apple, now get the max and the chnage of your purchase
money, price, max, change, = getdetails()
#display the amount
display(max,change)