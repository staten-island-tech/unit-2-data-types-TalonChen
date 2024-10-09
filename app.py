###Determines if the number is even or odd

'''
try:
    x = int(input("State your integer: "))
    if x%2 ==0:
        print("even")
    else:
        print("odd")
except ValueError: 
    print("Please enter a VALID INTEGER")
'''

###Tip  $$
'''
def calculate_tip(bill, service_quality):
    tip_percentages = {                #Dictionary 
        'bad': 0.0,
        'okay': 0.15,
        'good': 0.20,
        'great': 0.25
    }
    tip_percentage = tip_percentages.get(service_quality.lower(), 0.0)  #urns anything from- bAd, BAD, Bad will all become bad, and if it's not found, then it will return to 0 (i think)
    
    tip = bill * tip_percentage

    return tip

bill_amount = float(input("Enter the bill amount: "))

service = input("Rate the service (bad, okay, good, great): ")

tip_amount = calculate_tip(bill_amount, service)

print(f"The tip amount is: ${tip_amount}")
'''

###Finds the factors of numbers
'''
def find_factors(n):
    factors = []
    for i in range(1, abs(n) + 1):  
        if n % i == 0: 
            factors.append(i)
    return factors

try:
    a = int(input("Enter a number to find its factors: "))
    
    factors = find_factors(a)
    print(f"The factors of {a} are: {factors}")  
except ValueError:
    print("Please enter a valid integer.")
'''

###Greatest common factor :)
def find_gcf(a, b):
    c = min(a, b)
    gcf = 1
    
    for i in range(1, c + 1):
        if a % i == 0 and b % i == 0:
            gcf = i  
    
    return gcf

a = int(input("First number: "))
b = int(input("Second number: "))
result = find_gcf(a, b)
print(f"The GCF of {a} and {b} is {result}.")