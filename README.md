# Online shoppers purchasing intention
The aim of the project is to build a machine learning model that will train on given features to predict, whether a customer of the website will end with shopping or not, and to make a dashboard that will depict all the statistics and dependencies. All the additional information on the dataset can be found [here](https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset).

## Files
- `app`
  - `app.py`: script for running the dashboard
- `Dockerfile`: script of instructions to build a Docker container image
- `Project.ipynb`: exploratory data analysis
- `Project_ML.ipynb`: selection and building the model and dashboard
- `customers_clean.csv`: 'clean' data 
- `dashboard.py`: script for creating the dashboard
- `dashboard.yaml`: serialization container for running the dashboard
- `explainer.dill`: serialized dashboard

## Technologies
The exploratory data analysis was made with `pandas` and `numpy` for computations and transformations; `matplotlib` and `seaborn` for vizualization; `association_metrics` and `scipy.stats` for s[ecific correlations. The machine learning model was built with `KNNClassifier` from `scikit-learn`, its parameters were chosen using `GridSearchCV`. The dashboard was built from `ExplainerDashboard`.

The dashboard was packed into a `Docker` container.

## Dashboard
To run the dashboard on your PC, you should:
1. Open a terminal and paste the following command in the command line `docker run -p 9050:9050 marklukyanov/explainerdashboard:latest` to download the image(if it is still not on your computer) and run the container locally.
2. Open a web-browser you are currently using(preferably - Google Chrome) and paste the following address in the address line: `http://0.0.0.0:9050/`.

## Author and license
Code released under the MIT license.

Copyright (c) 2023 MarkLukyanov
