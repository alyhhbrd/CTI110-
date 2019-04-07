# Program get user input of assortment of numbers, returns sum
# 03242019
# CTI-110 P4HW3 - Sum of Numbers
# Aaliyah Hubbard
#

#prompt user for input
#define variables
#gather input using while loop, negative number being sentinel
#display result

def main():
    
    print('Iiiii\'m smart, I can add all the numbers you give me! \nBe warned, '
          'I\'ll know to stop when you give me a negative number.')
    inputNum = float(input('Gimmie a number, any number: '))
    
    sumTotal = 0

    while inputNum >= 0:
       
        sumTotal += inputNum
        inputNum = float(input('Keep going!: '))
        
    print('The sum total is: ', format(sumTotal, '.2f'))
    print('What? Did you think I\'d add the negative too? I\'m not that smart...')

main()
