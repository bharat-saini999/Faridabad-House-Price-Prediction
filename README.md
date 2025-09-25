# Faridabad-House-Price-Prediction

This project focuses on predicting house prices in Faridabad, India using a Linear Regression model. The dataset used was originally intended for Bengaluru housing prices, but has been adapted for Faridabad. The aim is to clean and prepare real estate data and build a machine learning model that estimates property prices based on features like size, location, number of bedrooms, and bathrooms.

✅ Tech Stack:

Python, Pandas, NumPy

Matplotlib, Seaborn

Scikit-learn

Linear Regression

JSON & Pickle for model export


----------------------KEY STEPS:-----------------------------------------------------------------------------------------
1.  Data Cleaning & Preprocessing:
Removed irrelevant features like society and balcony, handled missing values, and fixed inconsistent data formats (e.g., converting "2100-2850" sqft ranges to their average).

2.  Feature Engineering:
Added new features such as BHK and price_per_sqft. Also applied one-hot encoding to location data and performed dimensionality reduction for rare locations.

3.  Outlier Detection & Removal:
Implemented logic-based and statistical outlier detection:

Removed entries where total sqft per BHK was unrealistically low (<300 sqft).

Removed extreme values based on price per sqft using standard deviation filtering.

Dropped data where higher BHKs had lower prices than lower BHKs in the same area.

4.  Model Building:
Used Linear Regression to build the prediction model. Achieved an R² score of ~0.87 on the training set and ~0.84 on the test set, indicating good model performance.

5.  Visualization:
Plotted scatter charts comparing 2BHK and 3BHK prices for various locations, as well as histograms of price per sqft and bathroom counts to support outlier analysis.

6.  Model Deployment Ready:
Exported the trained model as a .pickle file and the feature columns in a columns.json file for easy use in a deployment pipeline or web app.
