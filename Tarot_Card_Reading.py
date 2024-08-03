from random import shuffle
import csv

deck = []
#read the cards in from the .csv
with open('TarotCards.csv', 'r') as csvfile:
    cards = csv.reader(csvfile)
    
    for row in cards:
        deck.append(row)
#shuffle the deck
shuffle(deck)

#ask the user to enter 3 numbers between 1 
# and the max length of the deck 
numbers = ['first','second','third']
user_num = []

print("This is a tarot reading program. You will be asked to enter {} numbers between 1 and {} then you will recieve a card reading.".format(len(numbers),len(deck)))
for i in range(len(numbers)):
    user_input  = input("Enter your {} number: ".format(numbers[i]))
    user_num.append(int(user_input))

#return the user's tarot reading
for i in user_num: 
    print('{} : {}'.format(deck[i-1][0],deck[i-1][1]))
