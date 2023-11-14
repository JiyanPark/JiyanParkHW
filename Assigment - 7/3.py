file_name = 'mbox.txt'
with open(file_name, 'r') as file:
        words = []
        for line in file:
            if line.startswith('From ') and not line.startswith('From: '):
                senders = line.split()[1]
                words.append(senders)
                print(senders)

        count = len(words)
        print("Total", count ,"lines were printed")
    