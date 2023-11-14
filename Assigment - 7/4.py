integers = []
print("Typing 'done' will exit the program!")

while True:
    int_integers = input("Please enter an integer: ")
    
    if int_integers.lower() == 'done':
        break
    try:
        num = int(int_integers)
        integers.append(num)
        avg = sum(integers) / len(integers)
        print(f"[{', '.join(map(str, integers))}] , average = {avg:.2f}")
    
    except ValueError:
        print("It is not an integers, input integer again!")

print("--- Bye !! ---")