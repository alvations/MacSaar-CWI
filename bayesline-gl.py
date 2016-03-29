import graphlab
import numpy


train = graphlab.SFrame.read_csv('bayesline.train', delimiter=' ', column_type_hints=[float, float, int, int, float, float, float])
labels = graphlab.SFrame.read_csv('labels.train', column_type_hints=[bool])
train.add_columns(labels)
#print train.print_rows(10)
test = graphlab.SFrame.read_csv('bayesline.test', delimiter=' ', column_type_hints=[float, float, int, int, float, float, float])
feat = [i for i in train.column_names() if i != 'out']
## Bad classifiers, ends up with all 0s
#m = graphlab.neuralnet_classifier.create(train, target='out', features=feat, validation_set=None)
#m = graphlab.svm_classifier.create(train, target='out', features=feat, validation_set=None)

## Good classifiers
#m = graphlab.random_forest_classifier.create(train, target='out', features=feat, validation_set=None) 
m = graphlab.nearest_neighbor_classifier.create(train, target='out', features=feat)

for i in m.predict(test):
    print i
