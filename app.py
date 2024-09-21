from app_pages.multipage import MultiPage


# load pages scripts
from app_pages.project_summary import project_summary_body
from app_pages.project_hypothesis import project_hypothesis_body
from app_pages.project_sale_price_study import project_sale_price_study_body
from app_pages.project_predict_sale_price import project_predict_sale_price_body
from app_pages.project_ml_predict_sale_price import project_ml_predict_sale_price_body


app = MultiPage(app_name= "House Price Predictor") # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("Project Summary", project_summary_body)
app.add_page("Project Hypothesis", project_hypothesis_body)
app.add_page("Sale Price Study", project_sale_price_study_body)
app.add_page("Predict Sale Price", project_predict_sale_price_body)
app.add_page("ML: Predict Sale Price Pipeline Details", project_ml_predict_sale_price_body)


app.run()