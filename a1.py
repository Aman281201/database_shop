


def show_menu():
	print("==========================================================================================")
	head = "MY BAZAR"
	print(head.center(90))
	print("==========================================================================================")
	print("Hello! welcome to my grocery store!")
	print("following are the items available in the shop", "\n")
	print("__________________________________________________________________________________________")
	print("|   CODE       |    DESCRIPTION        |        CATEGORY         |           COST(Rs)    |")
	print("------------------------------------------------------------------------------------------")
	print("|     0        |      T-shirts         |        Apparels         | 500                   | ")
	print("|     1        |      Trousers         |        Apparels         | 600                   | ")
	print("|     2        |      Scarf            |        Apparels         | 250                   | ")
	print("|     3        |      Smartphone       |        Electronics      | 20,000                | ")
	print("|     4        |      iPad             |        Electronics      | 30,000                | ")
	print("|     5        |      Laptop           |        Electronics      | 50,000                | ")
	print("|     6        |      Eggs             |        Eatables         | 5                     | ")
	print("|     7        |      Chocolate        |        Eatables         | 10                    | ")
	print("|     8        |      Juice            |        Eatables         | 100                   | ")
	print("|     9        |      Milk             |        Eatables         | 45                    | ")
	print("------------------------------------------------------------------------------------------")
	print("\n")


def get_regular_input():
	'''
	Description: Takes space separated item codes (only integers allowed). 

	
	Parameters: No parameters
	
	Returns: Returns a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i. 
	'''

	orders1 = []
	orders = input("Enter the Item codes (space separated):").split()
	for i in range(0, len(orders)):
		if (orders[i] == '0' or orders[i] == '1' or orders[i] == '2' or orders[i] == '3' or orders[i] == '4' or
				orders[i] == '5' or orders[i] == '6' or orders[i] == '7' or orders[i] == '8' or orders[i] == '9'):
			orders1.append(int(orders[i]))

		else:
			print("input at " + str(i+1) + "th index in wrong")
			continue
	li = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for i in orders1:
		li[i] = li[i] + 1
	return li


def get_bulk_input():
	'''
	Description: Takes inputs (only integers allowed) from a bulk buyer. 

	
	Parameters: No parameters
	
	Returns: Returns a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	'''
	print("__________________________________________________________________________________________")
	print("Enter Item and Quantities")
	print("------------------------------------------------------------------------------------------")
	li = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	flag = True

	name = ["T-Shirts","Trousers", "Scarf", "Smartphone", "iPad", "Laptop", "Eggs", "Chocolate", "Juice", "Milk"]
	while flag:
		n = input("Enter code and quantities (leave blank to stop)")

		if n == '':
			print("Your Order has been finalized")
			flag = False
		elif int(n.split()[0]) >= 0 and int(n.split()[0]) <=9:
			if int(n.split()[1]) >= 0:
				li[int(n.split()[0])] = li[int(n.split()[0])] + int(n.split()[1])
				print("You added " + str(int(n.split()[1])) + " " + name[int(n.split()[0])])
			else:
				print("pleas enter correct quantity")
		elif int(n.split()[1]) < 0:
			print("please enter correct code and quantity")
		else:
			print("please enter correct code")
	return li


def print_order_details(quantities):
	'''
	Description: Prints the details of the order
	
	Parameters: Takes a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	
	Returns: No return value
	'''
	index = [[0, "T-shirts", "Apparels", 500], [1, "Trousers", "Apparels", 600], [2, "Scarf", "Apparels", 250],
		  [3, "Smartphone", "Electronics", 20000], [4, "iPad", "Electronics", 30000],
		  [5, "Laptop", "Electronics", 50000],
		  [6, "Eggs", "Eatables", 5], [7, "Chocolate", "Eatables", 10], [8, "Juice", "Eatables", 100],
		  [9, "Milk", "Eatables", 45]]
	cat = ["Apparels", "Electronics", "Eatables"]

	print("__________________________________________________________________________________________")
	print("Order Details")
	print("------------------------------------------------------------------------------------------")
	j = 1
	for i in range(0, len(quantities)):

		if quantities[i] != 0:
			print("["+str(j)+"] " + index[i][1] + " X " + str(quantities[i]) + " = Rs " + str(index[i][3]) + " * " + str(quantities[i]) + " = Rs " + str(index[i][3]*quantities[i]))
			j = j+1




def calculate_category_wise_cost(quantities):
	'''
	Description: Calculates the category wise cost using the quantities
	provided.

	Parameters: Takes a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	
	Returns: A 3-tuple of integers in the following format: 
	(apparels_cost, electronics_cost, eatables_cost)
	'''
	print("__________________________________________________________________________________________")
	print("Category-Wise cost")
	print("------------------------------------------------------------------------------------------")
	a = (quantities[0]*500 + quantities[1]*600 + quantities[2]*250 , quantities[3]*20000 + quantities[4]*30000 + quantities[5]*50000 ,quantities[6]*5 + quantities[7]*10 + quantities[8]*100 + quantities[9]*45)
	print("Apparels = Rs " + str(a[0]))
	print("Electronics = Rs " + str(a[1]))
	print("Eatables = Rs " + str(a[2]), "\n")
	return a


