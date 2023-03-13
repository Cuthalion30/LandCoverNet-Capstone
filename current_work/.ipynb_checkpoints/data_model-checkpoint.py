import numpy as np
import pandas as pd
from lazypredict.Supervised import LazyClassifier
from sklearn.model_selection import train_test_split

# Read in the data
df = pd.read_csv('landcovernet_africa_data.csv')

# separate the data from the labels
# f1 (costal) and f2 (blue) are bands for landsat-8
X, Y = df[['f1', 'f2']], df.labels

# 80/20 split for the train/test
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=.2, random_state=1234)

# fit all models
clf = LazyClassifier(predictions=True)
models, predictions = clf.fit(X_train, X_test, y_train, y_test)
print(models)