def calculate_salary(hours, rate):
    """Calculate salary based on hours and rate."""
    if hours > 40:
        overtime = (hours - 40) * rate * 1.5
        salary = (40 * rate) + overtime
    else:
        salary = hours * rate
    return salary

def main():
    try:
        hours = input("Enter hours worked: ")
        hours = int(hours)

        if "." in str(hours):
            print("Error: Hours should be an integer value.")
            return

        rate = input("Enter hourly rate: ")
        rate = float(rate)

        salary = calculate_salary(hours, rate)
        print(f"Salary: ${salary:.2f}")

    except ValueError:
        print("Error: Please enter valid numeric values for hours and rate.")
        return

if __name__ == "__main__":
    main()
