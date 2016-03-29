  GNU nano 2.2.6                                       File: bayesline_crossvalid.py                                                                                     

import graphlab
import numpy


train = graphlab.SFrame.read_csv('bayesline.train', delimiter=' ', column_type_hints=[float, float, int, int, float, float, float])
labels = graphlab.SFrame.read_csv('labels.train', column_type_hints=[bool], quote_char='\0')

train.add_columns(labels)

feat = [i for i in train.column_names() if i != 'out']

train_valid_shuffled = graphlab.toolkits.cross_validation.shuffle(train, random_seed=1)

def kth_start_end(n,k,kth):
    start = (n*kth)/k
    end = (n*(kth+1))/k-1
    return start, end+1

def get_kth_train(data, kth_start, kth_end, n):
    part1 = data[0:kth_start]
    part2 = data[kth_end+1:n]
    return part1.append(part2)

n = len(train)
accuracy = []
k = 10
for i in range(k):
    start, end = kth_start_end(n,k,i)
    valid_kth = train_valid_shuffled[start:end]
    train_kth = get_kth_train(train_valid_shuffled, start, end, n)
    m = graphlab.random_forest_classifier.create(train_kth, target='out', features=feat, validation_set=None)
    rfc_accuracy = sum(1 for pred, gold in zip(m.predict(valid_kth), valid_kth['out']) if pred == gold) / float(len(valid_kth))
    m = graphlab.nearest_neighbor_classifier.create(train_kth, target='out', features=feat)
    nnc_accuracy = sum(1 for pred, gold in zip(m.predict(valid_kth), valid_kth['out']) if pred == gold) / float(len(valid_kth))
    accuracy.append((rfc_accuracy, nnc_accuracy))

print 'Fold\tRFC\tNNC'
for i in range(k):
    print str(i)+'\t',
    print '\t'.join(map(str, accuracy[i]))
