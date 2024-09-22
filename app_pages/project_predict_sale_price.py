import streamlit as st
import pandas as pd
from src.data_management import load_pkl_file, load_house_data


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
    X_live = DrawInputsWidgets()


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


def DrawInputsWidgets():

    # load dataset
    df = load_house_data()

    # create the columns
    col1, col2, col3, col4 = st.beta_columns(4)

    # We are using these features to feed the ML pipeline - values copied from check_variables_for_UI() result
    # {'OverallQual', '2ndFlrSF', 'GarageArea', 'TotalBsmtSF'}

    # create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # from here on we draw the widget based on the variable type (numerical or categorical)
    # and set initial values
    # streamlit docs for customising the number_input widget:
    # https://docs.streamlit.io/develop/api-reference/widgets/st.number_input

    with col1:
        feature = "OverallQual"
        st_widget = st.selectbox(
            label=feature,
            options=sorted(df[feature].unique()),
            help="Overall Quality of the house (1 = Poor, 10 = Very Excellent)"
        )
    X_live[feature] = st_widget

    with col2:
        feature = "2ndFlrSF"
        st_widget = st.number_input(
            label=feature,
            min_value=0,
            step=10,
            help="Square feet of 2nd floor"
        )
    X_live[feature] = st_widget

    with col3:
        feature = "GarageArea"
        st_widget = st.number_input(
            label=feature,
            min_value=0,
            step=10,
            help="Size of garage in square feet"
        )
    X_live[feature] = st_widget

    with col4:
        feature = "TotalBsmtSF"
        st_widget = st.number_input(
            label=feature,
            min_value=0,
            step=10,
            help="Total square feet of basement area"
        )
    X_live[feature] = st_widget

    return X_live
