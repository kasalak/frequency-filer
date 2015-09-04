import re

#convert text to all lower case
def word_frequency(text):
    words = {}
    for word in text.split():
        word = re.sub(r'[^A-Za-z]', ' ', word).lower()
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words

def top20(words):
    for k, v in sorted(words.items(), key=lambda c: c[1], reverse=True)[ :20]:
        print(a, b)

def get_text():
    given_file = print(input("Enter filename here. "))
    book = open(given_file)
    text = given_file.read()
    return text

def main():
    top20(word_frequency(get_text()))

if __name__ == '__main__':
    main()
