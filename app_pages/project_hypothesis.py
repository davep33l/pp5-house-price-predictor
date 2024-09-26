import streamlit as st


def project_hypothesis_body():

    st.write("### Project Hypothesis and Validation")

    # Conclusions taken from "3_House_Price_Study" notebook

    st.info(
        "**Hypothesis 1**\n\n"
        "* We suspect that better quality decoration will positively "
        "influence the sale price (as higher quality materials are "
        "likely to have been used, and cost more).\n\n "
    )

    st.success(
        "**Correct**\n\n "
        "* The correlation study performed in the House Price Study supports "
        "this. Along with the feature importance extraction within the "
        "Modelling and Evaluation stage. \n\n"
    )

    st.info(
        "**Hypothesis 2**\n\n"
        "* We suspect that larger rooms/floors will positively influence the "
        "sale price (as it implies more land/space).\n\n "
    )

    st.success(
        "**Correct**\n\n "
        "* The correlation study performed in the House Price Study supports "
        "this. Along with the feature importance extraction within the "
        "Modelling and Evaluation stage. \n\n"
    )

    st.info(
        "**Hypothesis 3**\n\n"
        "* We suspect that new builds will positively influence the sale "
        "price (due to higher cost of materials / inflation).\n\n "
    )

    st.warning(
        "**Partially Correct**\n\n "
        "* The correlation study performed in the House Price Study supported "
        "this. However the final model did not include the age of the "
        "property as being a defining feature in predicting house price \n\n"
    )
