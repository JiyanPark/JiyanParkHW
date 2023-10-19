def extract_hosts(filename):
    hosts = set() 
    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.startswith("From:"):
                    email = line.split()[1]
                    host = email.split('@')[1]
                    hosts.add(host)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    for host in hosts:
        print(host)
    print(f"Total {len(hosts)} hosts printed")

def main():
    filename = "mbox.txt"
    extract_hosts(filename)

if __name__ == "__main__":
    main()
