import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier


data_frame = pd.read_csv("diabetes.csv")


labels = {
    'Pregnancies'
    'Glucose'
    'BloodPressure'
    'SkinThickness'
    'Insulin'
    'BMI'
    'DiabetesPedigreeFunction'
    'Age'
    'Outcome'
}

data_frame.replace('0', 10, inplace=True)
data_frame.index = ['Stap', 'Milosh', 'Oli', 'Aco', 'Crepcho']

print(data_frame)
# print(data_frame['Milosh'])
prva_vrednost_za_glukoza = data_frame['Glucose'][0]

for index, column in data_frame.iterrows():
    print(column['Stap'], column['Milosh'])




label_encoders = {}
data_frame_encoded = pd.DataFrame()
for column in data_frame:
    if column in labels:
        label_encoders[column] = preprocessing.LabelEncoder()
        label_encoders[column].fit(labels[column])
        data_frame_encoded[column] = label_encoders[column].transform(data_frame[column])
    else:
        data_frame_encoded[column] = data_frame[column]


features = np.array(data_frame_encoded.drop(['Outcome'], 1))
label = np.array(data_frame_encoded['Outcome'])

features_train, features_test, label_train, label_test = model_selection.train_test_split(features, label, test_size=0.10)

decision_tree = DecisionTreeClassifier()
decision_tree.fit(features_train, label_train)

print('Score: ', decision_tree.score(features_test, label_test))
# print(classification_report(label_test, decision_tree.predict(features_test)))


# distribution = list(range(1,8))
# minus_distribution = [-x for x in distribution]
# log_distribution = [x for x in map(np.log2, distribution)]
# entropy_value = np.dot(minus_distribution, log_distribution)
# print(entropy_value)
# def entropy(distribution):
#     minus_distribution = [-x for x in distribution]
#     log_distribution = [x for x in map(np.log2, distribution)]
#     return np.dot(minus_distribution, log_distribution)
