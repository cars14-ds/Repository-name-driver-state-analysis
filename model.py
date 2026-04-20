import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# データ作成
np.random.seed(0)
data = pd.DataFrame({
    "eye_movement": np.random.rand(200),
    "steering_variance": np.random.rand(200),
    "speed_variance": np.random.rand(200),
})

# 疲労ラベル
data["fatigue"] = (data["eye_movement"] + data["steering_variance"] > 1).astype(int)

# 学習
X = data.drop("fatigue", axis=1)
y = data["fatigue"]

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = RandomForestClassifier()
model.fit(X_train, y_train)

# 評価
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
