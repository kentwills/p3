from __future__ import unicode_literals
import nltk

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
        sentence = c.strip()
        if len(sentence) > 1:
            test = nltk.Tree.fromstring(sentence).pos()
            for t in test:
                data[t[0]] = t[1]

    return data

if __name__ == "__main__":
    main()