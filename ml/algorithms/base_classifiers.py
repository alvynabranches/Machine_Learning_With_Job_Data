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

    LogisticRegression, DummyClassifier, AdaBoostClassifier, 
    BaggingClassifier, ExtraTreesClassifier, 
    GradientBoostingClassifier, RandomForestClassifier, GaussianProcessClassifier, 
    PassiveAggressiveClassifier, Perceptron, RidgeClassifier, 
    RidgeClassifierCV, SGDClassifier, KNeighborsClassifier, 
    MLPClassifier, LinearSVC, SVC, DecisionTreeClassifier, 
    ExtraTreeClassifier

]

classifiers_str = [

    'LogisticRegression', 'DummyClassifier', 
    'AdaBoostClassifier', 'BaggingClassifier', 'ExtraTreesClassifier', 
    'GradientBoostingClassifier', 'RandomForestClassifier', 
    'GaussianProcessClassifier', 
    'PassiveAggressiveClassifier', 'Perceptron', 
    'RidgeClassifier', 'RidgeClassifierCV', 'SGDClassifier', 'KNeighborsClassifier', 
    'MLPClassifier', 'LinearSVC', 'SVC', 
    'DecisionTreeClassifier', 'ExtraTreeClassifier'

]

def predict(Classifier, x, y, new_x):
    '''
        This function return out the predicts the new output of a following new input by a Classifier.
        Classifier: The Classifier class should be passed here.
        x: The x variable in the dataset.
        y: The y variable in the dataset.
        new_x: The new x which we want to predict the output of.
    '''
    return Classifier().fit(x, y).predict(new_x)

def accuracy(Classifier, x, y):
    '''
        This function is used to return out the accuracy of the Classifier.
        Classifier: The Classifier class should be passed here.
        x: The x variable in the dataset.
        y: The y variable in the dataset.
    '''
    return accuracy_score(y, Classifier().fit(x, y).predict(x))
