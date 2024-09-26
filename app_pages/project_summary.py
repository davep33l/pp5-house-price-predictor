import streamlit as st


def project_summary_body():

    st.write("### Project Summary")

    st.info(
        "**Project Purpose** \n\n"
        "A client has recently received an inheritance from a deceased great-grandfather, "
        "which contains properties located in Ames, Iowa. They have asked for assistance "
        "in maximising the sales price for the inherited properties. \n\n"
        "Although the client has an excellent understanding of property prices in their own "
        "local area, they fear that basing their estimates for property value on their current "
        "knowledge may lead to inaccurate appraisals. What makes a house desirable and valuable "
        "in their local area, might not be the same in Ames, Iowa. They have found a public "
        "dataset containing house prices from Ames, Iowa and have provided it as part of the analysis. \n\n"
    )

    st.info(
        "**Project Terms & Jargon**\n\n"
        "|Variable|Meaning|Units|\n"
        "|:-------|:-------|:-----|\n"
        "|1stFlrSF|First Floor square feet|334 - 4692|\n"
        "|2ndFlrSF|Second-floor square feet|0 - 2065|\n"
        "|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|\n"
        "|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|\n"
        "|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinished; None: No Basement|\n"
        "|BsmtFinSF1|Type 1 finished square feet|0 - 5644|\n"
        "|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|\n"
        "|TotalBsmtSF|Total square feet of basement area|0 - 6110|\n"
        "|GarageArea|Size of garage in square feet|0 - 1418|\n"
        "|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|\n"
        "|GarageYrBlt|Year garage was built|1900 - 2010|\n"
        "|GrLivArea|Above grade (ground) living area square feet|334 - 5642|\n"
        "|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|\n"
        "|LotArea|Lot size in square feet|1300 - 215245|\n"
        "|LotFrontage|Linear feet of street connected to property|21 - 313|\n"
        "|MasVnrArea|Masonry veneer area in square feet|0 - 1600|\n"
        "|EnclosedPorch|Enclosed porch area in square feet|0 - 286|\n"
        "|OpenPorchSF|Open porch area in square feet|0 - 547|\n"
        "|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|\n"
        "|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|\n"
        "|WoodDeckSF|Wood deck area in square feet|0 - 736|\n"
        "|YearBuilt|Original construction date|1872 - 2010|\n"
        "|YearRemodAdd|Remodel date (same as construction date if no remodeling or additions)|1950 - 2010|\n"
        "|SalePrice|Sale Price|34900 - 755000|\n"
    )

    st.success(
        "**Project Dataset** \n\n"
        "* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). \n "
        "* The dataset has almost 1.5 thousand rows and represents housing records "
        "from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, "
        "Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price "
        "for houses built between 1872 and 2010. \n "
    )

    # copied from README file - "Business Requirements" section
    st.success(
        "**The project has 2 business requirements:** \n\n"
        "* 1 - The client is interested in discovering how the house attributes correlate with the sale "
        "price. Therefore, the client expects data visualisations of the correlated variables against "
        "the sale price to show that. \n\n"
        "* 2 - The client is interested in predicting the house sale price from her four inherited "
        "houses and any other house in Ames, Iowa. \n\n"
    )

    # Link to README file, so the users can have access to full project documentation
    st.warning(
        "* For additional information, please visit and **read** the "
        "[Project README file](https://github.com/davep33l/pp5-house-price-predictor)."
        )
