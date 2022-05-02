#Author:Sheadiejah Salmon
#Date Created: April 22,2022
#Course: ITT103
#Purpose: Programming showing the amount of commission a salesperson will receive based on there sales amount and what class they fall to.
sales_class = 0
while sales_class !=8:
    salesperson_number = input("Insert sales person number")
    sales_class=int(input("Insert sales class"))
    sales_amount = float(input("Insert sales amount"))

    #Condition 1
    if sales_class==1 and sales_amount<=1000:
        rate = 0.06
        Commission = sales_amount*rate
        print('Commission =',Commission)
    #Condition 2    
    elif sales_class==1 and sales_amount>1000 and sales_amount <2000:
        rate = 0.07
        Commission = sales_amount*rate
        print('Commission =',Commission)
    #Condition 3    
    elif sales_class==1 and sales_amount>=2000:
        rate = 0.10
        Commission = sales_amount*rate
        print('Commission =',Commission)
    #Condition 4    
    elif sales_class==2 and sales_amount<1000:
        rate = 0.04
        Commission = sales_amount*rate
        print('Commission =',Commission)
    #Condition 5
    elif sales_class==2 and sales_amount>=1000:
        rate = 0.06
        Commission = sales_amount*rate
        print('Commission =',Commission)
    #Condition 6    
    elif sales_class==3: 
        rate = 0.045
        Commission = sales_amount*rate
        print('Commission =',Commission)
    #If no condition is true    
    else:
        print('There is no Commission for that class')  
print('The End')         

