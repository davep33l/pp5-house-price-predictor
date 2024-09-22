import streamlit as st
import pandas as pd
from src.data_management import load_pkl_file


def project_predict_sale_price_body():

    # load predict sale price files
    version = 'v1'
    sale_price_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_sale_price/{version}/clf_pipeline.pkl")
    sale_price_features = (pd.read_csv(f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv")
                       .columns
                       .to_list()
                       )

    st.write("### Predict Sale Price Interface")

    st.info(f"The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.")

    st.write("---")

    # Generate Live Data
    check_variables_for_UI(sale_price_features)



def check_variables_for_UI(sale_price_features):
    import itertools

    # The widgets inputs are the features used in all pipelines (sale price)
    # We combine them only with unique values
    combined_features = set(
        list(
            itertools.chain(sale_price_features)
        )
    )
    st.write(
        f"* There are {len(combined_features)} features for the UI: \n\n {combined_features}")
