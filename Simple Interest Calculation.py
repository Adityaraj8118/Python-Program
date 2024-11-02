def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100
P = 400000  # Principal amount
R = 4    # Rate of interest
T = 10  # Time in years
interest = simple_interest(P, R, T)
print(f"Simple Interest for {T} years: {interest}")
