#return sum of num1 and num2
def add(num1, num2):
	return num1 + num2

#num1 minus num2 (reuslt)	
def minus(num1, num2):
	return num1 - num2

#num1 devided by num2
def devide(num1, num2):
	return num1 / num2
	
#num1 multiply num2
def multi(num1, num2):
	return num1 * num2
	

		
def main():
	op = input("What operation? (+ - * / )= ")
	if(op != "+" and op != "-" and op != "*" and op != "/"):
		#invalid op
		print("Invalid operation.")
	else:
		num1 = int(input("Enter num1: "))
		num2 = int(input("Enter num2: "))
		print(" ")
		print("Result:")
		if(op == "+"):
			print(add(num1, num2))
		
		elif (op == "-"):
			print(minus(num1, num2))
		
		elif(op == "*"):
			print(multi(num1, num2))
		
		elif (op == "/"):
			print(devide(num1, num2))
		
main()
