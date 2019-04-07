# CTI-110 
# P3HW2 - MealTipTax 
# Aaliyah Hubbard 
# 03032019
#

# prompt for input (amount of meal and desired tip percentage; error if != 15%,18%,or20%)
# calculate tip percentage with added sales tax
# display each amount as output


# prompt for input

print('I hope you`ve enjoyed your meal!')
print('Time to pay up.')
print('')
meal_purchase = float(input('Please enter amount of meal purchase: $'))
print('Let`s see... so your bill was: $',format(meal_purchase,'.2f'))
print('Sales tax in NC in 7%. It is standard practice to tip an additional 15%, 18%, or 20%.')
tip_choice = input('Pick your poison: ')

# calculate tip % and sales tax

salestax = (meal_purchase * 0.07)
tip15 = (meal_purchase * 0.15)
tip18 = (meal_purchase * 0.18)
tip20 = (meal_purchase * 0.20)

# display output

if tip_choice == '15%':
    total = (meal_purchase + tip15 + salestax)
    print('Hola, el cheapo.')
    print('You chose a 15% tip. Your tip is:$',format(tip15,'.2f'))
    print('Tax is:$',format(salestax,'.2f'))
    print('Your bill total is:$',format(total, '.2f'))
elif tip_choice == '18%':
    total = (meal_purchase + tip18 + salestax)
    print('You chose a 18% tip. Your tip is:',format(tip18,'.2f'))
    print('Tax is:$',format(salestax,'.2f'))
    print('Your bill total is:$',format(total, '.2f'))
    print('Have a nice rest of your night.') 
elif tip_choice == '20%':
    total = (meal_purchase + tip18 + salestax)
    print('How generous!')
    print('You chose a 20% tip. Your tip is:$',format(tip20,'.2f'))
    print('Tax is:$',format(salestax,'.2f'))
    print('Your bill total is:$',format(total, '.2f'))
    print('Please come again :)')
else:
    print('Error! You didn`t pick a tip percentage, silly billy. Try again. Include a % symbol this time.')
print('')



