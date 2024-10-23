#Briged McCarthy 2024
#Dollar to Euro conversion for computer programming

print('Dollars to Euros project')
print('Dollar to Euro conversion')
print('Briged McCarthy 10/23/24')

usrchoice = input("Would you like to convert dollars to euros?")

while usrchoice == "yes":
    dollar = float(input("Amount of $: "))
    euro = dollar * .94540
    print(euro)
    usrchoice = input("Would you like to convert dollars to euros again?")

while usrchoice == "yes":
    dollar = float(input("Amount of $: "))
    euro = dollar * .94540
    print(euro)