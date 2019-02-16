# program calculating tip amount of meal purchase in 15%, 18%, & 20%
# 02162019
# CTI-110 P2HW2 - Meal Tip Calculator
# Aaliyah Hubbard
#

# PSUEDOCODE:
# user input meal_purchase amount >
# calculate tip_percentage using 0.15, 0.18, and 0.20 of meal_purchase
# (meal_purhase * 0.15) = tip_percentage15 // (meal_purhase * 0.18) = tip_percentage18 // (meal_purhase * 0.20) = tip_percentage20 >
# display tip_percentage >
# display total_charge

meal_purchase = float(input('Please enter amount of meal purchase: $'))
print('Of $', format(meal_purchase, '.2f')),print('Your tip amounts will be...') 

#calculate tip_percentage 
tip_percentage15 =  float(meal_purchase * 0.15)
tip_percentage18 =  float(meal_purchase * 0.18)
tip_percentage20 =  float(meal_purchase * 0.20)

#print blank for space
print('')

#display tip_percentages
print('15%: $',format(tip_percentage15, ',.2f'))
print('18%: $',format(tip_percentage18, ',.2f'))
print('20%: $',format(tip_percentage20, ',.2f'))

#blank space
print('')

#calculate total_charge
total_charge1 = float (meal_purchase + tip_percentage15)
total_charge2 = float (meal_purchase + tip_percentage18)
total_charge3 = float (meal_purchase + tip_percentage20)

#display total_charge
print('Your total charge with 15% tip will be: $',format(total_charge1, ',.2f'))
print('Your total charge with 18% tip will be: $',format(total_charge2, ',.2f'))
print('Your total charge with 20% tip will be: $',format(total_charge3, ',.2f'))

