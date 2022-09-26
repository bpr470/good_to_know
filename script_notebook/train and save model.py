# %%
# Train a model and store it including the preprocessing as pkl file
import numpy as np
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline

def load_data():

    df = pd.DataFrame(columns=["feature-1", "feature-2", "feature-3", "target"])

    df["feature-1"] = np.random.randint(10, size=1000)
    df["feature-2"] = np.random.randint(5, size=1000)
    df["feature-3"] = np.random.randint(200, size=1000)
    df["target"] = np.random.randint(2, size=1000)
    return df

def transform_train(df):
    cat_vars = ['feature-2']
    num_vars = ['feature-1', 'feature-3']

    data_pipeline = ColumnTransformer([
        ('numerical', StandardScaler(), num_vars),
        ('categorical', OneHotEncoder(), cat_vars)
    ])

    pipe = Pipeline(
        steps=[("preprocessor", data_pipeline), ("Model", LogisticRegression())])

    X, y = df[["feature-1", "feature-2", "feature-3"]], df["target"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


    clf = pipe.fit(X_train, y_train)
    print(clf.score(X_test, y_test))
    pickle.dump(clf, open("model_object.pkl",'wb'))
    return print('model trained')


# %%
# Interact with the model when deployed in seperate container

import pickle
import numpy as np
import pandas as pd

class Endpoint(object):

    def __init__(self):
        with open("model_object.pkl","rb") as f:
            self.clf = pickle.load(f)
        
    def predict(self, x, feature_names):
        x = pd.DataFrame(x, columns=feature_names)       
        response = self.clf.predict(x).tolist()
        response = np.asarray(response)

        return response