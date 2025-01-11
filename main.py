







def main():
    file = "books/frankenstein.txt"
    text = load_text(file)
    words = string_to_words(text)
    count = count_words(words)
    print(f"{count} words")
    
def count_words(words):
    count = 0
    for w in words:
        count += 1
        print(f"found word {count}")
    return count

def string_to_words(text):
    words = text.split()
    return words

def load_text(file):
    with open(file) as f:
        text = f.read()
    return text


main()