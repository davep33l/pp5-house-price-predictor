# House Price Predictor

Live site can be viewed [here](https://pp5-house-price-predictor-3b886bb0d166.herokuapp.com/)

## Dataset Content

* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|

## Business Requirements

A client has recently received an inheritance from a deceased great-grandfather, which contains properties located in Ames, Iowa. They have asked for assistance in maximising the sales price for the inherited properties.

Although the client has an excellent understanding of property prices in their own local area, they fear that basing their estimates for property value on their current knowledge may lead to inaccurate appraisals. What makes a house desirable and valuable in their local area, might not be the same in Ames, Iowa. They have found a public dataset containing house prices from Ames, Iowa and have provided it as part of the analysis. 

1. The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
2. The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.

## Hypothesis and how to validate?

1. Hypothesis 1 - Better quality decoration will positively influence the sale price (as higher quality materials are likely to have been used, and cost more). 
2. Hypothesis 2 - Larger rooms/floors will positively influence the sale price (as it implies more land/space).
3. Hypothesis 3 - New builds will positively influence the sale price (due to higher cost of materials / inflation)

## The rationale to map the business requirements to the Data Visualisations and ML tasks

* Business Requirement 1 - Data Visualization and Correlation Study
  * We will inspect the data related to the house features in Ames, Iowa
  * We will conduct a correlation study (Spearman and Pearson) to understand in more detail how the variables relate to the sale price.
  * We will plot the main variables against sale price and visualize the insights.

* Business Requirement 2 - Regression and Data Analysis
  * We want to predict the expected sale price of 4 inherited houses using a regression ML model

## ML Business Case

### Predict Sale Price

- We want an ML model to predict the Sale Price of a house in Ames, Iowa. As the target is a continuous variable a regression model will be the best approach. The model will be supervised and multi-dimensional. 
- Our ideal outcome is to provide the client the ability to predict the sale price of houses in Ames, Iowa for the inherited properties they received.
- The model success metrics are:
  - At least a 0.75 R2 score on both the train and test sets. 
- The model is considered a failure if:
  - The model does not provide any actionable insights for the client to take to maximise the sale price of the inherited properties.
- The model output is defined as a numerical value, which represents the predicted sale price of the house. 
- Heuristics: The client's currently estimations of property prices in her local area may not be relevant to Ames, Iowa. Therefore, requested that analysis be performed on a dataset specific to Ames, Iowa.
- The training data to fit the model comes from the client and consists of approximately 1,500 records. The Target is SalePrice and the features will be all other variables in from the dataset.

## Dashboard Design

* Project Summary Page
  * This will contain:
    * The project purpose
    * The project terms and jargon with a breakdown of all the features and description
    * The source of the dataset used
    * The business requirements
    * The link to the github repository

* Project Hypothesis
  * This will contain:
    * Each of the project hypothesis and the conclusion (Incorrect/Correct) 

* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items that your dashboard library supports.
* Eventually, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but eventually you needed to use another plot type)

### Page 1 - Project Summary
### Page 2 - Sale Price Study
#### Before Analysis
- High level, we know we want to answer business requirement 1, and as part of the analysis will explore the best visulisations to show the correlation of variables against the Sale Price.
#### After Analysis
- TBD
### Page 3 - Sale Price Prediction
- Highlight business requirement 2
- Have input widgets relating to house features, which are given to an ML task to predict the Sale Price. 
### Page 4 - Project Hypothesis and Validation
### Page 5 - ML: Process to determine Sale Price (placeholder name)

## Unfixed Bugs

* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not valid reason to leave bugs unfixed.

## Deployment

### Heroku

* The App live link is: <https://YOUR_APP_NAME.herokuapp.com/>
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

* Here you should list the libraries you used in the project and provide example(s) of how you used these libraries.

| Library Name | Example Usage |
|--------------|---------------|
|       numpy       |        tbc       |
|       pandas       |        tbc        |
|       matplotlib      |      tbc          |
|       scikit-learn   |      tbc          |
|       feature-engine   |     tbc           |
|       ydata-profiling   |      tbc          |
|       plotly   |        tbc        |
|       ppscore   |      tbc          |
|       streamlit   |      tbc          |


## Credits

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism.
* You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

* The text for the Home page was taken from Wikipedia Article A
* Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
* The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

* The photos used on the home and sign-up page are from This Open Source site
* The images used for the gallery page were taken from this other open-source site

## Acknowledgements (optional)


* In case you would like to thank the people that provided support through this project.

