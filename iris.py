# Download the Iris data set from the UCI Machine Learning Repository. The url is 
# https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data


import requests
import zipfile
import os
from ucimlrepo import fetch_ucirepo 
  
def load_data():
    # fetch dataset 
    iris = fetch_ucirepo(id=53) 
    
    # data (as pandas dataframes) 
    X = iris.data.features 
    y = iris.data.targets 
    
    # metadata 
    print(iris.metadata) 

    # Look at the data
    X.describe()
    X.info()

    # Append y to X
    X['species'] = y

    # Check species names
    X['species'].value_counts()

    # Save the data
    X.to_csv('iris.csv', index=False)

    return X

def descriptive_statistics_by_species(data, species):
    """
    function that outputs the descriptive stats for each numeric feature while the categorical 
    variable is held fixed.
    """
    print('Descriptive statistics for', species)
    return data[data['species'] == species].describe()

if __name__ == '__main__':
    
    X = load_data()
    for species in X['species'].unique():
        temp = descriptive_statistics_by_species(X, species)
        print(temp)
        print('\n')