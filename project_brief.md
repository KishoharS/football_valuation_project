# Football Player Valuation

## Objectives
  This project will mainly focuses on how player's certain factors like Age, Position, Country and so on will affect the player's market value and it'll also predict the player's market value in the future. I chose this project because obviously i'm interested in this football and that kind of stuff and also i feel like it'll describe who i am and also showcasing my skills to potential employer. Looking forward to finish this wonderful project and i think it'll be a great experience.

## Success Metric
  R2 (R square), RMSE (Root Mean Squared Error) for valuation prediction metrics.

## Dataset
  Kaggle Dataset link: https://www.kaggle.com/datasets/davidcariboo/player-scores/code

## Process Overview
  Project's structure of process is as follows:
  1) Data cleaning
  2) EDA and Feature enginnering
  3) Feature selection
  4) Model building
  5) Evaluation and insights

### 1) Data cleaning:
 -  Cleaned over 1000000 fields of combined data from the required CSV files ('players.csv', 'appearances.csv', 'player_valuations.csv') for this specific project.
 -  Handled various fields of missing values, removed duplicate data, adding some features into our dataset.
 -  Standardize the data types.
 -  Removed fields which are not necessary for this project (like past players who are retired, above age 40, and some more criteria)
 -  Standardize the competition id for the model to predict.

### 2) EDA and Feature engineering:
 -  Explored correlations,distributions, and created meaningful features.

### 3) Feature selection:
 -  Identified the most relevant predictors impacting market value.
 -  Retained the most influential features that impact the market value analysis.

### 4) Model building
 -  Split the dataset into training and testing sets to evaluate.
 -  Tuned hyperparameters and cross-validated models to achieve the best performance balance.

### 5) Evaluation and insights
 -  Evaluated models using R², MAE, and RMSE metrics.
 -  Interpreted results to understand which features most strongly influence player valuation.

 ## Tools and Libraries
  1) Python
  2) Pandas
  3) Numpy
  4) Seaborn
  5) Matplotlib
  6) Scikit-learn

## Results Summary
 Best model: Random Forest Regressor
 Matrics:
  R² Score: 0.6230
  MAE: 0.7453
  RMSE: 0.9750

## Future work!!
 - Going to experiment with XGBoost or CatBoost to improve predictive power.
 - Inxorporate more recent player data for higher accuracy.
 - Deploy the model using Streamlit or Flast for interactive use
 - Will dive deeper into other aspects of this dataset like clubs, transfers, game_events. and so on!!

## My learning!!
- This project practically enables my understanding about how machiene learning actually works and what is real data science world look like. I learnt about how to train a model by without giving any target variables  *(i actually gave my model the target variables and wondered how our model is error free!!! Then i realised i shouldn't give the target variables to the model during training)*
- This project also improves my exploration skills by enabling me to go beyond a certain limit and not just doing basic EDA with simple CSV file!!
- Looking forward to go beyond in this data world!!