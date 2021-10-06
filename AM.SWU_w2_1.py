# KNN 분류 모델 import
from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier()

# 필요한 데이터셋 불러오기
from sklearn.datasets import load_iris
iris = load_iris()

# 데이터 프레임 만들기
import pandas as pd
df = pd.DataFrame(iris['data'], columns = iris['feature_names'])

# 데이터셋 분할하기
from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(iris['data'], iris['target'], random_state = 30)

# train dataset 학습하기
kn.fit(train_input, train_target)

# 모델 성능평가하기
print(kn.score(test_input, test_target))
