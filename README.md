# Zipfian and Character-level features for Complex Word Identification

This is an implementation of our submission to the Complex Word Identification task (CWI) in SemEval-2016. The system is based on the assumption that complex words are likely to be less frequent and on average longer than words considered to be simple.


# Nitty-Gritty

**What tool did you use to calculate the language model probabilities?**

We did not use language model probabilities. You might be mistake when we have a feature call "word-level trigram density". We calculate the density by computing the sum probability of the character trigrams (normalized by the sum of all possible trigrams within the word). 

First, we collated all trigram probabilities from the trigram counts in the training data and produce a lookup table for every trigram and it's probabiliity, see . For a given the word, e.g. `\textit{purgation} that produces the following character trigrams {pur, urg, rga, gat, ati, tio, ion}, we sum the probabilities for these trigram and divided it by 7. 

**Did you do any parameter tuning?**

No, we use the default implementation of the Graphlab classifiers without tuning. There was no validation/development set provided by the task organizers. 

**Did you do any feature normalization?**

No, we did not explicitly normalize the features.

**Why do you use word length and word frequency as a feature? Do you assume that longer words and less frequent are more complex?**

Because it is an intuitive feature but this would have to be empirically proven outside the scope of the shared task. It is worth noting that the best performing team PLUJAGH-SEWDEFF in the CWI task, uses a frequency threshold statistics. Future studies can explore the corrleation between word length, word freqency and word complexity.


# Cite

Marcos Zampieri, Shervin Malmasi, Liling Tan and Josef van Genabith. 2016. MacSaar at SemEval-2016 Task 11: Zipfian and Character-level features for Complex Word Identification. In SemEval-2016. San Diego, USA (forthcoming)

```

```
