product_list = "Lovely Loveseat, Stylish Settee, Luxurious Lamp"

lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white. "

stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black. "

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade. "

product_dictionary = {"Lovely Loveseat" : 254.00, "Stylish Settee" : 180.50, "Luxurious Lamp" : 52.15}

sales_tax = .088

customer_itemisation = ""

print("Product List:\n")
print(product_list)

customer_total = 0
finished = "n"

while finished.lower() == "n":

  selection = input("\nPlease enter the product you would like to purchase: ")

  quantity = input("\nPlease enter the number you would like to purchase: ")

  if selection.lower() == "lovely loveseat":
    customer_total += (product_dictionary["Lovely Loveseat"] * float(quantity))
    customer_itemisation += lovely_loveseat_description
    finished = input("\nHave you finished selecting items? (Y/N:) ")
    if finished.lower() == "y":
      break
  elif selection.lower() == "stylish settee":
    customer_total += (product_dictionary["Stylish Settee"] * float(quantity))
    customer_itemisation += stylish_settee_description
    finished = input("\nHave you finished selecting items? (Y/N:) ")
    if finished.lower() == "y":
      break
  elif selection.lower() == "luxurious lamp":
    customer_total += (product_dictionary["Luxurious Lamp"] * float(quantity))
    customer_itemisation += luxurious_lamp_description
    finished = input("\nHave you finished selecting items? (Y/N:) ")
    if finished.lower() == "y":
      break
  else:
    print("\nPlease enter a valid product name!")

customer_tax = (customer_total * sales_tax)
customer_total += customer_tax

print("\nCustomer Items:\n")
print(customer_itemisation)

format_customer_total = "{:.2f}".format(customer_total)
print(u"\xA3" + format_customer_total)