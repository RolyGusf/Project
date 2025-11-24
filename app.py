print("Welcome to my Python program!")
hours = input("How many hours did you study today? ")
weekly_hours = hours * 7
print(f"You are on track to study {weekly_hours} hours this week.")
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()
