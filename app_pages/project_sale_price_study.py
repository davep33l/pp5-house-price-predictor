import streamlit as st
from src.data_management import load_house_data

def project_sale_price_study_body():

    # load data
    df = load_house_data()

    # hard copied from the 3_House_Price_Study.ipynb notebook
    vars_to_study = ['OverallQual', 'KitchenQual', 'GrLivArea', 'GarageArea', 'YearBuilt', 'TotalBsmtSF']

    st.write("### Sale Price Study")

    st.info(
        f"The client is interested in discovering how the house attributes correlate with the "
        f"sale price. Therefore, the client expects data visualisations of the correlated "
        f"variables against the sale price to show that.")
    
    # inspect the data
    if st.checkbox("Inspect House Price Data"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 10 rows.")

        st.write(df.head(10))

    st.write("---")