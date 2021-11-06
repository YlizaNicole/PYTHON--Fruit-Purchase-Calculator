# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is______.

def info():
   app = int (input('How many apples do you want to buy?: '))
   ore = int (input ('How many oranges do you want to buy: '))
   app_= 20 * app
   ore_= 25 * ore
   amount = app_ + ore_
   return amount, app, app_, ore, ore_


    

def display(totalm):
    print (f"the total amount is {totalm}")
    
     


#steps
# ask how many apples and orange you want to buy with the price 20 pesos for the apples and 25 for orange
total, apple, oranges, priceapp, priceora = info()
# display total amount
display (total)