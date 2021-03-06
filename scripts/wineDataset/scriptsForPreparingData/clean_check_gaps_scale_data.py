import pandas as pd
from sklearn.preprocessing import MinMaxScaler

name_file_to_read = '../../../preparedData/wineDataset/wines.csv'
data = pd.read_csv(name_file_to_read, sep=';', names=['fixed_acidit', 'volatile_acidity', 'citric_acid',
                                                      'residual_sugar', 'chlorides', 'free_sulfur_dioxide',
                                                      'total_sulfur_dioxide', 'density', 'pH', 'sulphates',
                                                      'alcohol', 'quality'])

data.drop(index=0, inplace=True)

for idx, row in data.iterrows():
    for item in row:
        if item == 'nan':
            print(idx, item)
        # if float(item) == 0:
        #     print(idx, item)    # some series has value 0 as value of for e.g. citric_acid

print(data.groupby(['quality']).count())

for idx, row in data.iterrows():
    if int(row['quality']) == 9:
        data.loc[idx, 'quality'] = str(8)
    if int(row['quality']) == 3:
        data.loc[idx, 'quality'] = str(4)

print(data.groupby(['quality']).count())

scaler = MinMaxScaler(feature_range=(0, 1))
X = scaler.fit_transform(data)
print(X)
print(type(X))

df = pd.DataFrame({'fixed_acidit': X[:, 0], 'volatile_acidity': X[:, 1], 'citric_acid': X[:, 2],
                   'residual_sugar': X[:, 3], 'chlorides': X[:, 4], 'free_sulfur_dioxide': X[:, 5],
                   'total_sulfur_dioxide': X[:, 6], 'density': X[:, 7], 'pH': X[:, 8], 'sulphates': X[:, 9],
                   'alcohol': X[:, 10], 'quality': data.iloc[:, 11]})

print(df)
df.to_csv('../../../preparedData/wineDataset/wines_scaled.csv')
