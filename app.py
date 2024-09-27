###Determines if the number is even or odd
'''
x = 12412412

if x%2 ==0:
    print("even")
else:
    print("odd")
'''

###Tip
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

###Greatest common factor 
'''
try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    
    while b != 0:    #Until b does equal to 0: keep doing this proccess
        remainder = a % b   #Remainder is a % b     ##Let's say a = 24, and b is 20: a%b = 4   remainder = 4 
        a = b                                                          # a = 20  b = 4   # remainder = 0    ## a=4 b=0 -- So GCf = A
        b = remainder
    
    print(f"The greatest common factor is: {a}")
except ValueError:
    print("Enter valid integers."
    '''








