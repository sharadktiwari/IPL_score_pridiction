# IPL_score_pridiction
I worked on a web app using Flask. Give Inputs as (batting_team, bowling_team, overs, runs, wickets, runs_in_prev_5_overs, wickets_in_prev_5_overs) and it will predict the approximate score the batting team may score within 20 overs. 

# Dataset:
IPL.csv.
* 1 - Time Series Columns, 2 - Categorical Columns and remaining Numerical Columns handled during EDA. Created 23 Feature Columns from 15 Features.

To Achieve Best Accuracy and To Reduce Overfitting Problem, I used Linear Ridge Regressor (With Hyperparameter tuning - GridSearchCV)

# ABOUT :
Took IPL Data & performed Data Wrangling. During EDA handling Categorical data is major task. Trained Linear Ridge Regressor model. After Prediction calculated Errors & Model Score. To Reduce Errors & to boost model score used GridSearchCV for Hyper Parameter Tuning. 
   
# Parameters Obtained After Hyperparameter Tuning - 
 {'alpha': 40}
 
# Score Obtained After Hyperparameter Tuning - 
-328.42
  
# Values After Hyperparameter Tuning
   MAE :-  12.12,
   MSE :-  251.03,
   RMSE :-  15.84

# Achieved    r2_score -   0.75


# Contributors:
> Sharad Kumar Tiwari



