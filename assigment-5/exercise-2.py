def computepay(hours, rate):
    if hours > 40:
        return 40 * rate + (hours - 40) * 1.5 * rate
    else:
        return hours * rate

def main():
    try:
        hours = float(input("Enter Hours: "))
        rate = float(input("Enter Rate: "))
        pay = computepay(hours, rate)
        print(f"Pay: {pay:.2f}")
    except ValueError:
        print("Error, please enter numeric input")

# Call the main function
if __name__ == "__main__":
    main()
