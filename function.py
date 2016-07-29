def square (a) : #declaration of function 
    q=a**2
    return q

if  __name__=='__main__': # __name__ is an attribute for any module and when the module is run directly by python itsname.py it is assigned a value __main__


    a= raw_input("enter the number bc")

    b= square(int(a))   

    print b  
else : 
    print __name__     