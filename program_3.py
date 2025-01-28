# Eliya Statema
# 1/28/25
# TOTAL PURCHASE

tax_rate = 0.07

print('''You are purchasing five items. Write the price of each item below. 
Do not include $ in your answer.
''')

print("ITEM 1")
item_1 = float(input("Price: "))

print("ITEM 2")
item_2 = float(input("Price: "))

print("ITEM 3")
item_3 = float(input("Price: "))

print("ITEM 4")
item_4 = float(input("Price: "))

print("ITEM 5")
item_5 = float(input("Price: "))

subtotal = item_1 + item_2 + item_3 + item_4 + item_5
sales_tax = subtotal * tax_rate
total = subtotal + sales_tax

print(f'''
SUBTOTAL: ${subtotal:.2f}
SALES TAX: ${sales_tax:.2f}
*** TOTAL: ${total:.2f} ***''')