# CTI-110
# P3HW1 - Color Mixer
# Aaliyah Hubbard
# 03032019
#

# Prompt user to input two of three primary colors; output as error code if input color is not primary
# Determine which secondary color is produced of two input colors
# Display secondary color produced as output

# promt user for input

print('LET`S MIX COLORS!')
print('We can make two primary colors into a secondary color.')
print('')

first_prime = input('Please enter first color: ')
sec_prime = input('Please enter second color: ')
print('')

# determine primary and secondary color values

sec_color1 = 'orange'
sec_color2 = 'purple'
sec_color3 = 'green'

# display output

if first_prime == 'red' and sec_prime == 'yellow' or first_prime == 'yellow' and sec_prime == 'red':
    print('Hooray! We`ve made',sec_color1+'!')
    print('')

elif first_prime == 'red' and sec_prime == 'blue' or first_prime == 'blue' and sec_prime == 'red':
    print('Hooray! We`ve made',sec_color2+'!')
    print('')

elif first_prime == 'blue' and sec_prime == 'yellow' or first_prime == 'yellow' and sec_prime == 'blue':
    print('Hooray! We`ve made',sec_color3+'!')
    print('')
else:
    print('Oops! You did not enter a primary color... /: Please try again.')
    print('')
