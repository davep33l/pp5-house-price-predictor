# House Price Predictor

Live site can be viewed [here](https://pp5-house-price-predictor-3b886bb0d166.herokuapp.com/)

- [House Price Predictor](#house-price-predictor)
  - [Dataset Content](#dataset-content)
  - [Business Requirements](#business-requirements)
  - [Hypothesis and Validation?](#hypothesis-and-validation)
  - [The rationale to map the business requirements to the Data Visualisations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualisations-and-ml-tasks)
  - [ML Business Case](#ml-business-case)
    - [Predict Sale Price](#predict-sale-price)
  - [Epics \& User Stories](#epics--user-stories)
    - [Epic 1 - Data Collection](#epic-1---data-collection)
    - [Epic 2 - Data Cleaning](#epic-2---data-cleaning)
    - [Epic 3 - Data Exploration](#epic-3---data-exploration)
    - [Epic 4 - Feature Engineering](#epic-4---feature-engineering)
    - [Epic 5 - Modelling \& Evaluation](#epic-5---modelling--evaluation)
  - [Dashboard Design](#dashboard-design)
    - [Page 1 - Project Summary Page](#page-1---project-summary-page)
    - [Page 2 - Sale Price Study](#page-2---sale-price-study)
    - [Page 3 - Sale Price Prediction](#page-3---sale-price-prediction)
    - [Page 4 - Project Hypothesis and Validation](#page-4---project-hypothesis-and-validation)
    - [Page 5 - ML: Predict Sale Price Pipeline Details](#page-5---ml-predict-sale-price-pipeline-details)
  - [Unfixed Bugs](#unfixed-bugs)
  - [Deployment](#deployment)
    - [Heroku](#heroku)
      - [Prerequisites](#prerequisites)
      - [Deploying on Heroku using the Web UI](#deploying-on-heroku-using-the-web-ui)
    - [Forking the project](#forking-the-project)
    - [Cloning the project](#cloning-the-project)
  - [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
  - [Testing](#testing)
    - [PEP8 compliance](#pep8-compliance)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)


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

<div style="text-align: right;">
<a href="#house-price-predictor" style="font-size: 1em; font-style: italic; ">Back to Top</a>
</div>

## Business Requirements

A client has recently received an inheritance from a deceased great-grandfather, which contains properties located in Ames, Iowa. They have asked for assistance in maximising the sales price for the inherited properties.

Although the client has an excellent understanding of property prices in their own local area, they fear that basing their estimates for property value on their current knowledge may lead to inaccurate appraisals. What makes a house desirable and valuable in their local area, might not be the same in Ames, Iowa. They have found a public dataset containing house prices from Ames, Iowa and have provided it as part of the analysis. 

1. The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
2. The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.

<div style="text-align: right;">
<a href="#house-price-predictor" style="font-size: 1em; font-style: italic; ">Back to Top</a>
</div>

## Hypothesis and Validation?

1. Hypothesis 1 - Better quality decoration will positively influence the sale price (as higher quality materials are likely to have been used, and cost more). 
   * **Correct** - The correlation study performed in the House Price Study supports this. Along with the feature importance extraction within the Modelling and Evaluation stage.
2. Hypothesis 2 - Larger rooms/floors will positively influence the sale price (as it implies more land/space).
   * **Correct** - The correlation study performed in the House Price Study supports this. Along with the feature importance extraction within the Modelling and Evaluation stage.
3. Hypothesis 3 - New builds will positively influence the sale price (due to higher cost of materials / inflation)
   * **Partially Correct** - The correlation study performed in the House Price Study supported this. However the final model did not include the age of the property as being a defining feature in predicting house price

<div style="text-align: right;">
<a href="#house-price-predictor" style="font-size: 1em; font-style: italic; ">Back to Top</a>
</div>

## The rationale to map the business requirements to the Data Visualisations and ML tasks

* Business Requirement 1 - Data Visualization and Correlation Study
  * We will inspect the data related to the house features in Ames, Iowa
  * We will conduct a correlation study (Spearman and Pearson) to understand in more detail how the variables relate to the sale price.
  * We will plot the main variables against sale price and visualize the insights.

* Business Requirement 2 - Regression and Data Analysis
  * We want to predict the expected sale price of 4 inherited houses using a regression ML model

<div style="text-align: right;">
<a href="#house-price-predictor" style="font-size: 1em; font-style: italic; ">Back to Top</a>
</div>

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

<div style="text-align: right;">
<a href="#house-price-predictor" style="font-size: 1em; font-style: italic; ">Back to Top</a>
</div>

## Epics & User Stories

The CRISP-DM framework was fundamental in designing and producing this project, providing a clear road map for the Epics and User Story creation. The project was therefor broken down into 5 Epics, denoted below.

### Epic 1 - Data Collection

As a data scientist, I want to gather the housing data provided by the client so I can analyse the data set.

As a data scientist, I want to save the data within the project directory so I can easily work on the data throughout the project.

As a data scientist, I want to review high level observations on the data so I can identify potential issues and use these conclusions in data cleaning stage.


### Epic 2 - Data Cleaning

As a data scientist, I want to load in the house price data so I can start to clean the dataset.

As a data scientist, I want to review missing values in the dataset so that I can plan the best method to deal with those missing values.

As a data scientist, I want to run a correlation and PPS analysis on the data set so it can help guide the data imputation stage of the data cleaning process.

As a data scientist, I want to compare my train and test set split so I can ensure that each variable is represented appropriately. 

As a data scientist, I want to apply imputations to the data or drop columns with missing data so I compare the before and after effect on the distribution. 

As a data scientist, I want to create a pipeline with all the imputations so I can automate the data cleaning in the latter stages of the project.

As a data scientist, I want to apply the pipeline to my train, test and fullset so I can save the data and work on it during my data exploration and feature engineering stages.

### Epic 3 - Data Exploration

As a data scientist, I want to load in the cleaned full data set so I can garner more relevant insights for the client.

As a data scientist, I want to review the quanile statistics, descriptive statistics and visual distribution of the data so I can better understand the relationships between the features and house price. 

As a data scientist, I want to perform a correlation study on the data so I can select the most correlated variable to perform further analysis on. 

As a data scientist, I want to visualise the distribution on the most correlated variables vs sale price so I can present these findings to the client. 

As a data scientist, I want to visualise the correlation on the most correlated variables so I can present these findings to the client.

As a data scientist, I want to save the data so I use it within the streamlit application when presenting findings to the client. 

### Epic 4 - Feature Engineering

As a data scientist, I want to load in the cleaned train and test data so I can perform feature engineering on the data.

As a data scientist, I want to revist the data profiling so it can assist in determining which feature engineering transformations can be applied to the data. 

As a data scientist, I want to group the data into relevant categories so I can apply various initial transformations to the data to help decide which transformation performed the best. 

As a data scientist, I want to create a pipeline with all the feature engineering steps so I can automate the feature engineering in the latter stages of the project.

### Epic 5 - Modelling & Evaluation

As a data scientist, I want to load in the raw data set so I can perform the ML pipeline to the data. 

As a data scientist, I want to define the ML pipeline so I can split into train and test sets. 

As a data scientist, I want to perform a Grid Search CV so I can determine the most suitable algorithm. 

As a data scientist, I want to perform hyperparameter optimisation on the best algorithm determined in the grid search and apply recommended parameters for that alogithm to see if the model improves.

As a data scientist, I want to select the best model and perform feature importance on the model so we can trim down the model to include only the best features. 

As a data scientist, I want to perform the regression on the train and test sets independantly so I can assess the R2 score.

As a data scientist, I want to refit the pipeline with only the best features to reduce the size of the model.

As a data scientist, I want to check that the reduced pipeline maintains its R2 score so I can determine if the refit was a success.

As a data scientist, I want to save the model so it can be used in the streamlit app to predict the house price of the inherited houses. 

## Dashboard Design

### Page 1 - Project Summary Page
  * This will contain:
    * The project purpose
    * The project terms and jargon with a breakdown of all the features and description
    * The source of the dataset used
    * The business requirements
    * The link to the github repository

### Page 2 - Sale Price Study
  * This will contain:
    * Details of business requirement 1
    * An inspection of the data set 
    * Details of the features used in the correlation study
    * Conclusions of how the features relate to Sale price
    * A checkbox to show a scatter plot visualising the feature distrubution vs sale price
    * A checkbox to show correlation study heatmaps and power predictive score 

### Page 3 - Sale Price Prediction
  * This will contain:
    * Details of business requirement 2
    * Have input widgets relating to house features, which are given to an ML task to predict the Sale Price. 
    * A button for the user to run the predictive analysis on
    * A section where the predictive analysis has been run on the inherited houses with their results

### Page 4 - Project Hypothesis and Validation
  * This will contain:
    * Each of the project hypothesis and the conclusion (Incorrect/Correct) 
  
### Page 5 - ML: Predict Sale Price Pipeline Details
  * This will contain:
    * A section explaining how we trained the data
    * A section showing the pipeline used including the different imputations and feature engineering steps
    * The features that the model was trained on
    * The importance of each feature
    * The performance of the pipeline and visual scatter plot

<div style="text-align: right;">
<a href="#house-price-predictor" style="font-size: 1em; font-style: italic; ">Back to Top</a>
</div>

## Unfixed Bugs

* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not valid reason to leave bugs unfixed.

<div style="text-align: right;">
<a href="#house-price-predictor" style="font-size: 1em; font-style: italic; ">Back to Top</a>
</div>

## Deployment

### Heroku

* The App live link is: <[https://YOUR_APP_NAME.herokuapp.com/](https://pp5-house-price-predictor-3b886bb0d166.herokuapp.com/)>

#### Prerequisites

* Set the `runtime.txt` Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.

```
python-3.8.19
```

* Ensure the root directory contains the following `setup.sh` script as this contains the parameters for setting up streamlit.
  
```bash
mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```
* Ensure the root directory contains a `Procfile` for Heroku containing the following. This ensures that Heroku knows what parameters to set for streamlit and server the right ports, and then knows to run the command for starting the streamlit app

```
web: sh setup.sh && streamlit run app.py
```
* General point of note, is to ensure that your `requirements.txt` file has all of the dependencies your project requires. As a reminder, run the following command to set your requirements.

```
pip freeze > requirements.txt
```
#### Deploying on Heroku using the Web UI
1. Log into Heroku using the [this](https://id.heroku.com/login) link. Where you can log in using your email address and password, or create a new account.

![Heroku Login Page](/assets/readme/heroku-login-page.png)

2. Once logged in, from the [app](https://dashboard.heroku.com/apps) page, select "New" from the top right.

![Heroku New App](/assets/readme/heroku-new-app.png)

3. Select Create New App

![Heroku Create New App](/assets/readme/heroku-create-new-app.png)

4. Give your App a memorable name, select a local region and select create app.
   
![Heroku Create New App 2](/assets/readme/heroku-create-new-app-2.png)

5. From the Deploy tab, select Github as the deployment method and select your repo to connect

![Heroku Deployment Settings](/assets/readme/heroku-deployment-settings.png)

6. On the same Deploy tab, select the branch you want to deploy, then click deploy branch

![Heroku Deploy Branch](/assets/readme/heroku-deploy-branch.png)

7. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.

![Heroku Open App](/assets/readme/heroku-open-app.png)

8.  If the slug size is too large then add large files not required for the app to the .slugignore file.

### Forking the project

1. Navigate to the [Github Repo](https://github.com/davep33l/pp5-house-price-predictor)
2. Select the "Fork" option and save it to your own Github account

### Cloning the project

1. Navigate to the [Github Repo](https://github.com/davep33l/pp5-house-price-predictor)
2. Select the "Code" button
3. Copy the HTTPS link
4. Create a new directory for the project on your local development environment
5. Open up your terminal of choice 
6. Type the following command
```
git clone https://github.com/davep33l/pp5-house-price-predictor.git
```

<div style="text-align: right;">
<a href="#house-price-predictor" style="font-size: 1em; font-style: italic; ">Back to Top</a>
</div>

## Main Data Analysis and Machine Learning Libraries

| Library Name | Example Usage |
|--------------|---------------|
| [numpy](https://numpy.org/) | Used in core visualization functions to manipulate data types. |
| [pandas](https://pandas.pydata.org/docs/index.html) | Used for data handling by utilizing the DataFrame object. |
| [matplotlib](https://matplotlib.org/) | Used for plotting various charts and visuals to provide evidence and conclusions on the data. |
| [seaborn](https://seaborn.pydata.org/) | Used for plotting various charts and visuals to provide evidence and conclusions on the data. |
| [sklearn](https://scikit-learn.org/stable/) | Used to create an ML pipeline, run ML algorithms, split train and test sets, and provide R² metric scores. |
| [feature-engine](https://feature-engine.trainindata.com/en/latest/) | Used to perform imputation and feature engineering encoding supplied to the sklearn pipeline. |
| [ydata_profiling](https://docs.profiling.ydata.ai/latest/) | Used to create quantile and statistical reports on the variables. |
| [os](https://docs.python.org/3/library/os.html) | Used to assist in loading data, creating files/directories, and loading environment variables. |
| [ppscore](https://pypi.org/project/ppscore/) | Used to calculate the Power Predictive Score for variables. |
| [scipy](https://scipy.org/) | Used as part of the feature engineering analysis to produce statistics. |
| [xgboost](https://xgboost.readthedocs.io/en/stable/) | Used to assess the best possible algorithms for the data. |
| [joblib](https://joblib.readthedocs.io/en/stable/) | Used to save and load the model pipeline. |
| [streamlit](https://streamlit.io/) | Used to create an interactive web application to showcase the project. |

<div style="text-align: right;">
<a href="#house-price-predictor" style="font-size: 1em; font-style: italic; ">Back to Top</a>
</div>

## Testing

I installed `nbqa` using in order to use `flake8` on my notebooks:

```
pip install nbqa
``` 
Then run `flake8` against each notebook using the following command:

```
nbqa flake8 <notebook>
# example
nbqa flake8 jupyter_notebooks/1_Data_Collection.ipynb
```

### PEP8 compliance

|Notebook name|Initial Results from Flake8|After Fixing Results|Summary|
|-------------|---------------|-------------|-------|
|1_Data_Collection.ipynb|![PEP8 Notebook 1 Before](/assets/testing/pep8-notebook-1-before.png)  |![PEP8 Notebook 1 After](/assets/testing/pep8-notebook-1-after.png) |I decided to leave these errors as they are specifically for file paths and its more readable this way|
|2_Data_Cleaning.ipynb|![PEP8 Notebook 2 Before](/assets/testing/pep8-notebook-2-before-1.png) ![PEP8 Notebook 2 Before 2](/assets/testing/pep8-notebook-2-before-2.png)   |![PEP8 Notebook 2 After](/assets/testing/pep8-notebook-2-after.png) |All errors fixed except for line lengths which are mainly for text prints and one which is an unused variable from the CI provided function. I did fix the formatting in the functions provided by CI to be more PEP8 compliant|
|3_House_Price_Study.ipynb|![PEP8 Notebook 3 Before](/assets/testing/pep8-notebook-3-before.png)  |![PEP8 Notebook 3 After](/assets/testing/pep8-notebook-3-after.png) |All errors fixed except for line lengths which are mainly for text prints and one which is an unused variable from the CI provided function. I did fix the formatting in the functions provided by CI to be more PEP8 compliant|
|4_Feature_Engineering.ipynb|![PEP8 Notebook 4 Before](/assets/testing/pep8-notebook-4-before.png)  |![PEP8 Notebook 4 After](/assets/testing/pep8-notebook-4-after.png) |All errors fixed except for line lengths which are mainly for text prints and one which is an unused variable from the CI provided function.|
|5_Modelling_And_Evaluation.ipynb|![PEP8 Notebook 5 Before](/assets/testing/pep8-notebook-5-before-1.png) ![PEP8 Notebook 5 Before 2](/assets/testing/pep8-notebook-5-before-1.png)  |![PEP8 Notebook 5 After](/assets/testing/pep8-notebook-5-after.png) |All errors fixed except for line lengths which are mainly for text prints.|
| multipage.py| ![PEP8 multipage.py Before](/assets/testing/pep8-multipage-before.png) | ![PEP8 multipage.py After](/assets/testing/pep8-multipage-after.png) | No Issues |
| project_summary.py | ![PEP8 project_summary.py Before](/assets/testing/pep8-project_summary-before.png) | ![PEP8 project_summary.py After](/assets/testing/pep8-project_summary-after.png) | Retained lines that are over the recommended amount for readability in the table for readability |
| project_hypothesis.py| ![PEP8 project_hypothesis.py Before](/assets/testing/pep8-project_hypothesis-before.png) | ![PEP8 project_hypothesis.py After](/assets/testing/pep8-project_hypothesis-after.png) | No Issues |
| project_sale_price_study.py| ![PEP8 project_sale_price_study.py Before](/assets/testing/pep8-project_sale_price_study-before.png) | ![PEP8 project_sale_price_study.py After](/assets/testing/pep8-project_sale_price_study-after.png) | Kept a few warnings to maintain readability |
| project_predict_sale_price.py| before | after | comments |
| project_ml_predict_sale_price.py| ![PEP8 project_ml_predict_sale_price.py Before](/assets/testing/pep8-ml_predict_sale_price-before.png) | ![PEP8 project_ml_predict_sale_price.py After](/assets/testing/pep8-ml_predict_sale_price-after.png) | Kept a few warnings to maintain readability |
| data_management.py| before | after | comments |
| evaluate_regression.py| before | after | comments |
| predictive_analysis.py| before | after | comments |

![alt text](image.png)
<div style="text-align: right;">
<a href="#house-price-predictor" style="font-size: 1em; font-style: italic; ">Back to Top</a>
</div>

## Credits

* I would not have been able to complete this project without the Churnometer walkthrough project as a support, it provided the structure and guidance I needed to piece this project together. 

<div style="text-align: right;">
<a href="#house-price-predictor" style="font-size: 1em; font-style: italic; ">Back to Top</a>
</div>

## Acknowledgements

* I want to thank my wife for giving me the freedom to `commit` (pun intended) to this course for the past year, and more recently giving me the extra time, even though we have a new born son to raise. Without her support and encouragement I could not have seen this through to the end. 

<div style="text-align: right;">
<a href="#house-price-predictor" style="font-size: 1em; font-style: italic; ">Back to Top</a>
</div>