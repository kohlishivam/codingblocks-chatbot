def square (a) : #declaration of function 
    'this function calculates the square of the given number'#this is the documentation string
    q=a**2
    return q

if  __name__=='__main__': # __name__ is an attribute for any module and when the module is run directly by python itsname.py it is assigned a value __main__


    a= raw_input("enter the number bc")#for input in module

    b= square(7)   # we use type casting here because every input in pyhton is stored as a string so thats why we use type casting

    print b  
    print square.__doc__  #printing the documentation string
else:
	print'i am being imported'
                                                                                               