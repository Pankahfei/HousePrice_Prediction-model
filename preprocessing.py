import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pickle
import re

from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet, LogisticRegression,LassoCV
from sklearn.neighbors import KNeighborsClassifier
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.preprocessing import PolynomialFeatures, StandardScaler, LabelEncoder, OneHotEncoder,OrdinalEncoder
from sklearn.model_selection import train_test_split,cross_val_score, GridSearchCV
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline
from scipy.stats import norm
from scipy import stats
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.compose import ColumnTransformer
from scipy.special import boxcox1p

##Preprocessing of data - as close to general modal as possible
def preprocessing(df_test):
 
 columns_dropped = ['Pool QC','Misc Feature','Alley','Fence','Fireplace Qu','Lot Frontage','Garage Finish','Garage Qual','Garage Yr Blt','Garage Cond','Garage Type','Pool Area','Fireplaces','Garage Area','Garage Cars','Mas Vnr Area','Mas Vnr Type','Misc Val','3Ssn Porch','Low Qual Fin SF','Screen Porch','BsmtFin SF 2','Enclosed Porch']
 coll_columns_drop = ['BsmtFin SF 1','Bsmt Unf SF','1st Flr SF','2nd Flr SF','Year Remod/Add','TotRms AbvGrd','Exter Qual','Exter Cond','Bsmt Qual','Bsmt Cond']
 skew_feature = ['Lot Area','Open Porch SF', 'Wood Deck SF','Gr Liv Area'] 

 ss = pickle.load(open('./standardscaler.pkl', 'rb'))
 trans = pickle.load(open('./onehot.pkl', 'rb')) 
 
 new_idx = trans.get_feature_names()
 df_test[['MS SubClass','Yr Sold','Mo Sold','Land Slope']] = df_test[['MS SubClass','Yr Sold','Mo Sold','Land Slope']] .astype(str)

 df_test = Categorical_feature_engineering(df_test)
 numerical_idx_test = df_test.select_dtypes(include = ['int64', 'float64']).columns
 categorical_idx_test = df_test.select_dtypes(include = ['object']).columns

 df_test.drop(columns=columns_dropped,inplace=True)
 df_test=df_test.fillna(0)
 df_test = df_test.drop(columns=coll_columns_drop)

 numerical_idx_test1 = df_test.select_dtypes(include = ['int64', 'float64']).columns
 categorical_idx_test1 = df_test.select_dtypes(include = ['object']).columns
 df_test_temp1 = df_test[categorical_idx_test1]
 df_test_temp2 = df_test[numerical_idx_test1]
 df_test = pd.concat([df_test_temp1,df_test_temp2], axis=1)

 for feature in skew_feature:
    df_test[feature] = boxcox1p(df_test[feature],0.1)
    
 df_test[numerical_idx_test1] = ss.transform(df_test[numerical_idx_test1])

 df_test_dummy = trans.transform(df_test)
 df_test = pd.DataFrame(df_test_dummy, columns=new_idx)

 df_test = df_test.fillna(0)
 
 return df_test

def Categorical_feature_engineering(data):
 data['Exter Qual'] = data['Exter Qual'].map({'Po': 1,'Fa':2,'TA':3,'Gd':4,'Ex':5})
 data['Exter Cond'] = data['Exter Cond'].map({'Po': 1,'Fa':2,'TA':3,'Gd':4,'Ex':5})
 data['Bsmt Qual'] = data['Bsmt Qual'].map({'Po': 1,'Fa':2,'TA':3,'Gd':4,'Ex':5})
 data['Bsmt Cond'] = data['Bsmt Cond'].map({'Po': 1,'Fa':2,'TA':3,'Gd':4,'Ex':5})
 data['Bsmt Exposure'] = data['Bsmt Exposure'].map({'No': 1,'Mn':2,'Av':3,'Gd':4})
 data['BsmtFin Type 1'] = data['BsmtFin Type 1'].map({'Unf': 1,'LwQ':2,'Rec':3,'BLQ':4,'ALQ':5,'GLQ':6})
 data['BsmtFin Type 2'] = data['BsmtFin Type 2'].map({'Unf': 1,'LwQ':2,'Rec':3,'BLQ':4,'ALQ':5,'GLQ':6})
 data['Heating QC'] = data['Heating QC'].map({'Po': 1,'Fa':2,'TA':3,'Gd':4,'Ex':5})
 data['Kitchen Qual'] = data['Kitchen Qual'].map({'Po': 1,'Fa':2,'TA':3,'Gd':4,'Ex':5})
 return data