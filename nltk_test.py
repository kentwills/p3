import nltk
import string

def main():
    text = word_tokenize("And now for something completely different")
    print nltk.pos_tag(text)

def word_tokenize(sentence):
    return sentence.split(" ")

if __name__ == "__main__":
    main()