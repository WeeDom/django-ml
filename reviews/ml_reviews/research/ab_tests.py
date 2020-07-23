import json
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import requests

# load dataset
df = pd.read_csv('https://raw.githubusercontent.com/pplonski/datasets-for-start/master/adult/data.csv', skipinitialspace=True)  # noqa 501
x_cols = [c for c in df.columns if c != 'income']
# set input matrix and target column
X = df[x_cols]
y = df['income']
# show first rows of data
df.head()

X_train, X_test, y_train, y_test = train_test_split(
                                    X, y,
                                    test_size=0.3,
                                    random_state=1234)

for i in range(1, 100):
    input_data = dict(X_test.iloc[i])
    target = y_test.iloc[i]
    req = requests.post(
        "http://127.0.0.1:8000/api/v1/income_classifier/predict?status=ab_testing",  # noqa 501
        input_data)
    response = req.json()
    # provide feedback
    requests.put("http://127.0.0.1:8000/api/v1/mlrequests/{}".format(response["request_id"]), {"feedback": target})  # noqa 501
