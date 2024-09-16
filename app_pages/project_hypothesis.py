import streamlit as st


def project_hypothesis_body():

    st.write("### Project Hypothesis and Validation")

    # Conclusions taken from "3_House_Price_Study" notebook


    st.info(
        f"**Hypothesis 1**\n\n"
        f"* We suspect that better quality decoration will positively influence the sale price (as higher quality materials are likely to have been used, and cost more)\n\n "
    )

    st.success(
        f"**Correct**\n\n "
        f"* The correlation study performed in the House Price Study supports this. \n\n"
    )

    st.info(
        f"**Hypothesis 2**\n\n"
        f"* We suspect that larger rooms/floors will positively influence the sale price (as it implies more land/space)\n\n "
    )

    st.success(
        f"**Correct**\n\n "
        f"* The correlation study performed in the House Price Study supports this. \n\n"
    )

    st.info(
        f"**Hypothesis 3**\n\n"
        f"* We suspect that new builds will positively influence the sale price (due to higher cost of materials / inflation)\n\n "
    )

    st.success(
        f"**Correct**\n\n "
        f"* The correlation study performed in the House Price Study supports this. \n\n"
    )

