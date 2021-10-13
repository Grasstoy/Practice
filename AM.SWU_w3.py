import pandas as pd

train_file = pd.read_csv(r'C:\Users\titanic\train.csv')
train_file.head()

train_file.isnull()
train_file.isnull().sum()

train_target = train_file['Survived']

train_file.drop(labels=['Name'], axis=1, inplace=True)
train_file.drop(labels=['Ticket'], axis=1, inplace=True)
train_file.drop(labels=['Pclass'], axis=1, inplace=True)
train_file.drop(labels=['SibSp'], axis=1, inplace=True)
train_file.drop(labels=['Parch'], axis=1, inplace=True)
train_file.drop(labels=['Fare'], axis=1, inplace=True)
train_file.drop(labels=['Cabin'], axis=1, inplace=True)
train_file.drop(labels=['Embarked'], axis=1, inplace=True)
train_file.drop(labels=['PassengerId'], axis=1, inplace=True)
train_file.head()

train_file['Sex']=train_file['Sex'].map({'male':0, 'female':1})
train_file.head()

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
feature_names = ['Sex', 'Age']
lr.fit(train_file[feature_names], train_target)

import pandas as pd
test_file = pd.read_csv(r'C:\Users\titanic\test.csv')
test_file.head()

test_file.drop(labels=['Name'], axis=1, inplace=True)
test_file.drop(labels=['Ticket'], axis=1, inplace=True)
test_file.drop(labels=['Pclass'], axis=1, inplace=True)
test_file.drop(labels=['SibSp'], axis=1, inplace=True)
test_file.drop(labels=['Parch'], axis=1, inplace=True)
test_file.drop(labels=['Fare'], axis=1, inplace=True)
test_file.drop(labels=['Cabin'], axis=1, inplace=True)
test_file.drop(labels=['Embarked'], axis=1, inplace=True)
test_file.drop(labels=['PassengerId'], axis=1, inplace=True)
test_file.head()

test_file['Sex']=test_file['Sex'].map({'male':0, 'female':1})
test_file.head()

lr.predict(test_file)
