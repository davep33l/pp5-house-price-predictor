import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import ppscore as pps
from src.data_management import load_house_data

def project_sale_price_study_body():

    # load data
    df = load_house_data()

    # hard copied from the 3_House_Price_Study.ipynb notebook
    vars_to_study = ['OverallQual', 'KitchenQual', 'GrLivArea', 'GarageArea', 'YearBuilt', 'TotalBsmtSF']

    # Title
    st.write("### Sale Price Study")

    # Text based on 3_House_Price_Study.ipynb notebook notebook - "Introduction" section
    st.info(
        f"The client is interested in discovering how the house attributes correlate with the "
        f"sale price. Therefore, the client expects data visualisations of the correlated "
        f"variables against the sale price to show that.")
    
    # Data Inspection
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

    # Text based on 3_House_Price_Study.ipynb notebook notebook - "Correlation Study" section
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

    # Dataframe for EDA
    df_eda = df.filter(vars_to_study + ['SalePrice'])

    # Individual plots per variable
    if st.checkbox("Variable Distribution by Sale Price"):
        sale_price_distribution_per_variable(df_eda)

    # Correlation and PPS Analysis heatmaps
    if st.checkbox("Correlation and Power Predictive Score (PPS) Analysis"):
        df_corr_pearson, df_corr_spearman, pps_matrix = CalculateCorrAndPPS(df)
        DisplayCorrAndPPS(df_corr_pearson = df_corr_pearson,
                    df_corr_spearman = df_corr_spearman, 
                    pps_matrix = pps_matrix,
                    CorrThreshold = 0.4, PPS_Threshold =0.2,
                    figsize=(12,10), font_annot=10)


# Distribution Plots Functions #
def sale_price_distribution_per_variable(df_eda):
    target_var = 'SalePrice'

    for col in df_eda.drop([target_var], axis=1).columns.to_list():
            plot_numerical(df_eda, col, target_var)

def plot_numerical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(8, 5))
    sns.regplot(data=df, x=col, y=target_var, scatter_kws={'s':5}, line_kws={"color":"green"})
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)


# Correllation and PPS Functions #
def heatmap_corr(df, threshold, figsize=(20, 12), font_annot=8):
    if len(df.columns) > 1:
        mask = np.zeros_like(df, dtype=np.bool)
        mask[np.triu_indices_from(mask)] = True
        mask[abs(df) < threshold] = True

        fig, axes = plt.subplots(figsize=figsize)
        sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                    mask=mask, cmap='viridis', annot_kws={"size": font_annot}, ax=axes,
                    linewidth=0.5
                    )
        axes.set_yticklabels(df.columns, rotation=0)
        plt.ylim(len(df.columns), 0)
        st.pyplot(fig)  # st.pyplot() renders image, in notebook is plt.show()


def heatmap_pps(df, threshold, figsize=(20, 12), font_annot=8):
    if len(df.columns) > 1:
        mask = np.zeros_like(df, dtype=np.bool)
        mask[abs(df) < threshold] = True
        fig, ax = plt.subplots(figsize=figsize)
        ax = sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                         mask=mask, cmap='rocket_r', annot_kws={"size": font_annot},
                         linewidth=0.05, linecolor='grey')
        plt.ylim(len(df.columns), 0)
        st.pyplot(fig)


def CalculateCorrAndPPS(df):
    df_corr_spearman = df.corr(method="spearman")
    df_corr_pearson = df.corr(method="pearson")

    pps_matrix_raw = pps.matrix(df)
    pps_matrix = pps_matrix_raw.filter(['x', 'y', 'ppscore']).pivot(columns='x', index='y', values='ppscore')

    pps_score_stats = pps_matrix_raw.query("ppscore < 1").filter(['ppscore']).describe().T
    st.write("Power Predictive Score (PPS) Stats")
    st.dataframe(pps_score_stats.round(3))

    return df_corr_pearson, df_corr_spearman, pps_matrix


def DisplayCorrAndPPS(df_corr_pearson, df_corr_spearman, pps_matrix, CorrThreshold, PPS_Threshold,
                      figsize=(20, 12), font_annot=8):

    st.info(
        f"\n"
        f"The below shows how the SalePrice is correlated with other variables (features and target). "
        f"Also showing multi-colinearity between features.\n\n"
        )

    st.write(
        f"\n\n"
        f"*** Heatmap: Spearman Correlation ***\n\n"
        f"It evaluates monotonic relationship\n"
        )
    heatmap_corr(df=df_corr_spearman, threshold=CorrThreshold, figsize=figsize, font_annot=font_annot)

    st.write(
        f"\n\n"
        f"*** Heatmap: Pearson Correlation ***\n\n"
        f"It evaluates the linear relationship between two continuous variables\n"
        )
    heatmap_corr(df=df_corr_pearson, threshold=CorrThreshold, figsize=figsize, font_annot=font_annot)

    st.write(
        f"\n\n"
        f"*** Heatmap: Power Predictive Score (PPS) ***\n\n"
        f"PPS detects linear or non-linear relationships between two columns.\n"
        f"The score ranges from 0 (no predictive power) to 1 (perfect predictive power) \n"
        )
    heatmap_pps(df=pps_matrix, threshold=PPS_Threshold, figsize=figsize, font_annot=font_annot)