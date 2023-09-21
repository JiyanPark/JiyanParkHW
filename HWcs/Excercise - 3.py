def main():
    total = 0.0  # To keep track of the sum of numbers
    count = 0  # To keep track of the number of valid inputs

    while True:
        num = input("Enter a number: ")

        if num == "done":
            break  # Exit the loop

        try:
            value = float(num)
            total += value  # Update the total sum
            count += 1  # Update the count of valid numbers
        except ValueError:
            print("Invalid input. Enter a number.")

    # Displaying the results after breaking out of the loop
    if count != 0:  # To avoid division by zero for the average
        average = total / count
    else:
        average = 0.0

    print(f"Sum of input numbers: {total}")
    print(f"Number of input: {count}")
    print(f"Average of input numbers: {average}")

if __name__ == "__main__":
    main()
