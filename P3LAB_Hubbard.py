# CTI-110 
# P3Lab1 - Debugging
# Aaliyah Hubbard 
# 03032019
#

# This program takes a number grade and outputs a letter grade.

# student inputs score
# calculate input and determine grade using 10-point scale
# display letter grade as output

def main():

# define scores

    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50

# gather input

    score = int(input('Enter grade: '))
    
# calculate and display output as letter grade
    
    if score >= A_score:
        print('Your grade is: A')
    elif score >= B_score and score < A_score:
        print('Your grade is: B')
    elif score >= C_score and score < B_score:
        print('Your grade is: C')
    elif score >= D_score and score < C_score:
        print('Your grade is: D')
    elif score <= F_score and score > 0:
        print('Your grade is: F')
    else:
        print('Sorry, Buddy, but you blew it.')
        
# program start
main()
