import streamlit as st
import pandas as pd
from src.data_management import load_pkl_file


def project_predict_sale_price_body():

    # load predict tenure files
    version = 'v1'
    sale_price_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_sale_price/{version}/clf_pipeline.pkl")
    sale_price_features = (pd.read_csv(f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv")
                       .columns
                       .to_list()
                       )

    st.write("### Predict Sale Price")

    st.write(sale_price_pipe)
    st.write("---")
    st.write(sale_price_features)