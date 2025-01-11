 
    
def count_words(words):
    count = 0
    for w in words:
        count += 1
    return count

def string_to_words(text):
    words = text.split()
    return words

def load_text(file):
    with open(file) as f:
        text = f.read()
    return text

def count_letters(text):
    letters = {}
    for char in text:
        lowered = char.lower()
        if lowered in letters:
            letters[lowered] += 1
        else:
            letters[lowered] = 1
    return letters

def sort_on(d):
    return d["num"]

def letters_sorted_by_count(letters):
    sorted_list = []
    for letter in letters:
        sorted_list.append({"char": letter, "num":letters[letter]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
        
def main():
    file = "books/frankenstein.txt"
    text = load_text(file)
    words = string_to_words(text)
    count = count_words(words)
    letters = count_letters(text)
    sorted_letters = letters_sorted_by_count(letters)

    for letter in sorted_letters:
        if letter["char"].isalpha():
            print(f"The letter {letter["char"]} occurs {letter["num"]}")
        else:
            continue
 




main()