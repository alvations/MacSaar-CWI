# Zipfian and Character-level features for Complex Word Identification

This is an implementation of our submission to the Complex Word Identification task (CWI) in SemEval-2016. The system is based on the assumption that complex words are likely to be less frequent and on average longer than words considered to be simple.

# Usage

```
git clone https://github.com/alvations/MacSaar-CWI.git
cd MacSaar-CWI
wget https://www.dropbox.com/s/398p08vo5q17ggu/dslcc-cwi.zip
unzip dslcc-cwi.zip
# Extract features from the training data (bayesline.train) and DSLCC
python bayesline.py
# Train the classifier and generate the predictions
python bayesline-gl.py > MACSAAR-NNC.txt
```

# Nitty-Gritty

**What tool did you use to calculate the language model probabilities?**

We did not use language model probabilities. You might be mistake when we have a feature call "word-level trigram density". We calculate the density by computing the sum probability of the character trigrams (normalized by the sum of all possible trigrams within the word). 

First, we collated all trigram probabilities from the trigram counts from the [English subset of the DSLCC v1.0 dataset](https://github.com/Simdiva/DSL-Task) and produce a lookup table for every trigram and it's probabiliity, see https://github.com/alvations/MacSaar-CWI/blob/master/bayesline.py#L15. For a given the word, e.g. `purgation that produces the following character trigrams {pur, urg, rga, gat, ati, tio, ion}, we sum the probabilities for these trigram and divided it by 7. 

**Did you do any parameter tuning?**

No, we use the default implementation of the Graphlab classifiers without tuning. There was no validation/development set provided by the task organizers. 

**Did you do any feature normalization?**

No, we did not explicitly normalize the features.

**Why do you use word length and word frequency as a feature? Do you assume that longer words and less frequent are more complex?**

Because it is an intuitive feature but this would have to be empirically proven outside the scope of the shared task. It is worth noting that the best performing team PLUJAGH-SEWDEFF in the CWI task, uses a frequency threshold statistics. Future studies can explore the corrleation between word length, word freqency and word complexity.

**Why are all your script named Bayesline?**

It's the first proper classification task that Liling Tan has done using standard machine learning libraries in his PhD journey. And from it we created the [DSL shared task](https://github.com/Simdiva/DSL-Task) and the DSL Corpus Collection. The naming here is just a tribute to the that since this is the last classification task he's doing during his PhD.


# Cite

Marcos Zampieri, Shervin Malmasi, Liling Tan and Josef van Genabith. 2016. MacSaar at SemEval-2016 Task 11: Zipfian and Character-level features for Complex Word Identification. In SemEval-2016. San Diego, USA (forthcoming)

```

```
