def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = get_num_words(text)
    letter_dic = count_letters(text)
    print_report(num_words,letter_dic)

def get_text(book_path):
    with open(book_path) as file:
        file_contents = file.read()
    return file_contents

def get_num_words(text):
    return len(split_text(text))

def split_text(text):
    return text.split()

def count_letters(text):
    letter_dic = dict.fromkeys(set(text.lower()), 0)
    for letter in text:
        letter_dic[letter.lower()] += 1
    return letter_dic

def print_report(num_words,letter_dic):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    key,value = [],[]
    for letter in letter_dic:
        if letter.isalpha():
            key.append(letter)
            value.append(letter_dic[letter])

    for num1 in range(0,len(value)):
        for num2 in range(0,len(value)):
            if value[num1] > value[num2]:
                a = value[num2]
                value[num2] = value[num1]
                value[num1]= a
                b = key[num2]
                key[num2] = key[num1]
                key[num1] = b
                
    for a in range(0,len(key)):
            print(f"The '{key[a]}' character was found {value[a]} times")
    print("--- End report ---")

main()