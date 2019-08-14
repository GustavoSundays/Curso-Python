# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 10:41:46 2019

@author: WMW
"""
import pandas as pd

base = pd.read_csv('credit-data.csv')

base.describe()

base.loc[base['age'] < 0]

# MANEIRAS DE ARRUMAR IDADE NEGATIVA

# apagar a coluna
base.drop('age', 1, inplace=True)

# apagar só os regristros com problema
base.drop(base[base.age < 0].index, inplace=True)

# preencher os valores manualmente
# preencer os valores com a média
base.mean()
base['age'].mean()
base['age'][base.age > 0].mean()
base.loc[base.age < 0, 'age'] = 40.92

pd.isnull(base['age'])
base.loc[pd.isnull(base['age'])]

previsores = base.iloc[:, 1:4].values
classe = base.iloc[:, 4].values

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy='mean', axis=0)
imputer = imputer.fit(previsores[:, 0:3])
previsores[:, 0:3] = imputer.transform(previsores[:,0:3])

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)