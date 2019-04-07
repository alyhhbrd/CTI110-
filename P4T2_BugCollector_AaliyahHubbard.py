# P4T2_program that keeps running total of # of bugs collected in 5 day span
# 03242019
# CTI-110 P4T2 - Bug Collector
# Aaliyah Hubbard
#

#Initialize accumulator
#Gather user input for amount of bugs collected
#Display total result of input

#initialize
total = 0

#get user input
print('ಠ_ಠ \nYou collect... bugs? \nYou say you like to collect '
'them in your spare time? \nHuh. That\'s weird. You\'re weird.')

for day in range (1,6):
    print('Enter the total amount of bugs collected on day', day)
    bugs = int(input())
    total += bugs

#print result
print('Wow, how gross. \nYou have collected a total of',total,'abominations - I mean, bugs in 5 days.\nNow please find a '
'new hobby. This one sucks.')
