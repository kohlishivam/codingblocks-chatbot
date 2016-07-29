class test():
	x=0
	def __init__(self,name1,age1):
		self.name=name1
		self.age=age1
		test.x=test.x+1

test1=test('vishrut',19)
a=[test('vishrut',19)]*11
# print test1.name	
# test2=test('vishrut',19)
# test3=test('vishrut',19)
# test4=test('vishrut',19)
# test5=test('vishrut',19)
# test6=test('vishrut',19)
# test7=test('vishrut',19)
# test8=test('vishrut',19)
# test9=test('vishrut',19)
# test10=test('vishrut',19)
# test11=test('vishrut',19)
print test.x
