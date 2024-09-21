import streamlit as st
from src.data_management import load_house_data
import matplotlib.pyplot as plt
import seaborn as sns

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

    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to better understand how "
        f"the variables are correlated to SalePrice. \n"
        f"The most correlated variable are: **{vars_to_study}**"
    )

    # Text based on 3_House_Price_Study.ipynb notebook notebook - "Conclusions and Next steps" section
    st.info(
        f"The correlations and the charts both show that:\n\n "

        f"* A higher quality finish to a house positively increases the SalePrice \n"
        f"* A larger square feet of ground floor living space positively increases the SalePrice \n"
        f"* A higher quality kitchen positively increases the SalePrice \n"
        f"* A more recently built homes positively increases the SalePrice \n"
        f"* A larger square feet of basement space positively increases the SalePrice \n"
        f"* A larger square feet of garage space positively increases the SalePrice \n\n"

        f"Each of these are backed up with strong or moderate positive correlation levels and high or fairly high confidence levels on the regression plots"
    )

    # Code copied from "3_House_Price_Study.ipynb notebook notebook" notebook - "EDA on selected variables" section
    df_eda = df.filter(vars_to_study + ['SalePrice'])

    # Individual plots per variable
    if st.checkbox("Variable Distribution by Sale Price"):
        sale_price_distribution_per_variable(df_eda)


# function created using "3_House_Price_Study.ipynb notebook notebook" notebook code - "Variables Distribution by Churn" section
def sale_price_distribution_per_variable(df_eda):
    target_var = 'SalePrice'

    for col in df_eda.drop([target_var], axis=1).columns.to_list():
            plot_numerical(df_eda, col, target_var)


# code copied from "3_House_Price_Study.ipynb notebook notebook" notebook - "Variables Distribution by Churn" section
def plot_numerical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(8, 5))
    sns.regplot(data=df, x=col, y=target_var, scatter_kws={'s':5}, line_kws={"color":"green"})
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)  # st.pyplot() renders image, in notebook is plt.show()