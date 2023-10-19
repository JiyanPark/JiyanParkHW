def compare_words(word1, word2):
    if word1 < word2:
        return f"{word1} comes first"
    elif word1 > word2:
        return f"{word2} comes first"
    else:
        return "Both words are the same"

def main():
    while True:
        words_input = input("Please enter two words: ")

        if words_input.strip().lower() == 'done' or not words_input:
            print("-- bye !!")
            break

        words = words_input.split()

        if len(words) != 2:
            continue

        result = compare_words(words[0], words[1])
        print(result)

# Call the main function
if __name__ == "__main__":
    main()
