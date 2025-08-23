""" 
TASK 3 : mini project : 

KALYAN JWELLERS : 

M 
>  65
purchase > 2lk - 3lk    20% 
purchase > 3lk - 5lk 	30% 
purchase > 5lk  	35% 


<65
purchase > 2lk - 3lk    10% 
purchase > 3lk - 5lk 	20% 
purchase > 5lk  	25% 



F
>  65
purchase > 2lk - 3lk    25% 
purchase > 3lk - 5lk 	35% 
purchase > 5lk  	40% 


<65
purchase > 2lk - 3lk    15% 
purchase > 3lk - 5lk 	25% 
purchase > 5lk  	30% 


------------------------------------------------------------
Enter your name : 
Enter gender : 
Enter age : 

Enter product : Ring 
Enter product gram : 20  
current gold price (1 grm) : 5752

-------------------------------------
TOTAL GOLD RATE :  XXXXX 


Making charges (1 gram)  : 845
Total Making CHarges :    TOTAL GOLD  X  MAKING CHARGES 

---------------------------------------
TOTAL AMOUNT : GOLD PRICE + TOTAL MAKING CHARG



DISCOUNT :   25% (AUTOMATIC) 
DIS- AMOUNT : except (making charges) 
-----------------------------------------
total net amount : 

--------------------------------------------
HINT : variables , input , conditional statements
"""


name=input("Enter Your Name= ")
gender=input("Enter Your Gender (M/F):  ")
age=int(input("Enter Your Age= "))

product=input("Enter Product= ")
product_weight=int(input("Enter Product Gram= "))
Current_gold_price=5752
print(f"current gold Price = {Current_gold_price}")

print(" ---------------------------------------------- ")
total_gold_amount=5752*product_weight
print(f"total_gold_amount= {total_gold_amount}")
print()
print("--------------------------------------")
print()
 
making_charge=845
total_m_c=making_charge*product_weight
print(f"total_Making_charge= {total_m_c}")
print()
print("-------------------------------------")
print()
total_Amount=total_gold_amount+total_m_c
print(f"total amount= {total_Amount}")
print()

print("--------------------------------------")

discount=0.25
if gender=='m' or gender=='M':
    if age>=65:
        if total_gold_amount>=21000 and total_gold_amount<=31000:
            discount=total_gold_amount*0.20
        elif total_gold_amount>31000 and total_gold_amount<=51000:
            discount=total_gold_amount*0.30
        elif total_gold_amount>51000:
            discount=total_gold_amount*0.35
    else:
        if total_gold_amount>=21000 and total_gold_amount<=31000:
            discount=total_gold_amount*0.10
        elif total_gold_amount>31000 and total_gold_amount<=51000:
            discount=total_gold_amount*0.20
        elif total_gold_amount>51000:
            discount=total_gold_amount*0.25
elif gender=='f' or gender=='F':
    if age>=65:
        if total_gold_amount>=21000 and total_gold_amount<=31000:
            discount=total_gold_amount*0.25
        elif total_gold_amount>31000 and total_gold_amount<=51000:
            discount=total_gold_amount*0.35
        elif total_gold_amount>51000:
            discount=total_gold_amount*0.40
    else:
        if total_gold_amount>=21000 and total_gold_amount<=31000:
            discount=total_gold_amount*0.15
        elif total_gold_amount>31000 and total_gold_amount<=51000:
            discount=total_gold_amount*0.25
        elif total_gold_amount>51000:
            discount=total_gold_amount*0.30


print()
print(f"total Discount= {discount}")
print()
print("--------------------------------------")
print()
total_gross_bill=total_Amount-discount
print(f"total_gross_amount= {total_gross_bill}")        
print()
print("--------------------------------------")
print()
