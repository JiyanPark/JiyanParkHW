def calculate_spam_confidence(filename):
    total_confidence = 0
    count = 0

    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.startswith("X-DSPAM-Confidence:"):
                    confidence_value = float(line.split(":")[1].strip())
                    total_confidence += confidence_value
                    count += 1

        if count > 0:
            average_confidence = total_confidence / count
            print(f"Average spam confidence : {average_confidence:.12f}")
        else:
            print("No confidence values found in the file.")

    except FileNotFoundError:
        print(f"File cannot be opened : {filename}")

def main():
    filename = input("Enter a file name : ")
    calculate_spam_confidence(filename)

if __name__ == "__main__":
    main()