def get_discount(cost, discount_rate):
	'''
	Description: This is a helper function. D
	
	Parameters: Takes 2 parameters:
	- cost: Integer
	- discount_rate: Float: 0 <= discount_rate <= 1

	Returns: The discount on the cost provided.
	'''
	return int(cost * discount_rate)


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
	'''
	Description: Calculates the discounted category-wise price, if applicable. 

	
	Parameters: Takes 3 integer parameters:
	- apparels_cost: 	cost for the category 'Apparels'
	- electronics_cost: cost for the category 'Electronics'
	- eatables_cost: 	cost for the category 'Eatables'
	
	Returns: A 3-tuple of integers in the following format: 
	(discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost). 
	'''
	app_dis_price = apparels_cost
	elec_dis_price = electronics_cost
	eat_dis_price = eatables_cost

	if get_discount(apparels_cost,0.1) >= 200:
		app_dis_price = apparels_cost - get_discount(apparels_cost,0.1)
	if get_discount(electronics_cost, 0.1) >= 2500:
		elec_dis_price = electronics_cost - get_discount(electronics_cost,0.1)
	if get_discount(eatables_cost, 0.1) >= 50:
		eat_dis_price = eatables_cost - get_discount(eatables_cost, 0.1)

	t = (apparels_cost, electronics_cost, eatables_cost)
	cost = (app_dis_price, elec_dis_price, eat_dis_price)
	cat = ["Apparels","Electronics","Eatables"]

	print("__________________________________________________________________________________________")
	print("Discounts")
	print("------------------------------------------------------------------------------------------")
	j = 1
	for i in range(0, 3):
		if cost[i] != t[i]:
			print("[" + cat[i] + "] Rs " + str(t[i]) + " - " + str(t[i] - cost[i]) + " = Rs " + str(cost[i]))

	print("\n\n")
	print("Total Discount = Rs " + str(t[0] - cost[0] + t[1] - cost[1] + t[2] - cost[2]))
	print("Total Cost = Rs " + str(cost[0] + cost[1] + cost[2]))
	print("\n")
	return cost

def get_tax(cost, tax):
	'''
	Description: This is a helper function.
	
	Parameters: Takes 2 parameters:
	- cost: Integer
	- tax: 	Float: 0 <= tax <= 1

	Returns: The tax on the cost provided.
	'''
	return int(cost * tax)


def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
	'''
	Description: Calculates the total cost including taxes.

	
	Parameters: Takes 3 integer parameters:
	- apparels_cost: 	cost for the category 'Apparels'
	- electronics_cost: cost for the category 'Electronics'
	- eatables_cost: 	cost for the category 'Eatables' 
	
	Returns: A 2-tuple of integers in the following format: 
	(total_cost_including_tax, total_tax)
	'''


	print("__________________________________________________________________________________________")
	print("Tax")
	print("------------------------------------------------------------------------------------------", "\n")

	tax_r = (0.1, 0.15, 0.05)
	f = (apparels_cost, electronics_cost, eatables_cost)
	cat = ["Apparels", "Electronics", "Eatables"]

	b = (apparels_cost + electronics_cost + eatables_cost + get_tax(apparels_cost, tax_r[0]) + get_tax(electronics_cost,
		tax_r[1]) + get_tax(eatables_cost, tax_r[2]), get_tax(apparels_cost, tax_r[0]) + get_tax(electronics_cost, tax_r[1])
		 + get_tax(eatables_cost, tax_r[2]))

	for i in range(0, 3):
		if f[i] != 0:
			print("[" + cat[i] + "] Rs " + str(f[i]) + " * " + str(tax_r[i]) + " = Rs " + str(
				get_tax(f[i], tax_r[i])))
	print("\n")
	print("Total Tax = Rs " + str(b[1]))
	print("Total cost = Rs " + str(b[0]))
	print("\n")

	return b

def apply_coupon_code(total_cost):
	'''
	Description: Takes the coupon code from the user as input (case-sensitive). 

	
	Parameters: The total cost (integer) on which the coupon is to be applied.
	
	Returns: A 2-tuple of integers:
	(total_cost_after_coupon_discount, total_coupon_discount)
	'''
	while True:
		print("Enter Coupon Code (leave blank to exit)")
		n = input()
		if n == '':
			print("No coupon code applied")
			return total_cost, 0

		elif n == "HELLE25":
			if total_cost >= 25000:
				print("coupon applied successfully")
				if total_cost*0.25 < 5000:
					a = total_cost*0.25
				else:
					a = 5000
				return total_cost - a, a
			else:
				print("You must shop for at least 25000 to avail this coupon")

		elif n == "CHILL50":
			if total_cost >= 50000:
				print("coupon applied successfully")
				if total_cost*0.25 < 10000:
					a = total_cost*0.25
				else:
					a = 10000
				return total_cost - a, a
			else:
				print("You must shop for at least 50000 to avail this coupon")
		else:
			print("Invalid coupon code")




def main():
	'''
	Description: This is the main function. This function will call the functions you have written
	above to design the logic.
	
	Parameters: No parameters
	
	Returns: No return value
	'''
	show_menu()
	z = True
	while z:
		res = input("Would you like to buy in bulk? (y or Y/n or N):")
		if res.lower() == 'n':
			print("__________________________________________________________________________________________")
			print("Enter the items you wish to buy")
			print("------------------------------------------------------------------------------------------")

			g = get_regular_input()
			z = False
		elif res.lower() == 'y':
			g = get_bulk_input()
			z = False
		else:
			print("invald reponse")
	print_order_details(g)
	cat_cost = calculate_category_wise_cost(g)
	dis_price = calculate_discounted_prices(cat_cost[0], cat_cost[1], cat_cost[2])
	tax_price = calculate_tax(dis_price[0], dis_price[1], dis_price[2])
	final_price = apply_coupon_code(tax_price[0])

	print("\n")
	print("money saved by coupons is Rs " + str(final_price[1]), "\n")
	print("Final Bill you have to pay is Rs " + str(final_price[0]), "\n")
	print("Thank you for visiting us")


if __name__ == '__main__':
	main()
