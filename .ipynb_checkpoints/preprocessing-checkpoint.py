{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2e50cd2a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def Categorical_feature_engineering(data):\n",
    " data['Exter Qual'] = data['Exter Qual'].map({'Po': 1,'Fa':2,'TA':3,'Gd':4,'Ex':5})\n",
    " data['Exter Cond'] = data['Exter Cond'].map({'Po': 1,'Fa':2,'TA':3,'Gd':4,'Ex':5})\n",
    " data['Bsmt Qual'] = data['Bsmt Qual'].map({'Po': 1,'Fa':2,'TA':3,'Gd':4,'Ex':5})\n",
    " data['Bsmt Cond'] = data['Bsmt Cond'].map({'Po': 1,'Fa':2,'TA':3,'Gd':4,'Ex':5})\n",
    " data['Bsmt Exposure'] = data['Bsmt Exposure'].map({'No': 1,'Mn':2,'Av':3,'Gd':4})\n",
    " data['BsmtFin Type 1'] = data['BsmtFin Type 1'].map({'Unf': 1,'LwQ':2,'Rec':3,'BLQ':4,'ALQ':5,'GLQ':6})\n",
    " data['BsmtFin Type 2'] = data['BsmtFin Type 2'].map({'Unf': 1,'LwQ':2,'Rec':3,'BLQ':4,'ALQ':5,'GLQ':6})\n",
    " data['Heating QC'] = data['Heating QC'].map({'Po': 1,'Fa':2,'TA':3,'Gd':4,'Ex':5})\n",
    " data['Kitchen Qual'] = data['Kitchen Qual'].map({'Po': 1,'Fa':2,'TA':3,'Gd':4,'Ex':5})\n",
    " return data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f39f1eb4",
   "metadata": {},
   "outputs": [],
   "source": [
    "def preprocessing(df_test):\n",
    " \n",
    " columns_dropped = ['Pool QC','Misc Feature','Alley','Fence','Fireplace Qu','Lot Frontage','Garage Finish','Garage Qual','Garage Yr Blt','Garage Cond','Garage Type','Pool Area','Fireplaces','Garage Area','Garage Cars','Mas Vnr Area','Mas Vnr Type','Misc Val','3Ssn Porch','Low Qual Fin SF','Screen Porch','BsmtFin SF 2','Enclosed Porch']\n",
    " coll_columns_drop = ['BsmtFin SF 1','Bsmt Unf SF','1st Flr SF','2nd Flr SF','Year Remod/Add','TotRms AbvGrd','Exter Qual','Exter Cond','Bsmt Qual','Bsmt Cond']\n",
    " feature = ['Lot Area','Open Porch SF', 'Wood Deck SF','Gr Liv Area'] \n",
    "    \n",
    " df_test[['MS SubClass','Yr Sold','Mo Sold','Land Slope']] = df_test[['MS SubClass','Yr Sold','Mo Sold','Land Slope']] .astype(str)\n",
    "\n",
    " df_test = Categorical_feature_engineering(df_test)\n",
    " numerical_idx_test = df_test.select_dtypes(include = ['int64', 'float64']).columns\n",
    " categorical_idx_test = df_test.select_dtypes(include = ['object']).columns\n",
    "\n",
    " df_test.drop(columns=columns_dropped,inplace=True)\n",
    " df_test=df_test.fillna(0)\n",
    " df_test = df_test.drop(columns=coll_columns_drop)\n",
    "\n",
    " numerical_idx_test1 = df_test.select_dtypes(include = ['int64', 'float64']).columns\n",
    " categorical_idx_test1 = df_test.select_dtypes(include = ['object']).columns\n",
    " df_test_temp1 = df_test[categorical_idx_test1]\n",
    " df_test_temp2 = df_test[numerical_idx_test1]\n",
    " df_test = pd.concat([df_test_temp1,df_test_temp2], axis=1)\n",
    "\n",
    " for feature in skew_feature:\n",
    "    df_test[feature] = boxcox1p(df_test[feature],0.1)\n",
    "    \n",
    " df_test[numerical_idx_test1] = ss.transform(df_test[numerical_idx_test1])\n",
    "\n",
    " df_test_dummy = trans.transform(df_test)\n",
    " df_test = pd.DataFrame(df_test_dummy, columns=new_idx)\n",
    "\n",
    " df_test = df_test.fillna(0)\n",
    " \n",
    " return df_test"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
