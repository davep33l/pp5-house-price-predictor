from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


def regression_performance(X_train, y_train, X_test, y_test, pipeline):
    st.write("*** Model Evaluation ***")
    st.write(f"* Train Set\n")
    regression_evaluation(X_train, y_train, pipeline)
    st.write(f"* Test Set\n")
    regression_evaluation(X_test, y_test, pipeline)


def regression_evaluation(X, y, pipeline):
    prediction = pipeline.predict(X)
    st.write(f"R2 Score: {r2_score(y, prediction).round(3)}")
    st.write(f"Mean Absolute Error: {mean_absolute_error(y, prediction):,.3f}")
    st.write(f"Mean Squared Error: {mean_squared_error(y, prediction):,.3f}")
    st.write(f"Root Mean Squared Error: {np.sqrt(mean_squared_error(y, prediction)):,.3f}")
    st.write("\n")


def regression_evaluation_plots(X_train, y_train, X_test, y_test, pipeline, alpha_scatter=0.5):
    pred_train = pipeline.predict(X_train)
    pred_test = pipeline.predict(X_test)

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
    sns.scatterplot(x=y_train.squeeze(), y=pred_train.squeeze(), alpha=alpha_scatter, ax=axes[0])
    sns.lineplot(x=y_train.squeeze(), y=y_train.squeeze(), color='purple', ax=axes[0])
    axes[0].set_xlabel("Actual")
    axes[0].set_ylabel("Predictions")
    axes[0].set_title("Train Set")

    sns.scatterplot(x=y_test.squeeze(), y=pred_test.squeeze(), alpha=alpha_scatter, ax=axes[1])
    sns.lineplot(x=y_test.squeeze(), y=y_test.squeeze(), color='purple', ax=axes[1])
    axes[1].set_xlabel("Actual")
    axes[1].set_ylabel("Predictions")
    axes[1].set_title("Test Set")

    st.pyplot(fig)