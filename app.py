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
    if n <= 0:
        return "Please enter a positive integer."
    
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    
    return factors

def main():
    try:
        number = int(input("Enter a positive integer: "))
        factors = find_factors(number)
        print(f"The factors of {number} are: {factors}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
'''

###Greatest common factor 
'''
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

# Get user input
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    result = gcd(num1, num2)
    print(f"The GCF of {num1} and {num2} is {result}.")
except ValueError:
    print("Please enter valid integers.")'''




def gcd(a,b):
    if a%i == 0 and b%i == 0:
        

a = int(input("Enter the first number: "))
b = int(input("Enter your second number: "))


for i in (a, a+1):
    if a%i == 0 and b%i ==0:
