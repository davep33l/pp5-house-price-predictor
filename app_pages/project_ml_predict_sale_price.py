import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.data_management import load_pkl_file
from src.machine_learning.evaluate_regression import regression_performance, regression_evaluation_plots

def project_ml_predict_sale_price_body():

    # load tenure pipeline files
    version = 'v1'
    sale_price_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_sale_price/{version}/clf_pipeline.pkl")
    sale_price_feat_importance = plt.imread(
        f"outputs/ml_pipeline/predict_sale_price/{version}/features_importance.png")
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/y_train.csv")
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/y_test.csv")

    st.write("### ML Pipeline: Predict Sale Price")

    # display pipeline training summary conclusions
    st.info(
        f"* We trained our data using a regression model. Specifically a GradientBoostingRegressor model."
        f" The model had an r2 score of 0.947 on the training data."
        f" The model had an r2 score of 0.807 on the testing data."
        f" The high r2 score on the training data suggests that the model is overfitting."
        f" However as both of these scores pass the criteria set out in the project plan of an r2 score of 0.75, we will proceed with this model."
    )
    st.write("---")

    # show pipeline steps
    st.write("### ML pipeline to predict sale price.")
    st.write(sale_price_pipe)
    st.write("---")

    # show best features
    st.write("### The features the model was trained on.")
    st.write(X_train.columns.to_list())
    st.write("### The importance of each feature in the model.")
    st.image(sale_price_feat_importance)
    st.write("---")

    # evaluate performance on both sets
    st.write("### Pipeline Performance")
    regression_performance(X_train, y_train, X_test, y_test, sale_price_pipe)
    st.write("---")
    regression_evaluation_plots(X_train, y_train, X_test, y_test, sale_price_pipe)