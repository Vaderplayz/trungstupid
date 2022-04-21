#defining the amount list
daily = []
def checker(amount):
	status = ""
	if amount <= 30 and type(amount) == int:
		#enter if smaller or equal than 30 situation here
		status = "Excellent"
	elif amount > 30 and type(amount) == int:
		#enter if larger than 30 situation here
		status = "Poor"
	else:
		status = "Error"
	return status
def getAmount():
	global daily
	#check the amount of number in array
	if len(daily) == 31:
		print("Reseting array")
		daily = []
	print(daily)
	#this can only be input once, if wanted to have multiple input, wrap this in a while True loop
	while True:
		try:
			amount = int(input("%> "))
		except TypeError:
			print("Variable entered is not integer")
	
		if checker(amount=amount) == "Excellent":
			print("Your water usage for today is great!")
			daily.append(amount)
			break
		elif checker(amount=amount) == "Poor":
			print("The amount you entered as exceeded the allowed paramenters. Please try again")

if __name__ == "__main__":
	while True:
		getAmount()
	