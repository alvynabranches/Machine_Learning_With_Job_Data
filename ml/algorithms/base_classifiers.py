from sklearn.calibration import CalibratedClassifierCV
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import AdaBoostClassifier, BaggingClassifier, ExtraTreesClassifier, GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.linear_model import LogisticRegression, PassiveAggressiveClassifier, Perceptron, RidgeClassifier, RidgeClassifierCV
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import LinearSVC, SVC
from sklearn.tree import DecisionTreeClassifier, ExtraTreeClassifier

from sklearn.metrics import accuracy_score

classifiers = [
    CalibratedClassifierCV, DummyClassifier, AdaBoostClassifier, BaggingClassifier, ExtraTreesClassifier, 
    GradientBoostingClassifier, RandomForestClassifier, GaussianProcessClassifier, LogisticRegression, 
    PassiveAggressiveClassifier, Perceptron, RidgeClassifier, RidgeClassifierCV, SGDClassifier, KNeighborsClassifier, 
    MLPClassifier, LinearSVC, SVC, DecisionTreeClassifier, ExtraTreeClassifier
]

classifiers_str = [
    'CalibratedClassifierCV', 'DummyClassifier', 'AdaBoostClassifier', 'BaggingClassifier', 'ExtraTreesClassifier', 
    'GradientBoostingClassifier', 'RandomForestClassifier', 'GaussianProcessClassifier', 'LogisticRegression', 
    'PassiveAggressiveClassifier', 'Perceptron', 'RidgeClassifier', 'RidgeClassifierCV', 'SGDClassifier', 'KNeighborsClassifier', 
    'MLPClassifier', 'LinearSVC', 'SVC', 'DecisionTreeClassifier', 'ExtraTreeClassifier'
]

def predict(self, Classifier, x, y, new_x):
    return Classifier().fit(x, y).predict(new_x)

def accuracy(self, Classifier, x, y):
    return accuracy_score(y, Classifier().fit(x, y).predict(x))
