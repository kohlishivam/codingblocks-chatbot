student={}
print type(student)# dictionary works on key value pairs
#print dir(student)
student['name']='vishrut'#name is the key and vishrut is the value
student['age']='19'
print student.keys()#all the keys will be printed as a list
print type(student.keys())#list
for i in student.values():#for printing the values of list
	print i
print student.items()#both keys and values are printed as a list and a nested tuple	
print type(student.items())#list
print type(student.items()[0])#tuple
for i ,j in student.items():
    print 'the key is %s' %i,
    print ' the value is %s' %j


students={}
students['1']=student # for creating a nested dictionery to obtain details of many students 

print students

