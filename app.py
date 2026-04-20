import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.title("ドライバー状態推定アプリ")

# データ
np.random.seed(0)
data = pd.DataFrame({
    "eye_movement": np.random.rand(100),
    "steering_variance": np.random.rand(100),
    "speed_variance": np.random.rand(100)
})

data["fatigue"] = (data["eye_movement"] + data["steering_variance"] > 1).astype(int)

X = data.drop("fatigue", axis=1)
y = data["fatigue"]

# モデル
model = RandomForestClassifier()
model.fit(X, y)

# UI
st.write("データ例", data.head())

eye = st.slider("視線の動き", 0.0, 1.0, 0.5)
steering = st.slider("操作のばらつき", 0.0, 1.0, 0.5)
speed = st.slider("速度変動", 0.0, 1.0, 0.5)

input_data = pd.DataFrame({
    "eye_movement":[eye],
    "steering_variance":[steering],
    "speed_variance":[speed]
})

prediction = model.predict(input_data)

st.write("疲労状態（1=疲労）:", prediction[0])
