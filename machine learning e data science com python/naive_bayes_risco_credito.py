# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 14:31:07 2019

@author: WMW
"""

import pandas as pd

base = pd.read_csv('risco-credito.csv')
previsores = base.iloc[:, 0:4].values
classe = base.iloc[:, 4].values

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
previsores[:,0] = labelencoder.fit_transform(previsores[:,0])
previsores[:,1] = labelencoder.fit_transform(previsores[:,1])
previsores[:,2] = labelencoder.fit_transform(previsores[:,2])
previsores[:,3] = labelencoder.fit_transform(previsores[:,3])

from sklearn.naive_bayes import GaussianNB
classificador = GaussianNB()
classificador.fit(previsores, classe)

# história boa, dívida, alta, garantias nenhuma renda > 35
resultado = classificador.predict([[0,0,1,2], [3,0,0,0]])

print(classificador.classes_)
print(classificador.class_count_)
print(classificador.class_prior_)