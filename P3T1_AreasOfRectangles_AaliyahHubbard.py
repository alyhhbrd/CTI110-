# Programming Tutorial 1 - Areas of Rectangle
# 03032019
# CTI-110 P3T1 - Areas of Rectangles
# Aaliyah Hubbard
#

# PC:
# gather input for dimensions of each rectange >
# calculate area for two rectangles
# determine whether if >,<, or = & display output for result


# user input dimensions of rectangle1 & rectange2

length1 = int(input('Please enter lenth of first rectangle: '))
width1 = int(input('Please enter length of first rectangle: '))
print('')

length2 = int(input('Please enter lenth of second rectangle: '))
width2 = int(input('Please enter lenth of second rectangle: '))
print('')

# calculate area

recarea1 = int(length1 * width1)
recarea2 = int(length2 * width2)

# display output for calculated area (>,<, or =)

if recarea1 == recarea2:
    print('Rectangle 1 has an area equal to Rectangle 2')
else: 
    if recarea1 > recarea2:
        print('Rectangle 1 has an area greater than that of Rectangle 2')
    else:
        print('Rectangle 1 has an area less than that of Rectangle 2')


