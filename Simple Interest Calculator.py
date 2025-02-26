def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

print("Simple Interest Calculator")
P = float(input("Enter Principal Amount: "))
R = float(input("Enter Annual Interest Rate (in %): "))
T = float(input("Enter Time (in years): "))

SI = simple_interest(P, R, T)

print(f"\nSimple Interest: {SI}")
print(f"Total Amount after {T} years: {P + SI}")
