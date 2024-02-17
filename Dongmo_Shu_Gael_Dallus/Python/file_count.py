import re 

#count_words takes a file path as input and returns two values: the total number of 
#words in the file and a dictionary containing the occurrences of each word.
def count_words(file_path):
    word_count = 0
    #word_occurrences dictionary stores the occurrences of each word.
    word_occurrences = {}

    with open(file_path, 'r') as file:
        #For each line, we use the split() method to split it into a list of words. 
        #By default, split() splits the line at whitespace characters, such as spaces or tabs, and returns a list of the words
        for seperate in file:
            #Makes the splitting case insensitive
            words = seperate.lower().split()
            word_count += len(words)
            for word in words:
                if word in word_occurrences:
                    word_occurrences[word] += 1
                else:
                    word_occurrences[word] = 1
        #The above iterate over each word in the words list. For each word, we check if it already exists in the word_occurrences dictionary. 
        #If it does, we increment its value by 1. If it doesn't, we add it to the dictionary with an initial value of 1

    return word_count, word_occurrences


def main():
    file_path = "./shakespeare.txt"
    target_word = input("Enter the word to search for: ").lower()

    total_words, occurrences = count_words(file_path)

    print("Total number of words:", total_words)
    #occurrences.get(target_word, 0) expression retrieves the value associated with the target_word key from the occurrences dictionary. 
    #If the key is not found, it returns 0
    print("Occurrences of the word '{}': {}".format(target_word, occurrences.get(target_word, 0)))


if __name__ == '__main__':
    main()