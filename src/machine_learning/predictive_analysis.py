import streamlit as st


def predict_sale_price(X_live, sale_price_features, sale_price_pipeline):

    # from live data, subset features related to this pipeline
    X_live_sale_price = X_live.filter(sale_price_features)

    # predict
    sale_price_prediction = sale_price_pipeline.predict(X_live_sale_price)

    # Display the prediction
    statement = f"The predicted sale price is: ${sale_price_prediction[0]:,.2f}"
    st.write(statement)
