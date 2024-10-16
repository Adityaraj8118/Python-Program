#An Armstrong number is a number that is equal to the sum of its digits, each raised to a power. For example, 153 is an Armstrong number because 1^3 (1) + 5^3 (125) + 3^3 (27) equals 153 
def is_armstrong(num):
    digits = [int(digit) for digit in str(num)]
    return num == sum(digit ** len(digits) for digit in digits)
num = 370
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
