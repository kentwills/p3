# Word SimpleEF

# Sentence SimpleFF

# We develop features by adding a name and a count, the name is constructed based on context
def word_left(sentence, index_word, num_left, feats):
    # nonzero index
    if (index_word-num_left) < 0:
        return

    feature_string = 'wl_%s_%s' % (num_left, sentence[index_word-num_left])
    feats[feature_string] += 1

def word_right(sentence, index_word, num_right, feats):
    # nonzero index
    if (index_word+num_right) < len(sentence):
        return

    feature_string = 'wl_%s_%s' % (num_right, sentence[index_word-num_right])
    feats[feature_string] += 1

# Pair

def noun_to_the_left():
    return