from sklearn.linear_model import LinearRegression
from sklearn.ensemble import AdaBoostRegressor, BaggingRegressor, ExtraTreesRegressor, GradientBoostingRegressor
from sklearn.compose import TransformedTargetRegressor
from sklearn.cross_decomposition import PLSRegression
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.linear_model import ARDRegression, BayesianRidge, ElasticNet, ElasticNetCV, HuberRegressor, Lasso, LassoCV
from sklearn.linear_model import LassoLarsCV, LassoLars, LassoLarsIC, Lars, LarsCV, MultiTaskLasso, MultiTaskLassoCV
from sklearn.linear_model import OrthogonalMatchingPursuit, OrthogonalMatchingPursuitCV, PassiveAggressiveRegressor
from sklearn.linear_model import Ridge, RidgeCV, RANSACRegressor, SGDRegressor, TheilSenRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.svm import LinearSVR, NuSVR, SVR
from sklearn.tree import DecisionTreeRegressor, ExtraTreeRegressor

from sklearn.metrics import mean_squared_error
from numpy import sqrt

regressors = [
    LinearRegression, AdaBoostRegressor, BaggingRegressor, ExtraTreeRegressor, GradientBoostingRegressor, 
    TransformedTargetRegressor, PLSRegression, DummyRegressor, RandomForestRegressor, GaussianProcessRegressor, ARDRegression, 
    BayesianRidge, ElasticNet, ElasticNetCV, HuberRegressor, MultiTaskLasso, MultiTaskLassoCV, OrthogonalMatchingPursuit, 
    OrthogonalMatchingPursuitCV, PassiveAggressiveRegressor, Ridge, RidgeCV, RANSACRegressor, SGDRegressor, TheilSenRegressor, 
    KNeighborsRegressor, MLPRegressor, NuSVR, SVR, DecisionTreeRegressor, ExtraTreeRegressor
]

regressors_str = [
    'LinearRegression', 'AdaBoostRegressor', 'BaggingRegressor', 'ExtraTreeRegressor', 'GradientBoostingRegressor', 
    'TransformedTargetRegressor', 'PLSRegression', 'DummyRegressor', 'RandomForestRegressor', 'GaussianProcessRegressor', 
    'ARDRegression', 'BayesianRidge', 'ElasticNet', 'ElasticNetCV', 'HuberRegressor', 'MultiTaskLasso', 'MultiTaskLassoCV', 
    'OrthogonalMatchingPursuit', 'OrthogonalMatchingPursuitCV', 'PassiveAggressiveRegressor', 'Ridge', 'RidgeCV', 'RANSACRegressor', 
    'SGDRegressor', 'TheilSenRegressor', 'KNeighborsRegressor', 'MLPRegressor', 'NuSVR', 'SVR', 'DecisionTreeRegressor', 
    'ExtraTreeRegressor'
]

def predict(Regressor, x, y, new_x):
    return Regressor().fit(x, y).predict(new_x)

def accuracy(Regressor, x, y):
    return (1 - (sqrt(mean_squared_error(y, Regressor().fit(x, y).predict(x))) / y).mean())