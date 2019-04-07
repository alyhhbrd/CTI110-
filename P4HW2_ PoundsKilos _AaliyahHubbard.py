# program converts LBs to KG Converter using (KG= LB/2.2046)
# 03242019
# CTI-110 P4HW2 - Pounds to Kilograms Converter
# Aaliyah Hubbard
#

#

# define main program
# define variables
# create loop for lb to kg conversion chart + display result

#define main 
def main():

#define variables
    startLBS = 100
    endLBS = 301
    increment = 10
    conversionFACT = 2.2046
    
#create loop + display result
    print('LBS\tKG')
    print('----------')

    for lbs in range (startLBS, endLBS, increment):
        kg = lbs / conversionFACT
        print(lbs,'\t',format(kg,'.2f'))
        

main()
    
