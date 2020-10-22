import re


def main():

    def split_line(line):
        return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

    dictionary = open("dictionary.txt")
    dictionary_list = []
    for line in dictionary:
        line = line.strip()
        dictionary_list.append(line)
    dictionary.close()

    print("--- Linear Search ---")
    story = open("AliceInWonderLand200.txt")

    line_number = 0
    for line in story:
        line_number += 1
        word_list = split_line(line)
        for word in word_list:
            list_pos = 0
            while list_pos < len(dictionary_list) and word.upper() != dictionary_list[list_pos]:
                list_pos += 1
            if list_pos == len(dictionary_list):
                print("Potential misspelling of the word ", word, " on line", str(line_number))
    story.close()

    print("--- Binary Search ---")
    story = open("AliceInWonderLand200.txt")

    line_number = 0
    for line in story:
        line_number += 1
        word_list = split_line(line)
        for word in word_list:
            upper_bound = len(dictionary_list) - 1
            lower_bound = 0
            found = False
            while lower_bound <= upper_bound and not found:
                middle = (lower_bound + upper_bound) // 2
                if dictionary_list[middle] < word.upper():
                    lower_bound = middle + 1
                elif dictionary_list[middle] > word.upper():
                    upper_bound = middle - 1
                else:
                    found = True
            if not found:
                print("Potential misspelling of the word", word, "on line", str(line_number))
    story.close()


main()
