# 보스턴 주택 데이터 불러오기
from sklearn.datasets import load_boston
boston = load_boston()
print(boston)

# 데이터프레임 만들기
import pandas as pd
df = pd.DataFrame(boston['data'], columns = boston['feature_names'])
df

# 결측값 확인하기
df.isnull()
df.isnull().sum()

# 상관관계 분석
df_corr = df.corr()

# 데이터셋 분할하기
from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(boston['data'], boston['target'], random_state=12)

# 데이터 전처리하기
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()

ss.fit(train_input)
train_scaled = ss.transform(train_input)
ss.fit(test_input)
test_scaled = ss.transform(test_input)

# 선형 회귀 분석 모델 import하기
from sklearn.linear_model import LinearRegression
lr = LinearRegression()

# 선형회귀모델에 train_scaled 훈련하기
lr.fit(train_scaled, train_target)

print(lr.score(test_scaled, test_target))
