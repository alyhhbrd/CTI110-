# MyFitnessPal clone; 5kcal/min @ 20, 35 & 45 minutes 
# 03242019
# CTI-110 P4HW1 - Calories Burned
# Aaliyah Hubbard
#

#initialize burn rate variable
#use loops to calculate iterations @ 20, 35, & 45 minutes
#display results

def main():
    
    print('Feel the burn! It\'s helpful to see it, too. \nI will show you how '
    'many calories will be burned after 20, 35, & 45 minutes at 5kcals/minute.\n')

    bR = 5

    for minutes in [20,35,45]:
        print(f'{minutes*bR} calories are burned in {minutes} minutes.\n')

main()

    
