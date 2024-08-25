# Script to calculate simple interest

# Prompt user for principal, rate of interest, and time
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

# Calculate simple interest
interest = (principal * rate * time) / 100

# Display the result
print(f"The Simple Interest is: {interest:.2f}")
