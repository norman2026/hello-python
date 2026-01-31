# Python day 2

message = " learning in fun "
first_name = "Norman"
last_name = "Smith"
full_name = first_name + " " + last_name

price = 79.99
vat_rate = 0.20

vat = price * vat_rate
total = price + vat


print (message)
print (message.upper())
print (message.lower())
print (message.strip())

print ("\n")

print(f"My Fullname is: {full_name}")


#working with numbers



user_input = "50"

print(user_input + user_input)   # This joins text

number = int(user_input)

print(number + number)           # This adds numbers




print(f"Original price: £{price}")
print(f"VAT amount: £{vat}")
print(f"Total price: £{total}")
