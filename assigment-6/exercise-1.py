def convert_to_uppercase(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines, start=1):
                print(f"LINE NUMBER : {i}\n{line.strip().upper()}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

def main():
    filename = input("Enter a file name: ")
    convert_to_uppercase(filename)

if __name__ == "__main__":
    main()
