###Determines if the number is even or odd
'''
x = 12412412

if x%2 ==0:
    print("even")
else:
    print("odd")
'''


'''
def calculate_tip(bill, service_quality):
    tip_percentages = {
        'bad': 0.0,
        'okay': 0.15,
        'good': 0.20,
        'great': 0.25
    }
    tip_percentage = tip_percentages.get(service_quality.lower(), 0.0)
    
    tip = bill * tip_percentage

    return tip

bill_amount = float(input("Enter the bill amount: "))

service = input("Rate the service (bad, okay, good, great): ")

tip_amount = calculate_tip(bill_amount, service)

print(f"The tip amount is: ${tip_amount}")
'''

def print_factors(number):
    number = input("What number do you want to find the factors of: ")
    




'''def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = 12

print_factors(num)
'''