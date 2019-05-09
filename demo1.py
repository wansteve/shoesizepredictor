from sklearn import tree
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier

#[height, weight, shoe size]
X=[[191,80,9], [177,70,10], [150,56,6], [133,42, 4], [155,32,8]]
Y=['male', 'male', 'female', 'female', 'male']

#clf = tree.DecisionTreeClassifier()
#clf = clf.fit(X, Y)
#prediction = clf.predict([[180,70,7]])
#print (prediction)

#clf1 = svm.SVC(gamma = 'scale')
#clf1 = clf1.fit(X, Y)
#prediction1 = clf1.predict([[180,70,7]])
#print (prediction1)


clf2 = RandomForestClassifier()
clf2 = clf2.fit(X, Y)
prediction2 = clf2.predict([[130,50,4]])
print (prediction2)
#(n_estimators=10, max_depth=None, min_samples_split=2, random_state=0)