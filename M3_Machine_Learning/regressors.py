import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn import tree
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import HistGradientBoostingRegressor
from catboost import CatBoostRegressor
from lightgbm import LGBMRegressor
from xgboost import XGBRegressor

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import SGDRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn import linear_model
from sklearn.neighbors import RadiusNeighborsRegressor


tree_regressors = {
    "Decision_tree_regressor": DecisionTreeRegressor(),
    "AdaBoost_Regressor": AdaBoostRegressor(),
    "Extra_tress_Regressor": ExtraTreesRegressor(),
    "Random_Forest_Regressor": RandomForestRegressor(),
    "GBM_regressor": GradientBoostingRegressor(),
    "HGB_regressor": HistGradientBoostingRegressor(),
    "CATBoost_regressor": CatBoostRegressor(verbose=0),
    "LightGBM_regressor": LGBMRegressor(),
    "XGBRegressor": XGBRegressor(),
}

multi_regressors = {
    "Linear_regression": LinearRegression(),
    "Ridge_regressor": Ridge(),
    "SVM_regressor": SVR(),
    "MLP_regressor": MLPRegressor(),
    "SGD_regressor": SGDRegressor(),
    "KNN_regressor": KNeighborsRegressor(),
    "BR_regressor": BayesianRidge(),
    "RNN_regressor": RadiusNeighborsRegressor(),
}
