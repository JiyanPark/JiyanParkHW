print("Welcome to the Time Traveler's Converter!")
print("Imagine you're a time traveler, converting seconds into time units.")

seconds = int(input("Enter the number of seconds: "))

hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

print("You've traveled in time and found yourself in:")
print(f"{hours} hours, {minutes} minutes, and {seconds} seconds!")
print("Time flies when you're having fun, or in this case, time traveling!")
