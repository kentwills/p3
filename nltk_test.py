import nltk
import string

def main():
    tree()
    #text = word_tokenize("And now for something completely different")
    #print nltk.pos_tag(text)

def word_tokenize(sentence):
    return sentence.split(" ")


def tree():
    data = {}
    fname = 'Science-parsed.de'
    with open(fname) as f:
        content = f.readlines()
    for c in content:
        try:
            test = nltk.Tree.fromstring(c.decode('utf-8')).pos()
            for t in test:
                data[t[0]] = t[1]
        except:
            print c

    return data

if __name__ == "__main__":
    main()