""" this module takes user input.........."""
num1 = raw_input("please enter first number : ")
num2 = raw_input("please enter second number : ")

if len(str(num1)) and len(str(num2)) == 2:
	print 'it is two digit number', num1,num2

elif len(str(num1)) and len(str(num2)) == 3:
	print 'it is three digit number', num1,num2

if len(str(num1)) == 2 and len(str(num2)) == 3:
	print "first number is two digit" ,num1
	print "second number is three digit",num2

elif len(str(num1)) == 3 and len(str(num2)) == 2:
	print "first number is three digit" ,num1
	print "second number is two digit" ,num2

else:
	print num1,num2


