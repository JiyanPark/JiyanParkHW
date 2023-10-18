def process_string(s):
    # Remove special characters
    for char in [';', '.', '!', '?']:
        s = s.replace(char, '')
    
    # Convert to uppercase
    return s.upper()

def main():
    while True:
        input_string = input("Please enter string: ")
        if input_string == 'done':
            print("Bye !")
            break
        else:
            print(process_string(input_string))

# Call the main function
if __name__ == "__main__":
    main()
