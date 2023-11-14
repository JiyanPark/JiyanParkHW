file_name = "romeo.txt"  
with open(file_name, 'r') as file:
        new_list = []
        for line in file:
            out_words = line.split()
            for word in out_words:
                if word not in new_list:
                    new_list.append(word)
        new_list.sort()
        output = "[" + ', '.join(["'{}'".format(word) for word in new_list]) + "]"
        print(output)