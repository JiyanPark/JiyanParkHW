def count_characters(s):
    uppercase = 0
    lowercase = 0
    numbers = 0
    others = 0
    
    for char in s:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        elif char.isdigit():
            numbers += 1
        else:
            others += 1
            
    return uppercase, lowercase, numbers, others

def main():
    input_string = input("Please enter string: ")
    uppercase, lowercase, numbers, others = count_characters(input_string)
    print("- Uppercase letters:", uppercase)
    print("- Lowercase letters:", lowercase)
    print("- Numbers:", numbers)
    print("- Other characters:", others)

# Call the main function
if __name__ == "__main__":
    main()
