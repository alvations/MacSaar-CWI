# -*- coding: utf-8 -*-

import os, sys, time, io
import cPickle as pickle
from collections import Counter

import string, random, time, re
from itertools import chain

rgx = r'(?=(...))'
def sent2ngrams_regex(text):
    return re.findall(rgx,text)


#chargrams = Counter()
#for line in io.open('dslcc.en.tok.txt', 'r', encoding='utf8'):
#    chargrams.update(sent2ngrams_regex(line.strip()))
#with open('dslcc.chargrams', 'wb') as fout:
#    pickle.dump(chargrams, fout)
dslcc_chargrams = pickle.load(open('dslcc.chargrams', 'rb'))
num_chargrams = float(sum(dslcc_chargrams.values()))
num_chargrams_uniq = float(len(dslcc_chargrams.keys()))

#dslcc_counts = Counter(io.open('dslcc.en.tok.txt', 'r', encoding='utf8').read().split())
#with open("dslcc.counts", "wb") as fout:
#    pickle.dump(dslcc_counts, fout)
dslcc_counts = pickle.load(open('dslcc.counts', 'rb'))
num_tokens = float(sum(dslcc_counts.values()))
num_uniq = float(len(dslcc_counts.keys()))
ranks = sorted(set(dslcc_counts.values()), reverse=True)
ranks.append(0)

def zipfian(word):
    count = dslcc_counts[word]
    percentile = ranks.index(count) / num_uniq
    prob = count / num_tokens
    return prob, percentile

def spelling(word):
    word_len = len(word)
    word_chargrams = sent2ngrams_regex(word)
    if word_len < 3:
        return word_len, 0
    word_chargram_prob = sum([dslcc_chargrams[ng]/num_chargrams for ng in word_chargrams]) / float(len(word_chargrams))
    return word_len, word_chargram_prob

def context(sent):
    sent_len = len(sent)
    sent_chargrams = sent2ngrams_regex(sent)
    sent_chargram_prob = sum([dslcc_chargrams[ng]/num_chargrams for ng in sent_chargrams]) / float(len(sent_chargrams))
    return sent_len, sent_chargram_prob

infile = sys.argv[1]
with io.open(infile, 'r', encoding='utf8') as fin:
    print "wordprob wordpercent wordlen sentlen wordcharprob sentprob wordsentprob"
    for line in fin:
        word, sent = line.split(' <s> ')
        wordprob, wordpercent = zipfian(word)
        wordlen, wordcharprob = spelling(word)
        sentlen, sentprob = context(sent)
        print wordprob, wordpercent, wordlen, sentlen, wordcharprob, sentprob, wordprob/sentprob
     




