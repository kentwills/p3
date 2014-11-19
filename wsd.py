from wsddata import *
import nltk
from nltk import stem

# simpleEFeatures(w) takes a word (in English) and generates relevant
# features.  At the very least, this should include the word identity
# as a feature.  You should also make it include prefix (two
# characters) and suffix (two characters) features.
def simpleEFeatures(w, wprob):
    feats = Counter()  # features are a mapping from strings (names) to floats (values)

    # generate a single feature with the word identity, called
    # w_EWORD, and value 1
    feats['w_' + w] = 1

    # generate a feature called wlogprob whose value is log(wprob)
    feats['wlogprob'] = log(wprob)

    # generate a feature corresponding to the two character prefix of
    # this word and a second feature for the two character suffix.
    # for example, on the word "happiness", generate "pre_ha" and
    # "suf_ss" as features.
    feats['pre_' + w[0:2]] = 1
    feats['suf_' + w[-2:]] = 1

    return feats


# simpleFFeatures(doc, i, j) asks for features about the French word
# in sentence i, position j of doc (i.e., at doc[i][j]).
def simpleFFeatures(doc, i, j):
    w = doc[i][j]

    feats = Counter()

    # generate a single feature with the (french) word identity
    feats[w] = 1

    # generate a feature corresponding to the two character prefix of
    # this word and a second feature for the two character suffix; same
    # deal about pre_ and suf_
    feats['pre_' + w[0:2]] = 1
    feats['suf_' + w[-2:]] = 1

    # generate features corresponding to the OTHER words in this
    # sentence.  for some other word "w", create a feature of the form
    # sc_w, where sc means "sentence context".  if a single word (eg.,
    # "the") appears twice in the context, the feature sc_the should
    # have value two.
    sent = doc[i]
    for a in range(len(sent)):
        # skip the actual word
        if a == j:
            continue
        feats['sc_' + sent[a]] += 1

    return feats


# simplePairFeatures(doc, i, j, ew, wprob) -- the first three are the
# same as for simpleFFeatures, the last two are the same as for
# simpleEFeatures.  we return features that are functions of both the
# french word (doc[i][j] and the english word w.
def simplePairFeatures(doc, i, j, ew, wprob):
    fw = doc[i][j]

    feats = Counter()

    # we have just one feature that asks if the fw and ew are
    # identical; this is really only useful for example on proper
    # nouns
    if fw == ew:
        feats['w_eq'] = 1

    return feats


def complexEFeatures(w, wprob):
    feats = Counter()  # features are a mapping from strings (names) to floats (values)

    # generate a single feature with the word identity, called
    # w_EWORD, and value 1
    feats['w_' + w] = 1

    # generate a feature called wlogprob whose value is log(wprob)
    feats['wlogprob'] = log(wprob)

    # generate a feature corresponding to the two character prefix of
    # this word and a second feature for the two character suffix.
    # for example, on the word "happiness", generate "pre_ha" and
    # "suf_ss" as features.
    stemmer = stem.PorterStemmer()
    stem_word = stemmer.stem(w)
    feats['stem_' + stem_word] = 1

    return feats


def complexFFeatures(doc, i, j):
    # cannot do until we change evaluation strings
    # w = unidecode(doc[i][j].lower())
    w = doc[i][j]

    feats = Counter()

    # generate a single feature with the (french) word identity
    feats[w] = 1

    # generate a feature corresponding to the two character prefix of
    # this word and a second feature for the two character suffix; same
    # deal about pre_ and suf_
    stemmer = stem.SnowballStemmer('french')
    stem_word = stemmer.stem(w.decode('utf-8')).encode('utf-8')
    feats['stem_' + stem_word] = 1

    # generate features corresponding to the OTHER words in this
    # sentence.  for some other word "w", create a feature of the form
    # sc_w, where sc means "sentence context".  if a single word (eg.,
    # "the") appears twice in the context, the feature sc_the should
    # have value two.
    sent = doc[i]

    for a in range(len(sent)):
        # skip the actual word
        if a == j:
            continue
        feats['sc_' + sent[a]] += 1




    #pull_out_all_pos(sent, feats)

    word_left(doc[i], j, 1, feats)
    word_left(doc[i], j, 2, feats)

    word_right(doc[i], j, 1, feats)
    word_right(doc[i], j, 2, feats)

    pos_left(doc[i], j, 1, feats)
    pos_left(doc[i], j, 2, feats)

    #pos_right(doc[i], j, 1, feats)
    #pos_right(doc[i], j, 2, feats)
    return feats


def hasNumbers(input_string):
    return any(char.isdigit() for char in input_string)


def complexPairFeatures(doc, i, j, ew, wprob):
    fw = doc[i][j]

    feats = Counter()

    # we have just one feature that asks if the fw and ew are
    # identical; this is really only useful for example on proper
    # nouns
    if fw == ew:
        feats['w_eq'] = 1

    return feats


def pull_out_all_pos(sent, feats):
    for a in range(len(sent)):
        word = sent[a]
        pos = data.get(word)
        if pos:
            feats[pos] += 1


def pos_left(sentence, index_word, num_left, feats):
    # nonzero index
    if (index_word - num_left) < 0:
        return

    word = sentence[index_word - num_left]
    pos = data.get(word)
    if pos:
        feature_string = 'posl_%s_%s' % (num_left, pos.decode('utf-8'))
        feats[feature_string] += 1


def pos_right(sentence, index_word, num_right, feats):
    # nonzero index
    if (index_word + num_right) >= len(sentence):
        return

    word = sentence[index_word + num_right]
    pos = data.get(word)
    if pos:
        feature_string = 'posr_%s_%s' % (num_right, pos.decode('utf-8'))
        feats[feature_string] += 1


# We develop features by adding a name and a count, the name is constructed based on context
def word_left(sentence, index_word, num_left, feats):
    # nonzero index
    if (index_word - num_left) < 0:
        return

    word = sentence[index_word - num_left]
    feature_string = 'wl_%s_%s' % (num_left, word)
    feats[feature_string] += 1


def word_right(sentence, index_word, num_right, feats):
    # nonzero index
    if (index_word + num_right) >= len(sentence):
        return

    word = sentence[index_word + num_right]
    feature_string = 'wr_%s_%s' % (num_right, word)
    feats[feature_string] += 1


def tree():
    data1 = tree_file('Science-parsed.de')
    return data1


def tree_file(fname):
    data = {}
    with open(fname) as f:
        content = f.readlines()
    for c in content:
        sentence = c.strip().decode('utf-8')
        if len(sentence) > 1:
            test = nltk.Tree.fromstring(sentence).pos()
            for t in test:
                data[t[0].encode('utf-8')] = t[1].encode('utf-8')
    print 'loaded pos'
    return data


if __name__ == "__main__":
    data = tree()
    (train_acc, test_acc, test_pred) = runExperiment('Science.tr', 'Science.te', complexFFeatures, complexEFeatures,
                                                     complexPairFeatures, quietVW=True)
    print 'training accuracy =', train_acc
    print 'testing  accuracy =', test_acc
    h = open('wsd_output', 'w')
    for x in test_pred:
        h.write(str(x[0]))
        h.write('\n')
    h.close()