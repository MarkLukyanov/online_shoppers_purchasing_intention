import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.neighbors import KNeighborsClassifier
from explainerdashboard import *


df = pd.read_csv("https://raw.githubusercontent.com/MarkLukyanov/online_shoppers_purchsing_intention/main/customers_clean.csv")
X_full = df.drop('Revenue', axis=1)
y = (df.Revenue == True).astype(int)
X_train_full, X_test_full, y_train_full, y_test_full = train_test_split(X_full, y, test_size=0.25, random_state=42)


categorical = ['Month', 'VisitorType', 'Weekend']
numeric_features = ['Administrative', 'Administrative_Duration', 'Informational',
                    "Informational_Duration", "ProductRelated", "ProductRelated_Duration",
                    'BounceRates', 'ExitRates', 'PageValues', 'SpecialDay', 'OperatingSystems',
                    'Browser', 'Region', 'TrafficType']

ct = ColumnTransformer([
    ('ohe', OneHotEncoder(handle_unknown="ignore"), categorical),
    ('scaling', MinMaxScaler(), numeric_features)
])

X_train_transformed = ct.fit_transform(X_train_full)
X_test_transformed = ct.transform(X_test_full)


new_features = list(ct.named_transformers_['ohe'].get_feature_names_out())
new_features.extend(numeric_features)

X_train_transformed = pd.DataFrame(X_train_transformed, columns=new_features)
X_test_transformed = pd.DataFrame(X_test_transformed, columns=new_features)


model = KNeighborsClassifier(n_neighbors=27, p=1, weights='distance').fit(X_train_transformed, y_train_full)


explainer = ClassifierExplainer(model, X_test_transformed.iloc[:20], y_test_full.iloc[:20])
db = ExplainerDashboard(explainer)
db.to_yaml("dashboard.yaml", explainerfile="explainer.dill", dump_explainer=True)
