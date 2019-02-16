# program converts LBs to KG Converter using (KG= LB/2.2046)
# 02162019
# CTI-110 P2HW1 - Pounds to Kilograms Converter
# Aaliyah Hubbard
#

# PSUEDOCODE: user input LBs > calculate KGs as LB/2.2046 > display KG amount

# user input LB amount
lb_amount = float(input('Enter Pound Amount: '))

# calculate KGs as LB/2.2046:
kg_amount = lb_amount / 2.2046

# display converted LBs in KGs:
print('The weight in kilograms is:', format(kg_amount, ',.4f'))
