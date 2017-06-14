# Version:  Python 2.7.13
#
# Author:   Josh Batchelor
#
# Purpose:  A simple program for the sake of exploring, practicing, and expanding on
#           the basic concepts learned from the Tech Academy Python course.


def main(x=0,y=0):
    x, y = 100, 100
    print("The following are if, elif, and else statements.")
    # Attribute the value of x, and y.
    if(x < y): # { The if  block decides 'st', print st
    	st= "x is less than y"  # Var 'st' is a string 
    elif (x == y):
                st= "x is the same as y"	
    else:
                st= "x is greater than y"
    	# } happens at the end...
    print st
    run()
    not_check()
    plus_check()
    the_tuple()

# Here are some data types.
def run():
    print("\nHere are the data types integer, float and a string.")
    hi = "hello"
    a = 1
    b = 1.5
    print("\nHere is a while loop result.")
    while a < b:
        print b,
        a, b = b, a+b
        break

    print hi   
    power(num=0,g=0)
    
# A function with default value for an argument
def power(num, g=1): # 'g' is the exponent.
# raises a number to the given power
	result =1;
	for i in range(g): # this loop multiplies value of 'g' by whatever number is given, g is only 1 by default.
		result = result * num
	return result



print power(2)
print ("This is a number to the power of 2:")
print power(2,3)
print ("This is 2 to the power of 3:")
print power(4,4) and power(5,5)
print ("\nYou can see this message.") or ("\nYou can't see this message.")

print (100-50)
print (23425*50)
print (90/30)
print (40000%5)


def not_check():
    s = 1
    r = 2
    not(s and r)
    print("\nResults: {} | {}.".format(s,not r))

def plus_check():
    e = 3
    while(e < 5):
        print ("\ne = {}.".format(e))
        e+=e



# Tuple...
def the_tuple():
    print("\nThis is for loop iterating through \na tuple and printing each item on a new line.")
    tup3 = (1, 2, 3, 4, 5 )
    for i in range(5):
        if i == 0:
             print tup3[0]
        if i == 1:
             print tup3[1]
        if i == 2:
             print tup3[2]
        if i == 3:
             print tup3[3]
        if i == 4:
             print tup3[4]







if __name__ == "__main__":
    main()
