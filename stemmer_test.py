from nltk import stem

def main():
    stemmer=stem.PorterStemmer()
    text = "completely"
    print stemmer.stem(text)

def word_tokenize(sentence):
    return sentence.split(" ")

if __name__ == "__main__":
    main()