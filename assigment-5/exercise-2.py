def print_string_backwards(s):
    index = len(s) - 1
    while index >= 0:
        print(s[index])
        index -= 1

def main():
    input_string = input("Enter string: ")
    print("Input string =", input_string)
    print_string_backwards(input_string)

# Call the main function
if __name__ == "__main__":
    main()
