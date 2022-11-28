import math
 
def swap(a,b):
 
    temp=a
    a=b
    b=temp
 
# log(n) solution
def xnor(a, b):
     
    # Make sure a is larger
    if (a < b):
        swap(a, b)
 
    if (a == 0 and b == 0) :
        return 1;
     
    # for last bit of a
    a_rem = 0
     
    # for last bit of b
    b_rem = 0
 
    # counter for count bit and
    #  set bit in xnor num
    count = 0
     
    # for make new xnor number
    xnornum = 0
 
    # for set bits in new xnor
    # number
    while (a!=0) :
     
        # get last bit of a
        a_rem = a & 1
         
        # get last bit of b
        b_rem = b & 1
 
        # Check if current two
        # bits are same
        if (a_rem == b_rem):    
            xnornum |= (1 << count)
         
        # counter for count bit
        count=count+1
         
        a = a >> 1
        b = b >> 1
     
    return xnornum;

num1 = 17 #int(input("Number 1:"))
num2 = int(input("Number 2:"))

NOR = (num1 ^ 0b11111111) & (num2 ^ 0b11111111)

print ("AND: ", int(num1) & int(num2))
print("---------------------")
print ("OR: ", int(num1) | int(num2))
print("---------------------")
print ("XOR: ", int(num1) ^ int(num2))
print ("NOT1: ", ~int(num1))
print ("NOT2: ", ~int(num2))
print ("NOR: ", NOR)
print ("XNOR: ", xnor(num1, num2))
